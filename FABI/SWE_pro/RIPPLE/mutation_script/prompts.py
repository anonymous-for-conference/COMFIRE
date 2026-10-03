"""Prompts and schemas for the six documentation mutation operators."""

OPERATORS = {
    "L1": "Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.",
    "L2": "Outcome Contract Drift: alter return values/types, exceptions, or output structure.",
    "L3": "State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.",
    "R1": "Responsibility / Ownership Drift: assign a repository behavior or concern to a different entity.",
    "R2": "Applicability / Scope Drift: expand, narrow, or shift the configurations, paths, platforms, versions, or entities covered.",
    "R3": "Dependency / Interaction Drift: alter an invocation, dependency, communication, or data-flow relation between entities.",
}

SELECTOR_PROMPT = """You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
- R1 requires a behavior, concern, or responsibility that can plausibly be assigned to another real repository entity.
- R2 requires a contract with an applicability domain that can plausibly be shifted: mode, branch, configuration, platform, version, lifecycle, or entity set.
- R3 requires or strongly implies a relation between repository entities, such as a call, dependency, communication path, or data flow.
Return an empty list only when none can apply; the caller will use the configured fallback operator.

Operator definitions:
{operator_definitions}

Return JSON matching the supplied schema and no prose.
"""

COMMON_RULES = """Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.
"""

OPERATOR_PROMPTS = {
    "L1": """Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.""",
    "L2": """Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.""",
    "L3": """Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.""",
    "R1": """Apply R1 Responsibility / Ownership Drift. After repository exploration, assign the documented behavior or concern to another real and plausible repository entity. Name or unambiguously identify the false owner.""",
    "R2": """Apply R2 Applicability / Scope Drift. After repository exploration, expand, narrow, or shift one documented applicability domain (mode, branch, configuration, platform, version, lifecycle, or entity set).""",
    "R3": """Apply R3 Dependency / Interaction Drift. After repository exploration, change the presence, endpoint, direction, or kind of an inter-entity call/dependency/communication/data-flow relation. Identify both sides unambiguously.""",
}


def selector_prompt(enabled_operators: tuple[str, ...] = tuple(OPERATORS)) -> str:
    definitions = "\n".join(f"- {key}: {OPERATORS[key]}" for key in enabled_operators)
    return SELECTOR_PROMPT.format(operator_definitions=definitions)


def mutation_prompt(operator: str) -> str:
    return OPERATOR_PROMPTS[operator] + "\n\n" + COMMON_RULES
