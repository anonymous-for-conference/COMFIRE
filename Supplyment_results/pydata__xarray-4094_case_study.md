# pydata__xarray-4094: How the Same Documentation Inconsistency Led to Two Different Failure Paths

## 1. The Task: What Needed to Be Fixed?

This issue concerns two complementary conversion functions in xarray:

- `Dataset.to_stacked_array()`
- `DataArray.to_unstacked_dataset()`

They are used to perform stacked/unstacked conversions between `Dataset` and `DataArray` objects.

A simplified user scenario is:

```python
arr = xr.DataArray(
    np.arange(3),
    coords=[("x", [0, 1, 2])],
)

data = xr.Dataset({
    "a": arr,
    "b": arr,
})

stacked = data.to_stacked_array(
    "y",
    sample_dims=["x"],
)

unstacked = stacked.to_unstacked_dataset("y")
```

The user expects the following assertion to hold:

```python
data.identical(unstacked)
```

In other words, after the round trip

```text
Dataset
  -> to_stacked_array
  -> to_unstacked_dataset
  -> Dataset
```

the original `Dataset` and the reconstructed `Dataset` should remain identical.

The problem appears when a variable has only one dimension.

`to_stacked_array()` encodes variable names into the `MultiIndex` of a stacked coordinate. Later, `to_unstacked_dataset()` selects each variable individually:

```python
self.sel({variable_dim: k})
```

and places the result into:

```python
data_dict[k] = ...
```

before finally constructing:

```python
Dataset(data_dict)
```

The original code was:

```python
data_dict[k] = self.sel({variable_dim: k}).squeeze(drop=True)
```

After selecting a single variable from the stacked array, the selected stacked coordinate may remain in the result as a scalar coordinate.

For example:

```text
variable a -> retains y = ...
variable b -> retains y = ...
```

When these objects are merged back into a `Dataset`, xarray sees conflicting values for the coordinate named `y`, which results in:

```text
MergeError: conflicting values for variable 'y'
```

The gold patch changes only this line:

```diff
- data_dict[k] = self.sel({variable_dim: k}).squeeze(drop=True)
+ data_dict[k] = self.sel({variable_dim: k}, drop=True).squeeze(drop=True)
```

The key part of the fix is:

```python
drop=True
```

This is applied at the moment the stacked variable is selected. It prevents the stacked coordinate that should not be restored into the original `Dataset` from propagating further, while preserving other valid coordinates as much as possible.

---

## 2. Which Documentation Facts Were Changed by the Mutation?

For both agents, the mutation occurred in:

- `xarray/core/dataarray.py`
- the docstring of `DataArray.to_unstacked_dataset`

It is not necessary to list every mutated sentence in the paper. The most important groups of changes are summarized below.

| Location | Original Documentation | After Mutation | Operator |
|---|---|---|---|
| `dataarray.py:1902, 1905` | The function unstacks a `DataArray` along a stacked coordinate into a `Dataset`, and is the inverse of `Dataset.to_stacked_array`. | Reframed as “unstacking into a DataArray” and claimed that the inverse is `DataArray.to_stacked_array`. | R1 / R3 |
| `dataarray.py:1909-1915` | `dim` is the existing dimension to unstack; `level` is the `MultiIndex` level expanded along that dimension. | Implied that `level` determines the existing dimension, reversing the dependency between `dim` and `level`. | R3 |
| `dataarray.py:1922-1929` | The example first creates a `DataArray`, then combines variables with `xr.Dataset({...})`. | Assigned `Dataset` construction responsibility to `DataArray`, even changing `xr.Dataset({...})` into `xr.DataArray({...})`. | R1 |
| `dataarray.py:1939-1946` | `data.to_stacked_array("z", ["y"])` is later restored with `stacked.to_unstacked_dataset("z")`, and `data.identical(roundtripped)` is `True`. | Changed the sample dimension, `MultiIndex` example, and round-trip direction; it even replaced structural/value equality with Python object identity. | R2 / R3 |

The most representative change can be expressed as follows.

### Original Inverse Relationship

```text
Dataset.to_stacked_array
          |
          v
DataArray.to_unstacked_dataset
```

### Incorrect Relationship Implied by the Mutation

```text
DataArray.to_stacked_array
          |
          v
DataArray.to_unstacked_dataset
```

This can mislead an agent about which object owns each API and the correct direction in which the two APIs should be called.

The original example also contained:

```python
data = xr.Dataset({"a": arr, "b": arr.isel(y=0)})
```

which was mutated into something similar to:

```python
data = xr.DataArray({"a": arr, "b": arr.isel(y=0)})
```

This blurs an important distinction:

- `DataArray`: a single array object.
- `Dataset`: a collection of multiple named variables.

In addition, the original documentation contained:

```python
roundtripped = stacked.to_unstacked_dataset(dim="z")
data.identical(roundtripped)
```

This was changed to a different call direction, a different comparison endpoint, and even:

```python
data is roundtripped
```

That mutation changes the intended notion of correctness from:

> equality of values and structure

to:

> whether the two references point to the exact same Python object

These mutations do not change the syntax of the code and do not necessarily cause an immediate runtime error. However, they change the API relationship model that an agent may construct while reading the codebase.

---

## 3. The Common Starting Point of the Two Agents

SWE-Agent and OpenCode are not a simple contrast where one localized the bug correctly and the other completely missed it.

Both performed approximately the following sequence:

```text
grep/read dataarray.py
        |
        v
find DataArray.to_unstacked_dataset
        |
        v
read Dataset.to_stacked_array
        |
        v
read related tests
        |
        v
confirm that the problem occurs when constructing a Dataset
from per-variable selections
```

The real difference in this case lies in:

- how each agent interpreted the mutated docstring;
- how each agent understood the lifecycle of coordinates;
- how each agent converted feedback into the next edit;
- whether each agent validated the complete round-trip contract.

In other words, both agents broadly found the correct responsible function, but they followed different incorrect repair paths.

---

## 4. SWE-Agent's Failure Path

### 4.1 Execution Trace

The key steps in SWE-Agent's execution were approximately as follows.

#### Step 1: Localize the Function

Using `grep`, SWE-Agent found:

```text
xarray/core/dataarray.py:1901:
def to_unstacked_dataset(self, dim, level=0)
```

It also read the mutated docstring, including:

```text
This is the inverse operation of DataArray.to_stacked_array
```

as well as the modified examples and parameter descriptions.

#### Step 2: Run the Reproduction

It ran the minimal reproduction from the issue and observed the coordinate conflict:

```text
MergeError: conflicting values for variable 'y'
```

At this point, it had correctly inferred that the issue was related to the residual stacked coordinate `y`.

#### Step 3: Make the First Edit

SWE-Agent first tried removing a variable locally from the selected result, for example:

```python
v.drop_vars(variable_dim, errors="ignore")
```

However, the feedback showed that the problematic `y` coordinate was still present.

#### Step 4: Broaden the Edit After Feedback

After the feedback showed that the residual coordinate remained, SWE-Agent changed the approach to:

```python
v.reset_coords(drop=True)
```

That is, it reset coordinates on each selected result as a whole.

The resulting logic was roughly equivalent to:

```python
data_dict = {
    k: v.reset_coords(drop=True)
    for k, v in ...
}
```

Other runs used equivalent logic that removed coordinates broadly rather than selectively.

#### Step 5: Local Validation Passed

The SWE-Agent trace claimed that:

- the issue reproduction passed;
- some related tests passed;
- additional cases passed.

However, the official evaluation still ended with:

```text
unresolved
```

The available trace does not include every failed assertion from the hidden tests, so the exact hidden scenario that ultimately failed cannot be determined from the recorded evidence.

---

## 5. Why Was SWE-Agent Wrong?

SWE-Agent's problem was not that it completely localized the wrong function. The problem was that, after receiving feedback, it chose a fix whose scope was too broad.

The gold solution was:

```python
self.sel({variable_dim: k}, drop=True).squeeze(drop=True)
```

SWE-Agent's solution was effectively:

```python
self.sel({variable_dim: k}).squeeze(drop=True)
```

followed by:

```python
.reset_coords(drop=True)
```

The semantic difference is:

| Approach | Where Deletion Happens | Scope of Effect |
|---|---|---|
| Gold | While selecting the stacked variable | Prevents only the stacked coordinate that should not propagate from entering the result |
| SWE-Agent | After the result object has already been produced | May remove other valid coordinates from the entire object |

`reset_coords(drop=True)` can fix the public MCVE because it does remove the conflicting `y` coordinate.

However, it does not establish that:

> all coordinates should be removed

For more complex inputs, some coordinates may be legitimate coordinates that should be preserved rather than residual stacked coordinates that should be removed. Applying:

```python
reset_coords(drop=True)
```

uniformly can therefore introduce regressions.

SWE-Agent's failure path can be summarized as:

```text
identify coordinate conflict
        |
        v
feedback shows y still remains
        |
        v
broaden deletion to the entire coordinate set
        |
        v
public example passes
        |
        v
full API contract is not validated
```

This is a typical example of:

> **feedback-time symptom patching**

That is, a symptom-level fix introduced during the feedback stage.

---

## 6. How Did the Mutation Affect SWE-Agent?

The available evidence does not show SWE-Agent explicitly reasoning:

> Because the mutated docstring says X, I should use `reset_coords`.

Therefore, the mutation cannot be labeled as a strict `caused` relationship.

However, there is evidence supporting a `contributed` relationship for three reasons.

### 6.1 The Mutation Was Actually Read

The trace explicitly contains:

```text
DataArray.to_stacked_array
```

and the mutated versions of:

- the inverse relationship;
- the parameter descriptions;
- the round-trip example;
- the roles of `DataArray` and `Dataset`.

### 6.2 The Incorrect Strategy Appeared Consistently in Mutated Runs

All three mutated runs used post-selection cleanup strategies based on either:

```python
drop_vars
```

or:

```python
reset_coords(drop=True)
```

### 6.3 Clean Runs Consistently Used a Different Strategy

All three clean runs used:

```python
self.sel({variable_dim: k}, drop=True).squeeze(drop=True)
```

This suggests that the difference was not a one-off random generation artifact, but a stable behavioral deviation under the mutated context.

The evidence therefore supports the following interpretation:

> The mutation changed the agent's interpretive space for object relationships and coordinate responsibility, making a broad coordinate-cleanup strategy during feedback appear more plausible. However, because the trace contains no explicit natural-language causal statement linking the mutated sentence to the edit, the evidence supports `contributed` rather than `caused`.

---

## 7. OpenCode's Failure Path

### 7.1 Execution Trace

The key steps in OpenCode's execution were as follows.

#### Step 1: Explore the Relevant Functions

OpenCode read:

```text
xarray/core/dataarray.py
xarray/core/dataset.py
xarray/tests/test_dataset.py
```

and found:

```text
DataArray.to_unstacked_dataset
Dataset.to_stacked_array
```

It also read the mutated statement:

```text
This is the inverse operation of DataArray.to_stacked_array
```

along with the modified:

- examples;
- parameters;
- round-trip relationship;
- descriptions of the roles of `Dataset` and `DataArray`.

#### Step 2: Confirm the Actual Error

It understood that the error occurred at:

```python
return Dataset(data_dict)
```

and confirmed that merging multiple variables produced a coordinate conflict.

#### Step 3: Localize the Correct Responsible Function

OpenCode still ultimately modified:

```text
xarray/core/dataarray.py
DataArray.to_unstacked_dataset
```

Thus, it did not fail completely at the file or function-localization level.

#### Step 4: Implement the Wrong Local Semantics

It used a strategy similar to:

```python
self.sel({variable_dim: k}).squeeze(drop=True).drop_vars(
    dim,
    errors="ignore",
)
```

Other mutated runs contained variants such as:

```python
if dim in data.coords and dim not in data.dims:
    data = data.drop_vars(dim)
```

or conditional deletion based on:

```python
isnull().all().item()
```

#### Step 5: Lack of Decisive Test Feedback

The OpenCode trace primarily showed checks such as:

```text
compileall
py_compile
git diff --check
```

along with test commands or summarized test output.

However, it did not consistently include a complete and decisive pytest assertion demonstrating that:

```python
drop_vars
```

was equivalent to the gold fix across all stacked/unstacked round-trip scenarios.

The final official evaluation was:

```text
unresolved
```

---

## 8. Why Was OpenCode Wrong?

OpenCode's failure occurred through:

> **semantic broadening inside the correct function**

It did not move the bug to an unrelated file. Instead, within the correct function, it transformed the intended behavior:

> do not propagate the stacked coordinate during selection

into:

> select first, then delete a variable or coordinate afterward

The gold solution was:

```python
self.sel({variable_dim: k}, drop=True)
```

OpenCode's solution was:

```python
self.sel({variable_dim: k}).squeeze(drop=True).drop_vars(dim)
```

The two are not semantically equivalent.

The gold solution controls:

> whether the coordinate should enter the selected result in the first place

whereas the OpenCode solution controls:

> whether a coordinate that has already entered the result should be removed afterward

This changes both the timing of the operation and its applicable scope.

OpenCode's failure path can be represented as:

```text
read multiple mutated docstrings
        |
        v
integrate incorrect inverse, parameter, and object-role information
into one overall model
        |
        v
find the correct function
        |
        v
reinterpret a local coordinate-propagation problem
as a variable-deletion problem
        |
        v
use drop_vars
        |
        v
final editing failure
```

This illustrates a characteristic OpenCode failure pattern:

```text
correct localization
        +
long-context semantic integration
        +
local contract scope expansion
        =
incorrect editing
```

---

## 9. Why Did the Same Inconsistency Produce Different Errors?

This is the central value of the case:

- the same set of mutations;
- the same repository;
- the same issue;
- the same genuinely responsible function;

yet two different failure paths emerged.

### SWE-Agent

```text
local edit
  -> coordinate-conflict feedback
  -> reset_coords(drop=True)
  -> symptom-level patching during feedback
```

### OpenCode

```text
integrate multiple incorrect documents over a long context
  -> generalize coordinate propagation into drop_vars
  -> broaden semantics inside the correct function
```

The comparison is summarized below.

| Dimension | SWE-Agent | OpenCode |
|---|---|---|
| File localization | Correct | Correct |
| Function localization | Correct | Correct |
| Read the mutation? | Yes | Yes |
| Initial error | Local variable/coordinate deletion | Replaced selection semantics with post-selection deletion |
| Key feedback | Coordinate-conflict feedback | No consistently decisive pytest feedback |
| Final strategy | `reset_coords(drop=True)` | `drop_vars(dim)` |
| Main failure stage | Feedback | Editing |
| Typical pattern | Symptom-level patching | Local semantic scope expansion |
| Mutation causality | `contributed` | `contributed` |

---

## 10. Simplified Diagrams

A more detailed diagram is:

```text
                 same mutated docstring set
      +-------------------------------------------+
      | inverse relation, object responsibility, |
      | dim/level semantics, and examples         |
      +-------------------------------------------+
                         |
             +-----------+------------+
             |                        |
             v                        v
      SWE-Agent harness          OpenCode harness
   single action + fixed       todo list + long context
        observation
             |                        |
             v                        v
      make a local edit       integrate multiple doc relations
             |                        |
   MergeError / coordinate       no decisive pytest feedback
          feedback
             |                        |
             v                        v
  reset_coords(drop=True)          drop_vars(dim)
 broaden cleanup scope         broaden local semantics
   during feedback            inside correct function
             |                        |
             +-----------+------------+
                         |
                         v
                     unresolved
```

A more compact paper-oriented version is:

```text
same documentation inconsistency
              |
       +------+------+
       |             |
       v             v
   SWE-Agent      OpenCode
feedback-driven   long-context
                  integration
       |             |
       v             v
 reset_coords     drop_vars
       |             |
       v             v
Feedback failure  Editing failure
```

---

## 11. What Agent-Level Patterns Does This Case Reveal?

### 11.1 SWE-Agent: Feedback-Driven Under-Exploration and Symptom Patching

SWE-Agent's main problem was not a lack of tokens, but insufficient validation scope.

Its behavior can be characterized as:

```text
form a local hypothesis quickly
        |
        v
continue reasoning only around the current symptom
        |
        v
broaden local cleanup after test feedback
        |
        v
fail to re-check the full object relationship
```

More precise terms for this pattern are:

- **premature hypothesis fixation**
- **feedback-time symptom patching**

That is, the agent commits to a hypothesis too early and then patches the observed symptom during feedback without reopening the broader contract.

### 11.2 OpenCode: Local Semantic Expansion Under Long-Context Integration

OpenCode's main problem was not that it completely localized the wrong function. Rather, it:

```text
integrated multiple incorrect documentation statements into a coherent model
        |
        v
generalized a local constraint into a broader rule
        |
        v
made a semantically over-broad edit inside the correct function
```

A more precise term for this pattern is:

> **context-induced semantic scope expansion**

That is, integrating a long context caused the local semantic scope of the intended change to expand beyond the actual contract.
