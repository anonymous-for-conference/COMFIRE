# Codex: django__django-12470

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 6/6 locations.

## 1. Problem and expected correct approach

Inherited model doesn't correctly order by "-pk" when specified on Parent.Meta.ordering
Description
	
Given the following model definition:
from django.db import models
class Parent(models.Model):
	class Meta:
		ordering = ["-pk"]
class Child(Parent):
	pass
Querying the Child class results in the following:
>>> print(Child.objects.all().query)
SELECT "myapp_parent"."id", "myapp_child"."parent_ptr_id" FROM "myapp_child" INNER JOIN "myapp_parent" ON ("myapp_child"."parent_ptr_id" = "myapp_parent"."id") ORDER BY "myapp_parent"."id" ASC
The query is ordered ASC but I expect the order to be DESC.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `django/db/models/sql/compiler.py`, `tests/ordering/models.py`, `tests/ordering/tests.py`
- Clean run 2: `django/db/models/sql/compiler.py`, `tests/model_inheritance/tests.py`
- Clean run 3: `django/db/models/sql/compiler.py`, `tests/model_inheritance_regress/models.py`, `tests/model_inheritance_regress/tests.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler.find_ordering_name`
  - Clean doc: The 'name' is of the form 'field1__field2__...__fieldN'.
  - Mutated doc: The 'field_name' is of the form 'field1__field2__...__fieldN'.
  - Contract change: The documented parameter name changes from `name` to `field_name`.
- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler.find_ordering_name`
  - Clean doc: Return the table alias (the name might be ambiguous, the alias will
        not be) and column name for ordering by the given 'name' parameter.
  - Mutated doc: Return the original ordering name unchanged for the given 'name'
        parameter.
  - Contract change: The documented outcome changes from returning the unambiguous table alias and column name to returning the original ordering name unchanged.
- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler.get_related_selections`
  - Clean doc: Fill in the information needed for a select_related query.
  - Mutated doc: Fill in the information needed for a prefetch_related query.
  - Contract change: The documented query API changes from select_related to prefetch_related.
- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler._setup_joins`
  - Clean doc: get_ordering() and get_distinct() must produce same target columns on
        same input, as the prefixes of get_ordering() and get_distinct() must
        match.
  - Mutated doc: get_ordering() and get_values() must produce same target columns on
        same input, as the prefixes of get_ordering() and get_values() must
        match.
  - Contract change: The documented API name changes from get_distinct() to get_values().
- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler._setup_joins`
  - Clean doc: Executing SQL where this is not true is an error.
  - Mutated doc: Compiling SQL where this is not true is an error.
  - Contract change: The documented SQL operation changes from execution to compilation.
- `tests/model_inheritance_regress/tests.py` / `tests/model_inheritance_regress/tests.py::ModelInheritanceTest.test_get_next_previous_by_date`
  - Clean doc: Regression tests for #8076
        get_(next/previous)_by_date should work
  - Mutated doc: Regression tests for #8076
        get_(next/previous)_by_pub_date should work
  - Contract change: The documented API name changes from get_(next/previous)_by_date to get_(next/previous)_by_pub_date.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m tracing the model ordering path first, then I’ll patch the smallest spot that turns inherited `-pk` into ascending order and run the relevant ORM tests.
- `rg` isn’t available here, so I’m switching to plain `grep`/`find` to locate the ordering code and any existing regression coverage before editing.
- I’ve narrowed this to ORM ordering resolution, not admin or forms. Next I’m reading the ordering compiler and the existing inheritance-ordering tests side by side so I can patch the conversion path instead of papering over the symptom.
- I found a likely hotspot in `django/db/models/sql/compiler.py` where `pk` is resolved to the concrete primary key field and may be losing the leading `-` during inherited ordering expansion. I’m opening that logic plus the existing pk-ordering tests now.
- The likely failure mode is `find_ordering_name()` recursing into inherited ordering with `default_order='DESC'`, then `get_order_dir('-pk', default='DESC')` may normalize the explicit minus away. I’m verifying that helper now before changing anything.
- I’ve confirmed the failure is in recursive default-order propagation, not the SQL renderer. I’m checking whether Django already special-cases `pk` in any related-ordering path so I can align the fix with existing behavior instead of inventing a one-off.
- I found an existing ordering app with a `-pk` model, which is a better place for a regression test than inventing a new test app. I’m reading that model/test module and then I’ll patch the compiler or ordering resolution in the smallest way that preserves current nested-order semantics.
- I want one more look at join resolution for `pk`, because this bug only appears on multi-table inheritance and not on ordinary related fields. That will tell me whether to fix the compiler or the join-name resolution itself.
- I’ve got the fix shape now: keep related-model ordering expansion for normal relations, but stop it for the top-level `pk` alias on a multi-table inherited model. I’m patching the compiler and adding a regression test that proves `Child.objects.all()` comes back in descending pk order.
- The code change is in place. I’m running the narrow ordering test module first so I can confirm the regression and make sure I didn’t disturb other ordering paths.
- The regression test needs real tables for the ad hoc parent/child models. I’m updating it to create those tables explicitly inside the test so it exercises the ORM path instead of failing at schema setup.
- The test now creates its own tables, so I’m rerunning the focused ordering case and the whole ordering module to verify the fix is isolated and stable.
- The ad hoc schema creation doesn’t work under SQLite’s transactional `TestCase`, so I’m switching to a model that already lives in the `ordering` app and will be picked up by the test DB setup, which is the cleanest way to keep this regression test stable.
- The regression now uses a real model that the ordering app’s test database already creates. I’m rerunning the focused case and the full ordering suite to confirm the behavior and catch any unintended side effects.
- The targeted regression passes and the full `ordering` module passes. I’m doing one final diff check now to make sure the change stayed minimal and the new test/model wiring is clean.
- I’ve confirmed the diff is limited to the ordering compiler plus one regression model/test. I’m grabbing exact line numbers so I can point you at the changed spots cleanly in the handoff.
- Implemented the fix and left a regression test in place.  What changed: - In [`/testbed/django/db/models/sql/compiler.py:714`](file:///testbed/django/db/models/sql/compiler.py#L714), `find_ordering_name()` now treats a top-level `pk` ordering on a relational primary key as a direct pk sort instead of recursing into the related model’s default ordering. That preserves `-pk` as descending on inherited models. - In [`/testbed/tests/ordering/models.py:26`](file:///testbed/tests/ordering/models.py#L26), I added `ChildAuthor`, a concrete multi-table child of `Author`, so the regression test uses a real model table already created by the test DB setup. - In [`/testbed/tests/ordering/tests.py:484`](file:///testbed/tests/ordering/tests.py#L484), I added a regression test proving `ChildAuthor.objects.all()` orders `[newer, older]` when the parent model’s `Meta.ordering = ['-pk']`.  Verification: - `python tests/runtests.py ordering.tests.OrderingTests.test_inherited_default_ordering_by_negative_pk` - `python tests/runtests.py ordering`  Both passed.

### Clean run 2
- I’m checking the model ordering code path and the existing regression tests first, then I’ll patch the smallest spot that handles inherited `Meta.ordering` for `-pk` and verify with a focused test run.
- `rg` isn’t available here, so I’m falling back to `find` and `grep` to locate the ordering logic and any existing multi-table inheritance coverage.
- I found the inheritance test area. Next I’m reading the model inheritance test file and the ordering resolution code around `pk` to see whether the bug is in normalization or in how inherited ordering is copied.
- I’ve narrowed it to model class construction. The next pass is the inheritance setup in `ModelBase` where parent `Meta.ordering` gets propagated to child classes.
- I’ve confirmed the child class inherits the parent’s `ordering` tuple directly. Now I’m tracing how `pk` is resolved when the ORM builds the actual `ORDER BY` so I can tell whether the sign is being dropped there.
- I haven’t found a query-building bug yet, so I’m checking the inheritance test models and the `Meta.ordering` shape on the parent/child classes to reproduce the exact state the ORM sees.
- There’s already a general ordering test module, so I’m checking whether this case is just missing coverage there instead of needing a broader ORM change.
- I have enough code context to reproduce this directly. I’m running a tiny Django snippet against the existing test models to see whether the failure is in `_meta.ordering` or in SQL compilation for `Child.objects.all()`.
- `tests.settings` isn’t the settings module in this checkout. I’m locating the actual test settings file, then I’ll rerun the reproduction with the right `DJANGO_SETTINGS_MODULE`.
- The repo’s test harness is custom, so I’m checking the top-level test settings conventions before I pick the fastest verification path. That should let me reproduce this without guessing at the setup.
- I don’t need the full suite to reproduce this. I’m going to spin up a tiny isolated Django config in a one-off script, define just the parent/child models, and inspect the generated SQL and `_meta` state.
- The first isolated run failed because I gave `isolate_apps` a nonexistent app label. I’m rerunning it against the real `tests` package so I can inspect the actual model metadata and query string.
- I’ve got the right shape now: the ad hoc models need an explicit `app_label` in this standalone script. I’m rerunning with that so the query compiler can be inspected cleanly.
- I’ve got the likely fix. Before editing, I’m checking what the compiler API returns for this query so the regression test can assert the semantic direction instead of a brittle SQL string.
- I’ve confirmed the compiler is currently producing `descending=False` for this case. I’m patching the `pk` resolution path in `SQLCompiler` and adding a regression test that checks the compiled ordering direction directly.
- The patch is in place. I’m running the smallest useful test target now: the new regression plus the surrounding inheritance tests so we can catch any fallout immediately.
- The new regression passes. I’m doing one direct reproduction against the patched compiler to confirm the generated ordering flips to descending, not just the test helper’s boolean.
- The direct compiler check now shows `DESC` on the child primary key, which is the intended behavior. I’m running the full `model_inheritance` test module once to make sure the change didn’t perturb other inheritance behavior.
- The fix is done and the full inheritance module is green. I’m grabbing the exact line numbers for the patch and regression test so I can point you to the changes cleanly.
- Fixed in `SQLCompiler.find_ordering_name()` so inherited `Meta.ordering = ['-pk']` no longer gets treated like a related-model default ordering when the child’s primary key is a parent link.  Changed: - [/testbed/django/db/models/sql/compiler.py:699](/testbed/django/db/models/sql/compiler.py#L699) - [/testbed/tests/model_inheritance/tests.py:207](/testbed/tests/model_inheritance/tests.py#L207)  What changed: - Added a `name != 'pk'` guard before recursing into related ordering expansion. - Added a regression test that defines a parent with `ordering = ['-pk']` and asserts the compiled child queryset orders descending.  Verification: - `python tests/runtests.py model_inheritance.tests.ModelInheritanceTests.test_inherited_ordering_by_negative_pk` - `python tests/runtests.py model_inheritance`  Both passed.

### Clean run 3
- I’m inspecting the ORM ordering path in the local Django checkout, then I’ll patch the smallest place that drops the `-pk` direction and run the targeted regression test.
- `rg` isn’t installed here, so I’m falling back to `grep`/`find` to locate the ordering code and any existing regression coverage around inherited model `Meta.ordering`.
- I found the likely area: ordering resolution in model inheritance, not the admin. Next I’m reading the inheritance regression models/tests and the `Options` ordering logic to see where `-pk` gets normalized away.
- I’ve narrowed it to the compiler path that expands ordering fields. I’m reading the `pk` special-case handling now, because that’s where inherited `-pk` can accidentally lose its sign.
- I’ve confirmed the parent `ordering` is inherited onto the child. The bug is more likely in how the compiler expands `pk` through the inherited parent link, so I’m tracing `get_order_dir` and the join/`OrderBy` handling next.
- There’s already coverage for `Meta.ordering = ('-pk',)` on a plain model, so I’m comparing that behavior with inherited models to isolate the multi-table inheritance gap instead of changing generic `pk` handling.
- The actual failure is a double application of `-pk` during relation-order expansion. I’m checking whether this test app already has a safe parent/child pair I can reuse, or whether I should add a minimal dedicated model for the regression.
- I have the fix shape: `pk` should behave like a concrete primary key alias here, not like a relation that inherits the parent model’s own ordering. I’m validating the exact field object returned for `Child.pk` before patching so I only change the minimal branch.
- I’m patching two spots now: - the compiler, to stop `pk` from recursing into parent-model default ordering when it is the inherited primary-key alias; - a regression test on the inherited model pair, so this doesn’t come back.
- I’m adding the regression in the existing model inheritance test app by reusing `Parent`/`Child`. That keeps the fix focused and verifies the child queryset itself now comes back in descending pk order.
- The code and regression test are in place. I’m running the narrow inheritance regression module first; if that passes, I’ll do one extra ordering-specific check to make sure the `-pk` SQL direction is now preserved.
- `tox.ini` shows the test entrypoint is `tests/runtests.py`. I’m running the inheritance regression app plus a focused ordering test under the same runner so we verify the actual ORM behavior, not just the new assertion.
- Both test runs are still active. I’m polling for the first failures or a clean pass so I can confirm whether the compiler change is sufficient or needs a narrower adjustment.
- The focused regression passed, and the broader ordering suite stayed green. I’m doing a final diff pass to make sure the change stayed minimal and there aren’t any accidental edits left behind.
- I’ve confirmed the diff is limited to the compiler branch and the regression fixture/test. I’m grabbing exact line numbers for the final handoff so you can jump straight to the changed code.
- Fixed the inherited `-pk` ordering regression.  What changed: - In [`django/db/models/sql/compiler.py`](sandbox:/testbed/django/db/models/sql/compiler.py#L711), `find_ordering_name()` no longer treats `pk` as a relation for ordering expansion. That prevents a multi-table inherited child from reapplying the parent model’s `Meta.ordering` and flipping `-pk` to ASC. - Added a regression case in [`tests/model_inheritance_regress/models.py`](sandbox:/testbed/tests/model_inheritance_regress/models.py#L75) by setting `Parent.Meta.ordering = ('-pk',)`. - Added a regression test in [`tests/model_inheritance_regress/tests.py`](sandbox:/testbed/tests/model_inheritance_regress/tests.py#L139) asserting `Child.objects.all()` comes back in descending pk order.  Validation: - `python runtests.py model_inheritance_regress --verbosity 2` - `python runtests.py ordering --verbosity 2`  Both passed.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 6/6. Hit lines: [21, 24, 67, 108, 123], [24], [21, 67, 108], [24], [21, 24, 67, 108], [19].
- Relative to the three clean runs, the mutant trajectory **expanded** in interaction length (17.67 clean-mean rounds to 19). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 17, 20, 16 extracted reasoning messages across runs 1--3; the mutant emitted 19. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’ll inspect the model inheritance and ordering resolution paths, then locate the existing regression coverage and implement the narrowest fix. I’ll run the relevant ORM tests, plus any targeted test file or check needed to confirm the generated SQL ordering.
- The worktree already contains edits in the exact compiler and regression-test files, so I’m treating them as user or prior-agent changes and will inspect them before modifying anything. `rg` is unavailable in this environment; I’ll use `grep` and targeted file reads instead, and I’ll avoid disturbing unrelated state.
- <thinking>**Tracing the direction loss**</thinking> The issue is in `SQLCompiler.find_ordering_name()`: a default `Meta.ordering` entry is recursively expanded when ordering through a parent link, and the outer `-` direction is passed as the recursive default. I’m checking the exact `get_order_dir()` and join metadata behavior now, because the correct fix must preserve explicit signs while applying the requested direction only where Django intends it.
- <thinking>**Pinpointing parent-link handling**
- <thinking>**Confirming current failure and regression placement**</thinking> The direction loss is confirmed by `get_order_dir()`: when the compiler recursively resolves the inherited parent ordering, the explicit `-` is interpreted relative to the passed default and becomes ascending. I’ll add a focused regression using the existing inheritance models, then adjust only the recursive call so an explicit sign remains authoritative while an unsigned inherited ordering can still inherit the outer direction.
- <thinking>**Implementing narrow recursive ordering fix**</thinking> I’m going to preserve the current relation-ordering behavior for explicit related lookups, while preventing the parent-link field from inverting an already explicit `Meta.ordering` entry. The regression will assert both SQL direction and returned primary-key order for a two-row `Parent`/`Child` queryset.
- <thinking>**Implementing parent-link exception**</thinking>The first test attempt exposed a test-only mistake: `Parent` was not imported, and standalone parents cannot appear in a `Child` queryset. The implementation path is now clear: skip related-model default-ordering expansion for multi-table parent links, allowing the resolved `-pk` expression to retain `DESC`; I’m correcting the regression to create two children and verify their order.
- <thinking>**Verifying parent-link ordering regression**
- <thinking>**Correcting regression assertion to match generated SQL****Validating the compiler output**
- <thinking>**Running focused regression and neighboring inheritance tests****Verifying final test behavior and diff**
- <thinking>**Checking broader regression impact**
- <thinking>**Investigating neighboring ordering regression failure****Comparing expected parent-link ordering semantics**
- <thinking>**Narrowing the fix after broader test failure****Comparing explicit relation ordering semantics**</thinking> The neighboring ordering test shows that skipping all parent-link expansion is too broad: explicit `order_by('article_ptr')` must still expand the related model’s default ordering. I’m narrowing the change to the recursive default direction itself, then I’ll rerun both the new inheritance regression and the existing expression-ordering case before deciding whether an even more specific guard is needed.
- <thinking>**Confirming correct SQL direction after recursion fix****Updating test expectation to parent-table primary key**</thinking> The narrowed fix now produces the expected `ORDER BY ...parent.id DESC`, and the existing pointer-ordering test passes. The regression assertion was still expecting the child pointer column from the earlier implementation attempt; I’m updating it to the actual backend-neutral SQL shape generated by this ORM version, then running the full affected apps.
- <thinking>**Reviewing final patch and checking full inheritance coverage****Running complete model inheritance regression suite**
- <thinking>**Cleaning regression test scope****Finalizing narrow fix and regression coverage**
- <thinking>**Running final focused verification****Reviewing final working tree state**
- <thinking>**Finalizing solution and verification****Marking task complete**</thinking> The affected inheritance and ordering suites now pass, including the existing expression-based parent-pointer ordering case. The final change is limited to preserving the original default direction during recursive ordering expansion, with a regression model/test demonstrating descending inherited `pk` order; preexisting unrelated docstring/comment edits remain untouched.
- Implemented the inherited `Meta.ordering = ('-pk',)` fix.  Changes: - Preserved the original default ordering direction during recursive relation ordering resolution in [compiler.py](/testbed/django/db/models/sql/compiler.py:729). - Added descending primary-key ordering to the inheritance regression model. - Added a regression test confirming `Child.objects.all()` returns children in descending PK order in [tests.py](/testbed/tests/model_inheritance_regress/tests.py:139).  Verification: - `model_inheritance_regress` and `ordering` suites: **57 tests passed**, 1 expected failure. - `git diff --check`: clean.

## 4. Patch and cost delta

- Clean mean tokens: 1,633,831; mutant tokens: 1,145,519; delta: -29.89%.
- Clean mean rounds: 17.67; mutant rounds: 19; delta: +7.55%.
- Final mutant patch files: `django/db/models/sql/compiler.py`, `tests/model_inheritance_regress/models.py`, `tests/model_inheritance_regress/tests.py`.
- Files added beyond every clean patch: none.
- Clean-patch files omitted by mutant: `tests/model_inheritance/tests.py`, `tests/ordering/models.py`, `tests/ordering/tests.py`.
- Trace patch paths: django/db/models/sql/compiler.py, tests/model_inheritance_regress/models.py, tests/model_inheritance_regress/tests.py.

## 5. Inconsistency awareness and causal mechanism

The trajectory explicitly mentions documentation/docstrings or a contradiction. These are the relevant awareness statements:
- <thinking>**Finalizing solution and verification****Marking task complete**</thinking> The affected inheritance and ordering suites now pass, including the existing expression-based parent-pointer ordering case. The final change is limited to preserving the original default direction during recursive ordering expansion, with a regression model/test demonstrating descending inherited `pk` order; preexisting unrelated docstring/comment edits remain untouched.

The mutation was observed before a patch that changed the clean localization/edit footprint. The extra and omitted files above identify the concrete structural divergence; subsequent testing did not restore the clean solution. This is positive evidence of mutation influence, although a single run cannot establish deterministic causality.

- Earliest evidence classification: **Testing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
