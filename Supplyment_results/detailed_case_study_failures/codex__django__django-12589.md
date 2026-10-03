# Codex: django__django-12589

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 7/8 locations.

## 1. Problem and expected correct approach

Django 3.0: "GROUP BY" clauses error with tricky field annotation
Description
	
Let's pretend that we have next model structure with next model's relations:
class A(models.Model):
	bs = models.ManyToManyField('B',
								related_name="a",
								through="AB")
class B(models.Model):
	pass
class AB(models.Model):
	a = models.ForeignKey(A, on_delete=models.CASCADE, related_name="ab_a")
	b = models.ForeignKey(B, on_delete=models.CASCADE, related_name="ab_b")
	status = models.IntegerField()
class C(models.Model):
	a = models.ForeignKey(
		A,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name="c",
		verbose_name=_("a")
	)
	status = models.IntegerField()
Let's try to evaluate next query
ab_query = AB.objects.filter(a=OuterRef("pk"), b=1)
filter_conditions = Q(pk=1) | Q(ab_a__b=1)
query = A.objects.\
	filter(filter_conditions).\
	annotate(
		status=Subquery(ab_query.values("status")),
		c_count=Count("c"),
)
answer = query.values("status").annotate(total_count=Count("status"))
print(answer.query)
print(answer)
On Django 3.0.4 we have an error
django.db.utils.ProgrammingError: column reference "status" is ambiguous
and query is next:
SELECT (SELECT U0."status" FROM "test_app_ab" U0 WHERE (U0."a_id" = "test_app_a"."id" AND U0."b_id" = 1)) AS "status", COUNT((SELECT U0."status" FROM "test_app_ab" U0 WHERE (U0."a_id" = "test_app_a"."id" AND U0."b_id" = 1))) AS "total_count" FROM "test_app_a" LEFT OUTER JOIN "test_app_ab" ON ("test_app_a"."id" = "test_app_ab"."a_id") LEFT OUTER JOIN "test_app_c" ON ("test_app_a"."id" = "test_app_c"."a_id") WHERE ("test_app_a"."id" = 1 OR "test_app_ab"."b_id" = 1) GROUP BY "status"
However, Django 2.2.11 processed this query properly with the next query:
SELECT (SELECT U0."status" FROM "test_app_ab" U0 WHERE (U0."a_id" = ("test_app_a"."id") AND U0."b_id" = 1)) AS "status", COUNT((SELECT U0."status" FROM "test_app_ab" U0 WHERE (U0."a_id" = ("test_app_a"."id") AND U0."b_id" = 1))) AS "total_count" FROM "test_app_a" LEFT OUTER JOIN "test_app_ab" ON ("test_app_a"."id" = "test_app_ab"."a_id") LEFT OUTER JOIN "test_app_c" ON ("test_app_a"."id" = "test_app_c"."a_id") WHERE ("test_app_a"."id" = 1 OR "test_app_ab"."b_id" = 1) GROUP BY (SELECT U0."status" FROM "test_app_ab" U0 WHERE (U0."a_id" = ("test_app_a"."id") AND U0."b_id" = 1))
so, the difference in "GROUP BY" clauses
(as DB provider uses "django.db.backends.postgresql", postgresql 11)

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `django/db/models/expressions.py`, `tests/queries/tests.py`
- Clean run 2: `django/db/models/query.py`, `django/db/models/sql/query.py`, `tests/queries/tests.py`
- Clean run 3: `django/db/models/sql/compiler.py`, `tests/aggregation/tests.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `django/db/models/query.py` / `django/db/models/query.py::QuerySet.annotate`
  - Clean doc: Return a query set in which the returned objects have been annotated
  - Mutated doc: Return a query set in which the returned objects are not annotated
  - Contract change: Annotation persistence is documented as omission: returned objects do not receive the supplied extra data or aggregations.
- `django/db/models/query.py` / `django/db/models/query.py::QuerySet.annotate`
  - Clean doc: with extra data or aggregations.
  - Mutated doc: with extra data or aggregations on the original query set.
  - Contract change: Annotations are documented as modifying the original query set rather than a cloned query set.
- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler.get_group_by`
  - Clean doc: The logic of what exactly the GROUP BY clause contains is hard
        to describe in other words than "if it passes the test suite,
        then it is correct".
  - Mutated doc: The logic of what exactly the GROUP BY clause contains is hard
        to describe in other words than "if it passes the test suite,
        then it is cached".
  - Contract change: GROUP BY clause contents are documented as being cached after validation.
- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler.get_group_by`
  - Clean doc: Return a list of 2-tuples of form (sql, params).
  - Mutated doc: Return a list of 3-tuples of form (sql, params).
  - Contract change: The documented return structure changes from 2-tuples to 3-tuples.
- `django/db/models/sql/compiler.py` / `django/db/models/sql/compiler.py::SQLCompiler.get_order_by`
  - Clean doc: The order_by clause can alter the select clause (for example it
        can add aliases to clauses that do not yet have one, or it can
        add totally new select clauses).
  - Mutated doc: The order_by clause can alter the where clause (for example it
        can add aliases to clauses that do not yet have one, or it can
        add totally new select clauses).
  - Contract change: The documentation changes the affected output structure from the SELECT clause to the WHERE clause.
- `tests/aggregation/tests.py` / `tests/aggregation/tests.py::AggregateTestCase.test_aggregation_subquery_annotation`
  - Clean doc: Subquery annotations are excluded from the GROUP BY if they are
        not explicitly grouped against.
  - Mutated doc: Subquery annotations are included in the GROUP BY if they are
        not explicitly grouped against.
  - Contract change: Subquery annotations are documented as included in the GROUP BY when they are not explicitly grouped against.
- `tests/aggregation/tests.py` / `tests/aggregation/tests.py::AggregateTestCase.test_group_by_subquery_annotation`
  - Clean doc: Subquery annotations are included in the GROUP BY if they are
        grouped against.
  - Mutated doc: Subquery annotations are excluded from the GROUP BY if they are
        grouped against.
  - Contract change: Subquery annotations are excluded from the GROUP BY even when they are explicitly grouped against.
- `tests/aggregation/tests.py` / `tests/aggregation/tests.py::AggregateTestCase.test_group_by_exists_annotation`
  - Clean doc: Exists annotations are included in the GROUP BY if they are
        grouped against.
  - Mutated doc: Exists annotations are excluded from the GROUP BY if they are
        grouped against.
  - Contract change: Explicitly grouped Exists annotations are documented as excluded from GROUP BY.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m inspecting the ORM grouping and annotation code paths first, then I’ll reproduce the regression with focused tests and patch the smallest place that changes the `GROUP BY` behavior.
- `rg` isn’t available here, so I’m switching to plain filesystem inspection and targeted `grep` searches in the ORM code and tests.
- I found existing subquery/group-by coverage, so I’m reading the expression and query compiler code around those paths to see why a subquery annotation is collapsing to its alias in `GROUP BY`.
- The failure smells like alias resolution: `values('status')` is probably being treated as the model field instead of the annotation alias, which then collapses `GROUP BY` to the wrong SQL. I’m tracing how `resolve_ref()` and `values()` decide between annotation names and concrete columns.
- I’ve narrowed it down to the `values()`/`set_group_by()` interaction. The key question now is whether the annotation alias `status` is being turned into a `Ref('status', ...)` too early, which would make the compiler emit `GROUP BY "status"` instead of the subquery expression.
- I’ve confirmed `values()` delegates to `Query.set_values()`, so I’m checking whether annotations are being masked or copied in a way that loses the original subquery expression before grouping is finalized.
- I found the likely mechanism: `GROUP BY "status"` is ambiguous because the query already joins tables that also have a `status` column. I’m checking whether the subquery/expression path can safely avoid alias-based grouping without breaking existing aggregation tests.
- There’s already a `status` field in the `queries` test app, so I’m checking whether I can build a compact regression there instead of introducing new test models.
- I’ve got the fix path: make subqueries group by their expression instead of the select alias, then add a regression test that uses the existing `Order`/`OrderItem` models and the `status` column collision. I’m patching both now.
- The code change is in place. I’m running the narrowest useful test slice next to verify both the new regression and that the surrounding queryset behavior still passes.
- The test runner here doesn’t support `-k`, so I’m running the `queries` app tests directly. That’s broader than ideal, but still focused on the queryset code we changed.
- The `queries` app passed, including the new regression. I’m running the aggregation app as a second check because the grouping change touches shared ORM code used there too.
- The first pass fixed the subquery collision but changed `Exists` grouping semantics too much. I’m restoring the prior `Exists` behavior explicitly and keeping the alias suppression only for plain `Subquery`.
- The grouping behavior needs to stay on the subquery/expression itself, not on its correlated outer columns. I’m switching to that simpler rule and dropping the `Exists` override so both `Subquery` and `Exists` group correctly.
- The implementation is now simplified to one rule: subqueries group by the subquery expression itself. I’m rerunning the aggregation app first because that’s where the regression showed up from the shared ORM change.
- I’ve got the narrower rule now: only explicit grouping requests should keep a subquery in `GROUP BY`; plain annotated subqueries should stay out. I’m encoding that as “`alias` present => group by the subquery expression, otherwise exclude it.”
- The rule is now aligned with the regression: implicit annotations don’t group by the subquery, but explicit `values()` grouping does. I’m rerunning aggregation, then I’ll recheck the queryset app with the new regression test.
- I need one more bit of visibility into the generated query shape, so I’m looking at the test settings and then I’ll inspect the SQL for the exact failing queryset instead of guessing from the assertion count.
- I’ve got the exact SQL now. The remaining step is to confirm whether the compiler is calling `get_group_by_cols()` with the annotation alias somewhere other than the `set_group_by()` path, because that would explain why the subquery still lands in the `GROUP BY` list.
- I spotted the mismatch: the file currently has the unconditional `[self]` version, so the latest intended alias-sensitive change didn’t stick. I’m checking the diff and then I’ll correct the method precisely.
- The diff shows the real mistake: I accidentally changed `RawSQL` instead of just `Subquery` on one pass. I’m restoring `RawSQL` and making `Subquery` alias-sensitive only when it’s explicitly grouped against.
- There’s one more accidental edit in `Col.get_group_by_cols`; that one should stay untouched. I’m restoring it and then applying the `Subquery` change with tighter context so it lands on the right method.
- The accidental edit moved again, this time onto `Ref.get_group_by_cols`. I’m restoring `Ref` to the original behavior and then patching `Subquery` with a narrower context block to avoid further drift.
- The expression code is back on the intended methods. I’m rerunning the exact aggregation regression that was failing, then I’ll rerun the new query regression by name.
- The exact regressions pass. I’m running the two touched app suites once more to catch any collateral behavior change from the grouping tweak before I wrap up.
- Fixed the `GROUP BY` regression by making `Subquery.get_group_by_cols()` only participate when the subquery is explicitly grouped against, and then grouping by the subquery expression itself rather than the alias. That avoids the ambiguous `GROUP BY "status"` case while preserving the existing behavior for ordinary annotated subqueries.  Changed: - [`django/db/models/expressions.py:1052`](/testbed/django/db/models/expressions.py#L1052) - [`tests/queries/tests.py:3559`](/testbed/tests/queries/tests.py#L3559)  Verification: - `python tests/runtests.py aggregation --verbosity 1 --failfast` - `python tests/runtests.py queries --verbosity 1 --failfast`

### Clean run 2
- I’m tracing the queryset compilation path that decides `GROUP BY` for annotations, then I’ll reproduce the regression with focused tests and patch the smallest place that changed behavior.
- `rg` isn’t available here, so I’m switching to plain filesystem search and narrowing to the ORM compiler and existing annotation/group-by tests.
- I’ve confirmed this is a full Django tree. Next I’m locating the annotation/group-by code path and the closest existing regression tests so I can mirror the bug instead of inventing a new shape.
- There are already regression tests around subquery grouping; I’m reading those first to see whether this bug is a missing case or a compiler regression adjacent to an existing rule.
- The compiler logic is clear: `GROUP BY` is built from each selected expression’s `get_group_by_cols()`. I’m now checking whether the `Subquery` expression changed its grouping behavior, because the regression smells like it started returning the inner `Col` instead of the subquery SQL wrapper.
- I’ve found the likely regression point: `Subquery.get_group_by_cols()` now prefers `Ref(alias, self)` when the annotation is selected, which emits `GROUP BY "status"`. I’m checking whether that alias path should be suppressed for this particular shape, or whether the compiler should avoid alias grouping when the alias can collide with joined columns.
- I have enough of the code path to narrow the fix. Before editing, I’m checking whether the project already has a later regression test or nearby commit that describes the intended behavior, so I can match Django’s existing conventions.
- I found a likely upstream fix: `#31150` “Included subqueries that reference related fields in GROUP BY clauses.” I’m reading that patch now because it may be the exact behavior change the regression needs, and I want the smallest faithful backport.
- The collision is likely coming from `values()` preserving annotation aliases in `GROUP BY`. I’m checking the queryset state transitions around `annotate()` and `values()` to see whether `allow_aliases=False` is already used in one path but not this one.
- The shape is clearer now: the first `annotate()` sets `group_by=True`, `values('status')` rebuilds the selected annotation list, and the final `annotate(total_count=Count('status'))` calls `set_group_by()` again with aliases allowed. That second pass is where the alias `"status"` comes back and collides with joined table columns.
- I found an even more targeted follow-up commit: `#31150` also “Enabled implicit GROUP BY aliases.” That sounds closer to the exact alias-resolution behavior in this bug, so I’m reading that patch next.
- The local tree doesn’t have the newer `allows_group_by_refs` feature yet, so I’m backporting the behavior at the compiler level instead of relying on a later feature flag. I’m now reproducing the SQL shape with a focused test to confirm the minimal change needed.
- The current regression still looks like an aliasing issue rather than a subquery-shape issue. I’m checking the later `#31136` change too, because it disables GROUP BY aliases in `values()/values_list()` and might be the exact guard that should apply here.
- I’ve ruled out the earlier `#31150` subquery-shape fix as the whole answer; this is a later alias-collision regression. I’m searching history for any patch that specifically changed when annotation aliases are allowed in `GROUP BY`, because that’s the likely smallest backport.
- I’ve settled on the fix strategy: make the second `GROUP BY` expansion in `annotate()` stop reintroducing aliases for already-selected values queries, then add a regression using the existing `Order`/`OrderItem` models so the bug is exercised without new schema scaffolding.
- I’m making the code change now, then I’ll run the targeted query tests to verify the SQL no longer uses the ambiguous alias.
- The patch is in place. I’m running the new regression plus a nearby existing subquery test to catch any unintended `GROUP BY` fallout from the alias change.
- The first pass was too broad: it fixed the ambiguous case but broke an existing test that legitimately wants to group by a selected subquery expression. I’m tightening the fix to only disable alias grouping when the alias actually collides with a column name present in the query’s joined tables.
- I’ve got the narrower rule: only fall back to non-alias grouping when a selected annotation alias would actually be ambiguous against columns from joins already present in the query. That keeps the existing subquery-grouping test intact while fixing the collision case.
- I’ve narrowed the code path so the fallback only triggers on real alias collisions. I’m rerunning the focused tests now to make sure the original subquery grouping case still passes.
- The test needs to validate the SQL shape, not a hand-computed result set. I’m changing it to execute the queryset and assert that the generated `GROUP BY` doesn’t fall back to the ambiguous `"status"` alias.
- I’ve switched the regression to a SQL-shape assertion, which is the right level for this backend-specific bug. I’m rerunning the focused tests now.
- The focused regression and the nearby aggregation tests both pass now. I’m doing one last diff review for the exact files changed so I can summarize the fix cleanly.
- I’ve verified the new regression and the existing aggregation subquery tests. I’m running one representative `values().annotate()` case as a sanity check, since that’s the code path we touched.
- I hit a bad test target name on the last sanity check. I’m swapping to a real nearby test that exercises a `values_list()` subquery path and should be sensitive to the same query plumbing.
- Implemented the fix and left it in the tree.  What changed: - In [django/db/models/query.py](/testbed/django/db/models/query.py), `annotate()` now checks whether selected annotation aliases collide with joined column names before rebuilding `GROUP BY`. - In [django/db/models/sql/query.py](/testbed/django/db/models/sql/query.py), I added a small helper to detect those alias collisions. - In [tests/queries/tests.py](/testbed/tests/queries/tests.py), I added a regression test that exercises the ambiguous `status` alias case and asserts the generated SQL doesn’t fall back to `GROUP BY "status"`.  Validation: - `python tests/runtests.py queries.tests.ValuesSubqueryTests.test_values_annotation_group_by_uses_subquery_sql --verbosity 2` - `python tests/runtests.py aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation aggregation.tests.AggregateTestCase.test_group_by_subquery_annotation --verbosity 2` - `python tests/runtests.py queries.tests.ValuesSubqueryTests.test_values_in_subquery --verbosity 2`  The key behavior is now: - safe subquery grouping still works when the alias is valid - ambiguous alias grouping is avoided when joins introduce conflicting column names

### Clean run 3
- I’m inspecting the ORM query compilation path and the existing regression tests around annotations and `GROUP BY` so I can make the smallest fix that preserves the Django 2.2 behavior where it matters.
- `rg` isn’t available here, so I’m switching to `grep`/`find` and reading the compiler/query code paths directly. I’m looking for where annotation references are turned into `GROUP BY` expressions, because the symptom points to an alias-vs-expression regression.
- I’ve found the relevant machinery in `Query.set_group_by()` and `SQLCompiler.get_group_by()`. Next I’m checking whether annotated aliases are being preserved through `values().annotate()` or whether the compiler is collapsing them back to raw column names too early.
- There are already several subquery/group-by regression tests. I’m reading those first to avoid duplicating coverage and to slot the new case into the same behavior boundary rather than inventing a separate test style.
- The existing tests already cover “subquery in GROUP BY” cases, but not this specific pattern: a later `.values('status')` reuses an annotation alias that is also a subquery. I’m checking how `Subquery.get_group_by_cols()` and `Ref` interact, because the ambiguity suggests we’re grouping by the alias name instead of the subquery SQL.
- I have the candidate code path: `values()` rewrites selected annotation names through `resolve_ref()`, and `set_group_by()` decides whether annotations can be grouped by alias. I’m reading those pieces now to confirm whether the alias is being treated like a plain selected column when it should stay as the underlying subquery.
- I’ve narrowed it down further: the bad SQL looks like a `Ref` survived into `group_by`, which means the alias-preserving path was used when the query later needed the full expression. I’m tracing where the annotation is marked as “selected” versus “grouped” so I can adjust the exact branch rather than broadening group-by behavior globally.
- I haven’t found a broad regression yet, so I’m checking the point where adding an aggregate flips `query.group_by` on. If that happens before `values('status')` runs, the later `values()` call may be reusing stale alias-based grouping instead of recomputing from the selected annotation mask.
- I’m at the point where the SQL shape suggests a stale alias is being retained somewhere in grouping, but the exact branch still needs confirmation. I’m checking whether the fix already exists in another regression test or nearby commit message, because that will tell me whether I should patch compiler grouping or the annotation-selection step.
- I found likely relevant history: Django has prior fixes around disabling `GROUP BY` aliases for `values()` and `exists()`, and one commit specifically mentions subquery group-by behavior. I’m reading those patches now to borrow the narrowest correction instead of inventing a new rule.
- The history confirms this area has already been touched for related regressions, so I’m now looking for a follow-up fix or a later refactor that would explain why this specific `values('status')` + subquery case still leaks an alias. If I can’t find one, I’ll patch the group-by path directly and add a regression test in the aggregation suite.
- I found a later commit specifically titled “Fixed #34176 -- Fixed grouping by ambiguous aliases.” That sounds very close to the failure mode here, so I’m inspecting that patch and will adapt the smallest relevant part into this tree.
- I found the upstream fix pattern: stop emitting the alias itself in `GROUP BY` when that alias can collide, and group by the underlying expression instead. The newer patch also uses select-index optimization, but for this backport I only need the alias-collision part plus a regression test that matches this subquery case.
- I confirmed this checkout doesn’t have the newer `allows_group_by_select_index` feature, so I’m keeping the backport minimal and compatible with the existing compiler logic. I’m now checking the feature flags that already exist so the patch stays within the current backend contract.
- I’ve got enough source context to patch, but I want one quick sanity check against the live ORM before editing: I’m going to reproduce an analogous query with existing models so I can confirm whether the bad `GROUP BY` is coming from the compiler branch or from `set_group_by()` itself.
- I’m applying the fix now: first the compiler change so `GROUP BY` keeps the underlying expression for aliased `Ref`s, then a regression test modeled on the upstream ambiguous-alias case but using the existing `Publisher`/`Book` fixtures.
- The compiler patch is in. The test insertion missed the exact local context, so I’m reopening the surrounding block and placing the regression next to the existing subquery/group-by tests.
- The code and regression test are in place. I’m running the narrowest relevant test now to verify the SQL path and ensure the new case passes without broadening the blast radius.
- The regression test exposed that my expected row set was too aggressive. I’m checking the actual compiled SQL and result shape now so I can align the test with the real grouping semantics and confirm the fix is still taking effect.
- The compiled SQL confirms the fix path is correct: the `GROUP BY` now uses the subquery expression, not the alias. I’m tightening the regression test to assert the SQL shape directly and to match the real row set from this queryset.
- The regression test now checks both the result shape and the absence of the ambiguous alias in `GROUP BY`. I’m rerunning that case and a nearby subquery/group-by test to make sure the compiler change didn’t disturb the existing behavior.
- The targeted regression and a neighboring subquery-group-by test both pass. I’m running the full `AggregateTestCase` on SQLite as a sanity pass since the fix touched shared grouping logic and I want to catch any collateral regression in the same suite.
- The shared compiler change was too broad: it fixed the collision case but disturbed existing explicit subquery grouping tests. I’m inspecting those two failures directly so I can narrow the behavior to alias collisions without changing how ordinary grouped subqueries are counted.
- I found the mistake: the skip logic needs to remember the grouped expression object itself, not the alias name. That preserves explicit grouped subqueries while still preventing the select clause from re-expanding them into outer columns. I’m reverting to source-based skipping and rerunning the same focused tests.
- The compiler now skips select re-expansion by expression identity, which is the behavior we want here. I’m rerunning the three relevant tests to confirm the collision fix and make sure the existing grouped-subquery cases are back to normal.
- The remaining mismatch is only the expected counts in the new regression test. The compiler behavior is now consistent, so I’m correcting the assertion to match the actual grouped result and then rerunning the same narrow set.
- The regression expectation is corrected. I’m rerunning the collision case plus the two existing grouped-subquery tests together, since that’s the minimal set that validates both the fix and the no-regression boundary.
- The focused cases are green again. I’m doing one final pass over the full `AggregateTestCase` on SQLite to make sure the compiler tweak didn’t introduce another grouping regression elsewhere in the same suite.
- Everything in the targeted aggregation suite is now passing. I’m doing a quick status check so I can hand back exactly what changed and the verification command that succeeded.
- Implemented the fix in: - [`/testbed/django/db/models/sql/compiler.py`](file:///testbed/django/db/models/sql/compiler.py) - [`/testbed/tests/aggregation/tests.py`](file:///testbed/tests/aggregation/tests.py)  What changed: - `SQLCompiler.get_group_by()` now preserves the underlying grouped expression for aliased `Ref`s instead of compiling the alias itself. - The select-clause expansion logic skips expressions already grouped by that source expression, which prevents the ambiguous `GROUP BY "status"`/`GROUP BY "rating"` shape without breaking existing explicit subquery grouping. - Added a regression test covering the collision case with a subquery annotation grouped via `values()`.  Verification: - `python tests/runtests.py aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_values_collision --settings=test_sqlite` - `python tests/runtests.py aggregation.tests.AggregateTestCase.test_group_by_subquery_annotation --settings=test_sqlite` - `python tests/runtests.py aggregation.tests.AggregateTestCase.test_group_by_exists_annotation --settings=test_sqlite` - `python tests/runtests.py aggregation.tests.AggregateTestCase --settings=test_sqlite`  All of those passed.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 7/8. Hit lines: [44], [44], [17], [17, 199], [19, 137, 203], [19, 203], [19].
- Relative to the three clean runs, the mutant trajectory **expanded** in interaction length (27.33 clean-mean rounds to 34). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 26, 26, 30 extracted reasoning messages across runs 1--3; the mutant emitted 34. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m inspecting the ORM query compilation path and the existing regression tests first, then I’ll patch the smallest place that restores the older `GROUP BY` behavior for this annotation shape.
- `rg` isn’t available in this environment, so I’m falling back to `grep`/`find` to locate the ORM grouping code and matching regression coverage.
- I found the relevant compiler and existing aggregation regression coverage. Next I’m reading the exact `GROUP BY` expansion logic and nearby tests to see where the alias/reference switch happened.
- I’ve confirmed the regression is in `GROUP BY` generation, not the subquery itself. I’m now checking how selected annotations are converted into `Ref`/expression objects so I can keep the fix narrow and avoid changing unrelated grouping behavior.
- The suspicious path is `Query.set_values()` when `values()` keeps only an annotation. I’m reading `Ref` and the `set_group_by()` input/output to confirm whether the annotation is being grouped by alias instead of by its expression.
- I have the key symptom: `Subquery.get_group_by_cols(alias=...)` now prefers a `Ref`, and that becomes a bare `"status"` in SQL. I’m checking the callers to see whether we should suppress aliases specifically for `values()`-selected annotations or only for subqueries that can’t safely be referenced by alias.
- I’ve isolated the regression mechanism: `values('status')` clears aliases correctly, but the later `annotate(total_count=Count('status'))` rebuilds `GROUP BY` with aliases turned back on. I’m checking whether there are existing tests that depend on alias-based grouping before I change that behavior.
- I’m making the fix in the expression layer and adding a regression test that reproduces the alias collision shape using the existing `Book`/`Author` fixtures.
- The code change is in place. I’m running the narrowest test slice that covers the regression and the surrounding subquery aggregation behavior so I can catch any unintended SQL shape changes quickly.
- `tests/runtests.py` needs the repo on `PYTHONPATH` here. I’m rerunning the targeted tests with the workspace root added so the local Django package is importable.
- The test run is blocked by missing runtime deps in this container, starting with `asgiref`. I’m checking the local packaging metadata to install only the minimum needed dependencies instead of guessing.
- Dependency installation is in progress; once that finishes I’ll rerun the two focused aggregation tests and, if needed, inspect the generated SQL directly.
- The test label was off because this module’s class name differs from the one I guessed. I’m locating the exact class and rerunning the two targeted methods directly.
- The first pass at the regression assertion was too strict: the fixed query groups by `contact_id`, which is still correct and avoids the alias collision. I’m relaxing the test to assert the real invariant: no `GROUP BY "age"` and the grouped queryset evaluates cleanly.
- The regression test passes. I’m running one more nearby subquery-aggregation test to make sure the broader `GROUP BY` behavior still matches the existing expectations after dropping alias-based grouping for subqueries.
- The failing nearby test shows the previous change was too broad: direct subquery selections still need their existing grouping semantics. I’m restoring the `alias` path and only changing it to group by the subquery expression itself, which avoids alias collisions without changing the fallback behavior.
- I need one more bit of signal from the ORM itself, because the two cases are going through different internal shapes. I’m printing the resolved `group_by` objects for both queries so I can separate the direct `values_list(Subquery(...))` path from the `values('alias').annotate(...)` path.
- The first probe failed because Django apps weren’t loaded before importing the test models. I’m retrying with the setup order corrected so I can inspect the resolved query structures directly.
- The ad hoc probe also needs the test settings module, not the default placeholder. I’m checking the test harness configuration and then I’ll use that to inspect the ORM state safely.
- The evidence points to the simpler rule: subqueries should group by the subquery expression itself, never by an output alias or correlated external columns. I’m switching to that and rerunning the surrounding aggregation tests.
- The failing nearby test clarifies the tradeoff: some subquery annotations do need alias-based grouping to avoid duplicating the subquery in `GROUP BY`. I’m reading that test alongside the query-shaping code so I can narrow the fix to the alias-collision case instead of changing all subquery grouping.
- I’ve narrowed the remaining requirement: keep alias-based grouping for safe subqueries, but suppress it when the alias would collide with a real column on any joined table. I’m checking the `Query` internals now, because that decision has to happen in the outer query where the join list is visible.
- I’ve got the shape of the final fix: keep alias-based grouping for subqueries when the alias is safe, and suppress it only when the current query already joins a table with that column name. I’m wiring that safety check into `Query.set_group_by()` and restoring the subquery expression’s normal alias behavior.
- The remaining failure is on the `group_by=True` path, which bypasses `set_group_by()` and goes straight through the compiler. I’m teaching that path to use the annotation alias only when the outer query says it’s safe.
- The alias-based compiler change was too broad for the `group_by=True` case. I’m reverting that path and keeping the collision check only where `set_group_by()` explicitly builds the grouping list for `values()`/`annotate()` queries.
- I have the simpler split now: direct selected subqueries use the no-alias path, while grouped annotations use the alias-aware path but get rewritten to correlated columns instead of a raw alias. I’m applying that split and rechecking the regression tests.
- The direct `values_list(Subquery(...))` case is not an annotation, so it shouldn’t go through the same alias-aware path as named annotations. I’m narrowing the compiler change to only pass an alias for real annotation select items.
- The missing distinction is between user-named annotations and the auto-generated aliases that `values_list()` creates for expressions. I’m special-casing those generated `subqueryN` aliases so they group by the subquery itself, while named annotations keep the correlated-column path.
- The alias-safety helper turned out not to be needed once the subquery expression itself distinguishes named aliases from generated ones. I’m removing that dead path so the patch stays as small as possible.
- The focused regression set is green. I’m grabbing the final diff summary now so I can report exactly what changed and what I validated.
- I noticed the diff also touched a couple of test docstrings around the existing subquery cases. I’m checking whether those edits are accidental or if they need to stay aligned with the assertions before I wrap up.
- I’m reverting the stray test docstring edits so the patch stays focused on behavior, not wording.
- The last edit was wording only, but I’m rerunning the same focused aggregation slice once more to make sure the working tree still validates cleanly after the cleanup.
- Implemented the fix and left it in the working tree.  What changed: - `Subquery.get_group_by_cols()` now treats auto-generated `values_list()` aliases like `subquery1` as a no-alias case, so those queries keep grouping by the subquery result instead of a colliding column name. See [/testbed/django/db/models/expressions.py:1052](file:///testbed/django/db/models/expressions.py#L1052). - `SQLCompiler.get_group_by()` now passes annotation aliases through when building `GROUP BY`, which lets subquery annotations use the right grouping shape for named annotations. See [/testbed/django/db/models/sql/compiler.py:115](file:///testbed/django/db/models/sql/compiler.py#L115). - Added a regression test covering the alias-collision case with an annotated subquery selected through `values()`. See [/testbed/tests/aggregation/tests.py:1194](file:///testbed/tests/aggregation/tests.py#L1194).  Validation: - Ran focused aggregation tests:   - `aggregation.tests.AggregateTestCase.test_group_by_subquery_annotation`   - `aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation`   - `aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_values_alias_collision`   - `aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_values`   - `aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_multivalued`  All passed.

## 4. Patch and cost delta

- Clean mean tokens: 4,354,258; mutant tokens: 3,982,557; delta: -8.54%.
- Clean mean rounds: 27.33; mutant rounds: 34; delta: +24.39%.
- Final mutant patch files: `django/db/models/expressions.py`, `django/db/models/query.py`, `django/db/models/sql/compiler.py`, `tests/aggregation/tests.py`.
- Files added beyond every clean patch: none.
- Clean-patch files omitted by mutant: `django/db/models/sql/query.py`, `tests/queries/tests.py`.
- Trace patch paths: django/db/models/expressions.py, django/db/models/query.py, django/db/models/sql/compiler.py, tests/aggregation/tests.py.

## 5. Inconsistency awareness and causal mechanism

The trajectory explicitly mentions documentation/docstrings or a contradiction. These are the relevant awareness statements:
- I noticed the diff also touched a couple of test docstrings around the existing subquery cases. I’m checking whether those edits are accidental or if they need to stay aligned with the assertions before I wrap up.
- I’m reverting the stray test docstring edits so the patch stays focused on behavior, not wording.

The mutation was observed before a patch that changed the clean localization/edit footprint. The extra and omitted files above identify the concrete structural divergence; subsequent testing did not restore the clean solution. This is positive evidence of mutation influence, although a single run cannot establish deterministic causality.

- Earliest evidence classification: **Editing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
