# OpenCode: django__django-13925

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 5/7 locations.

## 1. Problem and expected correct approach

models.W042 is raised on inherited manually specified primary key.
Description
	
I have models which inherit from other models, and they should inherit the primary key. This works fine with Django 3.1. However, if I install Django 3.2 alpha, when I run make_migrations I get the following error messages:
System check identified some issues:
WARNINGS:
accounts.ReservedUsername: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the SpeedyCoreAccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
accounts.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the SpeedyCoreAccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
blocks.Block: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
contact_by_form.Feedback: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the SpeedyCoreContactByFormConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
core_messages.ReadMark: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the SpeedyCoreMessagesConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
friendship.Block: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
friendship.Follow: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
friendship.Friend: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
friendship.FriendshipRequest: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
likes.UserLike: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
uploads.Image: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
		HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
These models should not use auto-created primary keys! I already defined the primary key in the ancestor of the model. For example class Entity which class User inherits from. It looks to me like a bug in Django 3.2 alpha.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `django/db/models/base.py`, `tests/check_framework/test_model_checks.py`
- Clean run 2: `django/db/models/base.py`, `tests/check_framework/test_model_checks.py`
- Clean run 3: `django/db/models/base.py`, `tests/check_framework/test_model_checks.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `django/db/models/query.py` / `django/db/models/query.py::QuerySet.bulk_create`
  - Clean doc: Insert each of the instances into the database.
  - Mutated doc: Insert each of the instances into the database with bulk_update().
  - Contract change: The documented API name changes from bulk_create() to bulk_update().
- `django/db/models/base.py` / `django/db/models/base.py::Model.save`
  - Clean doc: The 'force_insert' and 'force_update' parameters can be used to insist
        that the "save" must be an SQL insert or update (or equivalent for
        non-SQL backends), respectively.
  - Mutated doc: The 'force_insert' and 'force_update' parameters can be used to insist
        that the "save" must be an SQL update or insert (or equivalent for
        non-SQL backends), respectively.
  - Contract change: The documented effects of force_insert and force_update are reversed: force_insert is said to require an update, while force_update is said to require an insert.
- `django/db/models/base.py` / `django/db/models/base.py::Model.save`
  - Clean doc: Normally, they should not be set.
  - Mutated doc: Normally, they should be set.
  - Contract change: Forced save mode is documented as normally enabled.
- `django/db/models/base.py` / `django/db/models/base.py::Model._save_table`
  - Clean doc: Do the heavy-lifting involved in saving.
  - Mutated doc: Avoids mutating model state involved in saving.
  - Contract change: The save implementation is documented as avoiding model-state mutation.
- `django/db/models/base.py` / `django/db/models/base.py::Model._check_fields`
  - Clean doc: Perform all field checks.
  - Mutated doc: Perform checks for local fields only.
  - Contract change: Field checking is documented as limited to local fields and excluding local many-to-many fields.
- `django/db/models/options.py` / `django/db/models/options.py::Options.can_migrate`
  - Clean doc: Return True if the model can/should be migrated on the `connection`.
  - Mutated doc: Return True if the model can/should be migrated on the `database`.
  - Contract change: The documented parameter name changes from `connection` to `database`.
- `django/db/models/options.py` / `django/db/models/options.py::Options.can_migrate`
  - Clean doc: `connection` can be either a real connection or a connection alias.
  - Mutated doc: `connection` must be a real connection.
  - Contract change: The documented connection parameter type changes from accepting either a real connection or an alias to accepting only a real connection.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the model check path and the existing tests around default primary keys first, then I’ll patch the warning logic where inherited primary keys are treated as missing.
- I’ve got the file map. Next I’m tracing the warning from model checks back to the exact condition that decides whether a primary key is considered auto-created or inherited.
- I found the warning gate: it only looks at `cls._meta.pk.auto_created`. For inherited concrete PKs that can be true even when the field was explicitly declared on an ancestor, so I’m looking for the right metadata signal to distinguish “really implicit” from “inherited explicit.”
- I have the fix shape now: the warning should only fire for models that actually define their own implicit PK, not for proxies or multi-table descendants. I’m adding a regression test for a child model inheriting an explicit parent PK, then I’ll run the targeted check test file.
- I’m editing two spots: the check itself in `django/db/models/base.py`, and one regression test in `tests/check_framework/test_model_checks.py` that exercises a child model inheriting an explicit primary key.
- The code change is in place. I’m running the check-framework model-check tests, which should cover both the new regression and the existing default-PK cases without needing a full suite run.
- The test runner couldn’t import the local checkout as `django`, so I’m rerunning with `PYTHONPATH` pointed at the workspace root.
- I hit an environment gap rather than a code failure: the checkout is missing `asgiref`, which the Django package imports before tests even start. I’m trying a minimal dependency install so I can still run the targeted test file here.
- `asgiref` was the first missing dependency. The next import failure is `pytz`, so I’m filling that in and retrying the same narrow test command.
- The test run is now far enough to load the suite; it’s failing on `sqlparse`, which is another standard Django dependency. I’m adding that last missing package and rerunning the same target.
- The targeted check-model suite passed after the patch. I’m doing a quick diff/status pass to make sure only the intended files changed and to summarize the exact behavior shift.
- Fixed in `django/db/models/base.py`: `models.W042` now only fires for models that actually define their own implicit primary key, and skips proxies plus multi-table descendants that inherit their PK from an ancestor.  I also added a regression test in `tests/check_framework/test_model_checks.py` covering a child model inheriting an explicit `BigAutoField` PK from its parent.  Verified with: `PYTHONPATH=/testbed python tests/runtests.py check_framework.test_model_checks`  That file passed cleanly.

### Clean run 2
- I’m tracing the model-check path that emits `models.W042` and then I’ll tighten the condition so inherited concrete primary keys don’t get treated as auto-created. After that I’ll run the focused model-check tests around primary key warnings.
- I found the warning gate: `_check_default_pk()` only looks at `cls._meta.pk.auto_created`. The bug is likely that inherited primary keys still report `auto_created=True` even when the field itself was explicitly declared on an ancestor, so I’m following the field inheritance path next to see where that flag is set.
- I’ve narrowed it to model inheritance, and the distinction matters: abstract inheritance copies a real field, while multi-table inheritance synthesizes a parent link field. I’m checking whether the warning should key off “auto-created and no concrete inherited PK exists” rather than the raw `pk.auto_created` flag.
- The current warning is too blunt if it treats every auto-created `_meta.pk` the same. I’m checking whether MTI and proxy models can be distinguished cheaply from `Options`, because that lets us keep the fix tiny and avoid touching unrelated primary-key behavior.
- I have the shape of the fix now: keep `models.W042` for genuinely auto-created primary keys, but suppress it when the pk is a proxy’s inherited field or an MTI parent-link field. I’m patching the check and adding a regression test for a child model that inherits an explicit primary key from its parent.
- The code change is in place. I’m running the narrow check-framework test class first so we can confirm the warning is gone without waiting on the full suite.
- The test runner was being executed from `tests/`, so Python wasn’t seeing the repo root as importable. I’m rerunning with `PYTHONPATH=/testbed` so it imports the local Django tree instead of looking for an installed package.
- The full Django test runner can’t start in this workspace because the runtime dependency `asgiref` isn’t installed. I’m doing a syntax-level verification on the touched files instead, which at least confirms the patch is structurally clean.
- The condition is subtle enough that it benefits from one short comment. I’m adding a note that the warning is meant for model-generated primary keys, not parent-link keys created by inheritance.
- Fixed `models.W042` so it no longer fires for inherited primary keys created by inheritance machinery. The check now skips auto-created parent-link PKs and proxy models, while still warning on genuinely auto-created PKs. See [django/db/models/base.py:1299](/testbed/django/db/models/base.py:1299).  I also added a regression test for a child model that inherits an explicit primary key from its parent in [tests/check_framework/test_model_checks.py:405](/testbed/tests/check_framework/test_model_checks.py:405).  Verification: `python -m py_compile django/db/models/base.py tests/check_framework/test_model_checks.py` passed. I couldn’t run the Django test runner in this workspace because `asgiref` isn’t installed.

### Clean run 3
- I’m checking the model check path and the existing tests around `models.W042` first, then I’ll patch the smallest place that decides whether a model already has an explicit primary key.
- I found the warning in `django/db/models/base.py`. Next I’m comparing that logic with the model-option code and the existing `W042` tests to see whether the bug is in the check itself or in how inherited primary keys are detected.
- The warning gate is currently just `cls._meta.pk.auto_created`. That’s too coarse if the primary key is inherited from a parent model. I’m tracing how `Options.pk` gets set during model preparation to see what extra condition can distinguish a true auto-created field from an inherited one.
- I’ve confirmed the warning is emitted from the model class check, not migrations. I’m now checking whether later Django code already fixed this in a narrower way, because that gives us the right minimal patch and a matching regression test.
- I need one concrete reproduction point now: whether the inherited primary key is actually flagged `auto_created` on the child, or whether the check is seeing the wrong model state. I’m probing that with a tiny runtime example before I patch anything.
- The model formset tests already encode the key distinction: multi-table inheritance can produce an auto-created primary key that is not an `AutoField`. That points to a very small fix in the warning predicate rather than anything broader in model construction.
- I have the patch shape now: narrow the warning to auto-created fields that are actually `AutoField` subclasses, and add a regression test with a multi-table child inheriting a concrete parent primary key. I’m applying both together.
- I’ve made the code change. I’m running the narrowest relevant test next; if the environment is missing Django’s runtime deps, I’ll report that explicitly rather than pretending the verification happened.
- The syntax check passed. I’m doing one more pass over import order, because `base.py` sits in a sensitive part of Django’s import graph and I want to avoid introducing a circular import with the new `AutoField` reference.
- The targeted test runner can see the local Django tree now, but it still stops on the missing `asgiref` dependency before executing the case. I’m doing a final diff review for the two-file change and then I’ll hand back the result with that verification note.
- Fixed in the working tree.  I narrowed `models.W042` in [`django/db/models/base.py`](#/testbed/django/db/models/base.py:1299) so it only fires for auto-created primary keys that are actually `AutoField` subclasses. That excludes the auto-created `OneToOneField` primary key Django generates for multi-table inheritance, which was the false positive here.  I added a regression test in [`tests/check_framework/test_model_checks.py`](#/testbed/tests/check_framework/test_model_checks.py:408) covering a child model inheriting a concrete parent primary key.  Verification: - `python -m py_compile django/db/models/base.py tests/check_framework/test_model_checks.py` - `PYTHONPATH=/testbed python tests/runtests.py check_framework.test_model_checks.ModelDefaultAutoFieldTests.test_inherited_pk --verbosity 2` could not run here because the environment is missing `asgiref`.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 5/7. Hit lines: [70], [70], [15, 70], [24], [24].
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (23.33 clean-mean rounds to 20). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 12, 10, 11 extracted reasoning messages across runs 1--3; the mutant emitted 8. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking how Django decides whether a model has an explicit primary key, then I’ll patch the check and run the targeted tests around model field inheritance and system checks.
- I found the warning path. Next I’m tracing how `_meta.pk` is assigned for multi-table inheritance so the check can distinguish “auto-created because nothing was defined” from “inherited explicit primary key.”
- The bug is likely in the warning condition, not in model construction: inherited parent-link primary keys can still end up with `_meta.pk.auto_created == True` in some inheritance shapes. I’m checking existing inheritance tests to mirror the intended behavior rather than patching by guess.
- I’ve got the shape of the fix: make the warning depend on whether the inherited primary-key chain contains any explicit PK, not just whether the current model’s PK was auto-created. I’m patching the system check and adding a regression test for a child of a concrete parent with an explicit primary key.
- The code change is in. I’m running the narrowest test slice that exercises `models.W042` and the new inheritance case, then I’ll widen only if that misses the regression.
- Test execution is blocked by missing runtime deps in this workspace (`asgiref` isn’t installed), so I’m at least compiling the touched files to catch syntax issues and then I’ll summarize the remaining verification gap plainly.
- I found unrelated edits already sitting in the worktree; I’m leaving those alone. I’m only tightening the new check line for readability and to keep the patch as narrow as possible.
- Fixed in `django/db/models/base.py` and added a regression in `tests/check_framework/test_model_checks.py`.  The warning now only fires when the auto-created PK chain has no explicit primary key anywhere in the model ancestry, so inherited manual PKs no longer trigger `models.W042`.  Verification: - `python -m py_compile django/db/models/base.py tests/check_framework/test_model_checks.py` passed - Full Django test run wasn’t possible here because the workspace is missing runtime deps (`asgiref`), so I couldn’t execute `tests.runtests.py` end to end

## 4. Patch and cost delta

- Clean mean tokens: 1,102,732; mutant tokens: 691,183; delta: -37.32%.
- Clean mean rounds: 23.33; mutant rounds: 20; delta: -14.29%.
- Final mutant patch files: `django/db/models/base.py`, `django/db/models/options.py`, `django/db/models/query.py`, `tests/check_framework/test_model_checks.py`.
- Files added beyond every clean patch: `django/db/models/options.py`, `django/db/models/query.py`.
- Clean-patch files omitted by mutant: none.
- Trace patch paths: django/db/models/base.py, django/db/models/options.py, django/db/models/query.py, tests/check_framework/test_model_checks.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

The mutation was observed before a patch that changed the clean localization/edit footprint. The extra and omitted files above identify the concrete structural divergence; subsequent testing did not restore the clean solution. This is positive evidence of mutation influence, although a single run cannot establish deterministic causality.

- Earliest evidence classification: **Testing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
