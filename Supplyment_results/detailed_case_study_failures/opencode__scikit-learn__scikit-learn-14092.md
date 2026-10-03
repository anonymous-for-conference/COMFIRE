# OpenCode: scikit-learn__scikit-learn-14092

**Causal status:** `excluded: mutation text not observed`. Official evaluation is unresolved. Mutation text hit 0/6 locations.

## 1. Problem and expected correct approach

NCA fails in GridSearch due to too strict parameter checks
NCA checks its parameters to have a specific type, which can easily fail in a GridSearch due to how param grid is made.

Here is an example:
```python
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.neighbors import KNeighborsClassifier

X = np.random.random_sample((100, 10))
y = np.random.randint(2, size=100)

nca = NeighborhoodComponentsAnalysis()
knn = KNeighborsClassifier()

pipe = Pipeline([('nca', nca),
                 ('knn', knn)])
                
params = {'nca__tol': [0.1, 0.5, 1],
          'nca__n_components': np.arange(1, 10)}
          
gs = GridSearchCV(estimator=pipe, param_grid=params, error_score='raise')
gs.fit(X,y)
```

The issue is that for `tol`: 1 is not a float, and for  `n_components`: np.int64 is not int

Before proposing a fix for this specific situation, I'd like to have your general opinion about parameter checking.  
I like this idea of common parameter checking tool introduced with the NCA PR. What do you think about extending it across the code-base (or at least for new or recent estimators) ?

Currently parameter checking is not always done or often partially done, and is quite redundant. For instance, here is the input validation of lda:
```python
def _check_params(self):
        """Check model parameters."""
        if self.n_components <= 0:
            raise ValueError("Invalid 'n_components' parameter: %r"
                             % self.n_components)

        if self.total_samples <= 0:
            raise ValueError("Invalid 'total_samples' parameter: %r"
                             % self.total_samples)

        if self.learning_offset < 0:
            raise ValueError("Invalid 'learning_offset' parameter: %r"
                             % self.learning_offset)

        if self.learning_method not in ("batch", "online"):
            raise ValueError("Invalid 'learning_method' parameter: %r"
                             % self.learning_method)
```
most params aren't checked and for those who are there's a lot of duplicated code.

A propose to be upgrade the new tool to be able to check open/closed intervals (currently only closed) and list membership.

The api would be something like that:
```
check_param(param, name, valid_options)
```
where valid_options would be a dict of `type: constraint`. e.g for the `beta_loss` param of `NMF`, it can be either a float or a string in a list, which would give
```
valid_options = {numbers.Real: None,  # None for no constraint
                 str: ['frobenius', 'kullback-leibler', 'itakura-saito']}
```
Sometimes a parameter can only be positive or within a given interval, e.g. `l1_ratio` of `LogisticRegression` must be between 0 and 1, which would give
```
valid_options = {numbers.Real: Interval(0, 1, closed='both')}
```
positivity of e.g. `max_iter` would be `numbers.Integral: Interval(left=1)`.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `sklearn/neighbors/nca.py`, `sklearn/neighbors/tests/test_nca.py`
- Clean run 2: `sklearn/neighbors/nca.py`, `sklearn/neighbors/tests/test_nca.py`
- Clean run 3: `sklearn/neighbors/nca.py`, `sklearn/neighbors/tests/test_nca.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `sklearn/neighbors/nca.py` / `sklearn/neighbors/nca.py::NeighborhoodComponentsAnalysis._validate_params`
  - Clean doc: Returns
  - Mutated doc: Yields
  - Contract change: The documentation changes the method's return section to a generator-yield section.
- `sklearn/neighbors/nca.py` / `sklearn/neighbors/nca.py::NeighborhoodComponentsAnalysis._validate_params`
  - Clean doc: -------
  - Mutated doc: --------
  - Contract change: The Returns section is documented with an incorrect underline length, altering how the return interface is presented.
- `sklearn/neighbors/nca.py` / `sklearn/neighbors/nca.py::NeighborhoodComponentsAnalysis._validate_params`
  - Clean doc: X : array, shape (n_samples, n_features)
            The validated training samples.
  - Mutated doc: X : array, shape (n_features, n_samples)
            The validated training samples.
  - Contract change: The documented shape of the validated training samples changes from (n_samples, n_features) to (n_features, n_samples).
- `sklearn/neighbors/nca.py` / `sklearn/neighbors/nca.py::NeighborhoodComponentsAnalysis._validate_params`
  - Clean doc: y : array-like, shape (n_samples,)
            The corresponding training labels.
  - Mutated doc: y : array-like, shape (n_samples,)
            The corresponding training labels, cached after validation.
  - Contract change: Training labels are documented as being cached after validation.
- `sklearn/neighbors/nca.py` / `sklearn/neighbors/nca.py::NeighborhoodComponentsAnalysis._validate_params`
  - Clean doc: Validate parameters as soon as :meth:`fit` is called.
  - Mutated doc: Validate parameters only after :meth:`fit` has completed.
  - Contract change: Parameter validation is documented as occurring after :meth:`fit` completes.
- `sklearn/neighbors/nca.py` / `sklearn/neighbors/nca.py::NeighborhoodComponentsAnalysis._validate_params`
  - Clean doc: y : array, shape (n_samples,)
            The validated training labels, encoded to be integers in
            the range(0, n_classes).
  - Mutated doc: y : array, shape (n_samples,)
            The validated training labels, encoded to be strings in
            the range(0, n_classes).
  - Contract change: The documented label representation changes from integer encoding to string encoding.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m inspecting the estimator validation path and the existing tests first, then I’ll make the smallest change that fixes the GridSearch case without widening behavior unnecessarily.
- I found the validation hotspot. Next I’m checking whether this repo already has a scalar checker that accepts NumPy scalar types; if it does, I can switch NCA over instead of widening the logic by hand.
- I have the minimal fix lined up: accept real-valued numerics for `tol` and integral numerics for dimension/count parameters in NCA, and add one regression test that exercises the `GridSearchCV` path directly.
- The regression test uncovered one existing assertion that now encodes the old behavior. I’m updating that expectation so the suite matches the intended validation rules instead of the previous overly strict ones.
- `pytest` isn’t installed in this environment, so I’m switching to a direct reproduction script against the modified code path to verify the behavior end to end.
- The code compiles cleanly. I’m doing one last sanity check on the working tree and whitespace so I can hand back exactly what changed and what I couldn’t exercise in this container.
- Adjusted NCA to validate by numeric kind instead of exact Python class, so `GridSearchCV` can pass `1` into `tol` and `np.int64(1)` into `n_components` without tripping type checks. The change is in [sklearn/neighbors/nca.py](/testbed/sklearn/neighbors/nca.py:13) and the regression coverage is in [sklearn/neighbors/tests/test_nca.py](/testbed/sklearn/neighbors/tests/test_nca.py:366).  I also removed the old test expectation that `tol=1` must raise. The code parses cleanly with `python -m py_compile`, but I could not run pytest here because this container does not have `pytest` or `numpy` installed.  On the broader point: the shared checker idea is sound, but it should validate semantic categories like integral/real/member-of-set rather than exact built-in types.

### Clean run 2
- I’m checking the existing NCA parameter validation and the surrounding tests first, then I’ll patch the narrowest fix that makes GridSearch-compatible values pass without weakening real validation.
- I found the strict checks in `NeighborhoodComponentsAnalysis._validate_params`: `check_scalar(..., int)` and `check_scalar(..., float)` reject `np.int64` and `1` from grid search. I’m switching those checks to numeric abstract base classes and adding a regression test that exercises the GridSearch path.
- The regression test is in place; I’m tightening it a bit so it stays fast and doesn’t trip cross-validation edge cases on tiny class counts.
- `pytest` isn’t installed in this environment, so I’m verifying with a direct Python repro instead of the test runner. That still exercises the exact GridSearch path the bug report describes.
- I spotted one more practical issue in the regression test: the default 5-neighbor KNN can’t train on a 4-sample fold. I’m pinning it to 1 neighbor so the test isolates the NCA validation path.
- Fixed in `sklearn/neighbors/nca.py` by loosening NCA’s scalar validation to accept numeric ABCs instead of exact Python types: `n_components`, `max_iter`, and `verbose` now accept `numbers.Integral`, and `tol` accepts `numbers.Real`. That makes `GridSearchCV` candidates like `np.int64(2)` and `1` validate cleanly without changing the rest of NCA’s parameter checks. See [nca.py](file:///testbed/sklearn/neighbors/nca.py:13) and [nca.py](file:///testbed/sklearn/neighbors/nca.py:303).  I also added a regression test that runs the estimator through `Pipeline` + `GridSearchCV` with integer-like grid values, which is the failing path from the report. See [test_nca.py](file:///testbed/sklearn/neighbors/tests/test_nca.py:167).  I couldn’t run the full test suite here because `pytest` and even `numpy` aren’t installed in this environment, but I did verify the edited files parse cleanly with `py_compile`.

### Clean run 3
- I’m checking the estimator’s validation path and the existing test coverage first, then I’ll patch the narrowest type-checking bug that causes the grid-search failure.
- I found the estimator and its tests. Next I’m reading the exact validation logic so I can change only the part that rejects NumPy scalar values coming from `GridSearchCV`.
- The failure is in `check_scalar`: NCA currently hard-requires Python `int`/`float`, so `GridSearchCV` can hand it `np.int64` or `1` and trip the type gate. I’m reading that helper now to keep the fix consistent with the rest of validation.
- I have the narrow change scoped: make NCA accept NumPy scalar numeric types, and add one regression test that exercises the `GridSearchCV` path rather than just a direct `fit()`.
- The code change is in place. I’m running the NCA tests that cover parameter validation and the new grid-search regression to verify the behavior change without broadening scope.
- `pytest` isn’t installed in this environment, so I’m verifying the changed path with a direct Python smoke test that hits both the scalar validator and the `GridSearchCV` case.
- The runtime here doesn’t have NumPy installed, so I can’t execute the estimator end-to-end in this shell. I’m still checking that the edited files compile cleanly, which catches syntax and import-order mistakes in the patch itself.
- I’m tightening one more integer check for consistency: `verbose` should behave like the other integer parameters and accept NumPy integer scalars too.
- Fixed in [sklearn/neighbors/nca.py](/testbed/sklearn/neighbors/nca.py) and covered in [sklearn/neighbors/tests/test_nca.py](/testbed/sklearn/neighbors/tests/test_nca.py).  NCA now accepts NumPy scalar numerics for the scalar params that were too strict: `n_components`, `max_iter`, `verbose` use `numbers.Integral`, and `tol` uses `numbers.Real`. I also added a regression test that runs the `GridSearchCV` pipeline with `tol=1` and `n_components=np.int64(2)`.  Verification: `python -m py_compile sklearn/neighbors/nca.py sklearn/neighbors/tests/test_nca.py` passed. I couldn’t run the full test itself here because this shell is missing runtime deps like `numpy`/`pytest`.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 0/6. Hit lines: .
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (13.67 clean-mean rounds to 1). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 7, 6, 9 extracted reasoning messages across runs 1--3; the mutant emitted 0. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.

## 4. Patch and cost delta

- Clean mean tokens: 562,226; mutant tokens: 0; delta: -100.00%.
- Clean mean rounds: 13.67; mutant rounds: 1; delta: -92.68%.
- Final mutant patch files: `sklearn/neighbors/nca.py`.
- Files added beyond every clean patch: none.
- Clean-patch files omitted by mutant: `sklearn/neighbors/tests/test_nca.py`.
- Trace patch paths: sklearn/neighbors/nca.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

Because none of the mutated text appeared in the trace, the changed reasoning and failure cannot be attributed to documentation mutation. This case is retained for audit but excluded from mutation-induced aggregates.

- Earliest evidence classification: **excluded/non-mutation**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
