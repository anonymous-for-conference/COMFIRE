# OpenCode: django__django-11039

**Causal status:** `excluded: mutation text not observed`. Official evaluation is unresolved. Mutation text hit 0/5 locations.

## 1. Problem and expected correct approach

sqlmigrate wraps it's outpout in BEGIN/COMMIT even if the database doesn't support transactional DDL
Description
	 
		(last modified by Simon Charette)
	 
The migration executor only adds the outer BEGIN/COMMIT ​if the migration is atomic and ​the schema editor can rollback DDL but the current sqlmigrate logic only takes migration.atomic into consideration.
The issue can be addressed by
Changing sqlmigrate ​assignment of self.output_transaction to consider connection.features.can_rollback_ddl as well.
Adding a test in tests/migrations/test_commands.py based on ​an existing test for non-atomic migrations that mocks connection.features.can_rollback_ddl to False instead of overdidding MIGRATION_MODULES to point to a non-atomic migration.
I marked the ticket as easy picking because I included the above guidelines but feel free to uncheck it if you deem it inappropriate.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `django/core/management/commands/sqlmigrate.py`, `tests/migrations/test_commands.py`
- Clean run 2: `django/core/management/commands/sqlmigrate.py`, `tests/migrations/test_commands.py`
- Clean run 3: `django/core/management/commands/sqlmigrate.py`, `tests/migrations/test_commands.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `tests/migrations/test_commands.py` / `tests/migrations/test_commands.py::MigrateTests.test_migrate_conflict_exit`
  - Clean doc: migrate exits if it detects a conflict.
  - Mutated doc: migrate continues if it detects a conflict.
  - Contract change: Migration conflict handling is documented as continuing rather than exiting.
- `tests/migrations/test_commands.py` / `tests/migrations/test_commands.py::MigrateTests.test_migrate_fake_initial`
  - Clean doc: --fake-initial only works if all tables created in the initial
        migration of an app exists.
  - Mutated doc: --fake-initial only works if at least one table created in the initial
        migration of an app exists.
  - Contract change: The documented requirement changes from all initial-migration tables existing to at least one existing.
- `django/core/management/base.py` / `django/core/management/base.py::BaseCommand.execute`
  - Clean doc: Try to execute this command, performing system checks if needed (as
        controlled by the ``requires_system_checks`` attribute, except if
        force-skipped).
  - Mutated doc: Try to execute this command, performing system checks if needed (as
        controlled by the ``requires_system_checks`` attribute, after the
        command handler runs unless force-skipped).
  - Contract change: System checks are documented as running after the command handler executes.
- `tests/migrations/test_commands.py` / `tests/migrations/test_commands.py::MigrateTests.test_migrate_fake_split_initial`
  - Clean doc: Split initial migrations can be faked with --fake-initial.
  - Mutated doc: Split initial migrations cannot be faked with --fake-initial.
  - Contract change: Split initial migrations are documented as not being fakeable with --fake-initial.
- `tests/migrations/test_commands.py` / `tests/migrations/test_commands.py::MigrateTests.test_showmigrations_list`
  - Clean doc: showmigrations --list  displays migrations and whether or not they're
        applied.
  - Mutated doc: showmigrations --list  displays migrations and their
        dependencies.
  - Contract change: The documented output changes from each migration's applied status to its dependencies.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the command implementation and the existing migration command tests first, then I’ll patch the narrowest path that decides whether `sqlmigrate` emits transaction wrappers.
- The command already has a single assignment to `output_transaction`; I’m reading that and the neighboring test cases so the fix stays aligned with the current test style instead of adding new scaffolding.
- I’ve confirmed the bug source: `sqlmigrate` only looks at `migration.atomic`. Next I’m locating the existing transaction-wrapping tests so I can mirror the nearest one and keep the assertion shape stable.
- I have the exact code path now. I’m making one line of logic stricter in `sqlmigrate`, then I’ll add a focused regression test that keeps the migration atomic but simulates a backend that cannot roll back DDL.
- The regression test is in place. I’m running only the `sqlmigrate` cases from the migrations command suite so we verify the behavior without dragging in the full test matrix.
- The first test run missed the in-tree `django` package on `PYTHONPATH`. I’m rerunning with the repository root injected so the command exercises the local code I just changed.
- The environment is missing test dependencies (`pytz`), so the Django test runner can’t start here. I’m still doing a syntax-level check on the touched files to catch any edit mistakes before I wrap up.
- The edit is syntactically clean. I’m checking the final diff now so I can report the exact files and keep the summary tight.
- `sqlmigrate` now only wraps output in `BEGIN`/`COMMIT` when the migration is atomic *and* the backend can roll back DDL. I changed that in [django/core/management/commands/sqlmigrate.py]( /testbed/django/core/management/commands/sqlmigrate.py ) and added a regression test in [tests/migrations/test_commands.py]( /testbed/tests/migrations/test_commands.py ) that keeps the migration atomic but patches `connection.features.can_rollback_ddl = False`.  Verification: `python -m py_compile django/core/management/commands/sqlmigrate.py tests/migrations/test_commands.py` passed. I couldn’t run the Django test cases here because the environment is missing `pytz`, so the test runner fails during import.

### Clean run 2
- I’m checking the command path and the existing migration command tests first, then I’ll patch the transaction gating and verify with a targeted test run.
- I found the command and the existing test file. Next I’m reading the command implementation and the migration command tests together so I can keep the fix aligned with the current test style.
- The command is exactly where the report said it was: it only looks at `migration.atomic`. I’m locating the closest existing `sqlmigrate` assertions so the new test can mirror the current coverage rather than inventing a new pattern.
- I’ve got the minimal change: gate `sqlmigrate`’s outer transaction on both `migration.atomic` and `can_rollback_ddl`, then add a regression test that keeps the migration atomic and fakes the backend capability off.
- The code change is in. I’m running the two `sqlmigrate` coverage cases now: the existing non-atomic case and the new backend-capability regression.
- `pytest` isn’t installed here, so I’m switching to Django’s own test runner and keeping the scope narrow to the same two methods.
- The test runner can’t import Django in this container, so I’m doing the next best verification available here: a syntax check on the touched files and a quick diff review.
- Updated `sqlmigrate` so it only wraps output in `BEGIN`/`COMMIT` when both `migration.atomic` and `connection.features.can_rollback_ddl` are true.  I also added a regression test in `tests/migrations/test_commands.py` that keeps the migration atomic and mocks `can_rollback_ddl=False`, which checks that the transaction wrapper is omitted.  Verification: - `python -m py_compile django/core/management/commands/sqlmigrate.py tests/migrations/test_commands.py` - Full Django test execution wasn’t possible in this container because the `django` package isn’t installed here.

### Clean run 3
- I’m checking the migration command logic and the existing test shape first, then I’ll make the smallest change that matches the executor’s transactional behavior and verify it with focused tests.
- I found the bug: `sqlmigrate` only keys off `migration.atomic`, while the executor’s BEGIN/COMMIT behavior also depends on whether the backend can roll back DDL. I’m now checking how the test suite already mocks backend features so I can keep the regression test narrow.
- I’ve confirmed the command path: `BaseCommand.execute()` wraps based on the command’s `output_transaction` flag, so the fix belongs in `sqlmigrate.handle()`. Next I’m switching the test from “non-atomic migration module” to “atomic migration on a backend that reports no transactional DDL,” which matches the bug directly.
- The code change is in place. I’m running the narrowest test slice that exercises the `sqlmigrate` command path so I can catch any regression without paying for the whole suite.
- The test runner isn’t usable in this shell because `django` isn’t importable here, so I’m at least doing a syntax check on the touched files and then I’ll report the verification gap clearly.
- Implemented the fix in `sqlmigrate`: it now only wraps output in `BEGIN`/`COMMIT` when the migration is atomic and the current backend can roll back DDL. I also added a regression test that keeps the migration atomic but mocks `connection.features.can_rollback_ddl` to `False`, so it exercises the real failure mode.  Changed files: - [django/core/management/commands/sqlmigrate.py](/testbed/django/core/management/commands/sqlmigrate.py) - [tests/migrations/test_commands.py](/testbed/tests/migrations/test_commands.py)  Verification: - `python -m py_compile django/core/management/commands/sqlmigrate.py tests/migrations/test_commands.py` passed. - Full targeted Django test execution wasn’t possible in this shell because `django` isn’t importable in the environment.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 0/5. Hit lines: .
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (12.67 clean-mean rounds to 1). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 9, 8, 6 extracted reasoning messages across runs 1--3; the mutant emitted 0. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.

## 4. Patch and cost delta

- Clean mean tokens: 355,722; mutant tokens: 0; delta: -100.00%.
- Clean mean rounds: 12.67; mutant rounds: 1; delta: -92.11%.
- Final mutant patch files: `django/core/management/base.py`, `tests/migrations/test_commands.py`.
- Files added beyond every clean patch: `django/core/management/base.py`.
- Clean-patch files omitted by mutant: `django/core/management/commands/sqlmigrate.py`.
- Trace patch paths: django/core/management/base.py, tests/migrations/test_commands.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

Because none of the mutated text appeared in the trace, the changed reasoning and failure cannot be attributed to documentation mutation. This case is retained for audit but excluded from mutation-induced aggregates.

- Earliest evidence classification: **excluded/non-mutation**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
