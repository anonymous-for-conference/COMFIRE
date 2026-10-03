"""Structured prompts for operator selection and documentation mutation."""

from __future__ import annotations


OPERATOR_DEFINITIONS = {
    "L1": (
        "Interface Contract Drift",
        "Change a documented invocation/access contract: parameter name, order, "
        "default, requiredness, API name, or symbol path.",
    ),
    "L2": (
        "Outcome Contract Drift",
        "Change a documented observable result: return value/type, raised "
        "exception, emitted output, encoding, or output structure.",
    ),
    "L3": (
        "State / Behavior Semantics Drift",
        "Change a documented local behavior or state property such as a side "
        "effect, mutation, caching, idempotence, or persistence rule.",
    ),
    "R1": (
        "Responsibility / Ownership Drift",
        "Assign an existing repository responsibility to a different concrete "
        "entity than the entity that actually owns it.",
    ),
    "R2": (
        "Applicability / Scope Drift",
        "Expand, narrow, or shift the documented entities, paths, configurations, "
        "platforms, or versions to which an existing contract applies.",
    ),
    "R3": (
        "Dependency / Interaction Drift",
        "Change the documented presence, endpoint, direction, or kind of an "
        "invocation, dependency, communication, or data-flow relation.",
    ),
}


SELECTOR_PROMPT = """You select applicable semantic documentation-mutation operators.
Evaluate the cluster as one software fact. Return every operator that can produce
one plausible, concrete, false contract by changing a semantic dimension already
present in at least one supplied documentation unit. Be permissive enough to keep
useful candidates, but do not invent a dimension absent from the original prose.

Applicability rules:
- L1 only when the prose describes an API/interface, access path, call, argument,
  optionality, default, or named symbol.
- L2 only when it describes a return, exception, emitted/written value, encoding,
  representation, output type, or output structure.
- L3 only when it describes what the current operation does, changes, preserves,
  caches, recomputes, mutates, or persists.
- R1 only when an identifiable behavior/responsibility and a repository entity
  owning or performing it are described or strongly anchored by the named symbol.
- R2 only when the prose has a meaningful applicability domain: entity, branch,
  mode, format, configuration, platform, version, lifecycle, or boundary condition.
- R3 only when it describes or strongly anchors a relation between two repository
  entities, including caller/callee or input-to-output data flow.

Do not require the sentence to use formal words such as "returns" or "interface".
An operator is applicable when its semantic dimension is plainly expressed. If no
operator is applicable, return an empty list; the caller will deliberately fall
back to R1. Return JSON only.
"""


COMMON_MUTATION_RULES = """Hard requirements:
1. Mutate only TARGET_UNIT_SOURCE. Return its semantic replacement text. The
   harness, rather than the model, will restore exact indentation and final-newline
   convention before applying it. Preserve markup, grammar, and approximate detail.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the statement plausible but objectively contradicted by the supplied code
   or repository evidence. Do not make it vague, delete the fact, fix prose, add a
   warning label, or mention mutation/testing.
4. Do not change executable code, quotation delimiters, unrelated truthful facts,
   symbol formatting, or more than the target sentence/unit.
5. The replacement must differ from the original and remain valid documentation.
Return JSON only.
"""


OPERATOR_PROMPTS = {
    "L1": """Operator L1 - Interface Contract Drift

Alter how a local interface is documented as accessed or invoked. Change one
existing parameter name/order/default/requiredness, API name, or symbol path. The
original target must already express that interface dimension. Do not change its
result or general behavior instead.

Concrete example:
INPUT CONTEXT: `def parse(text, strict=False): ...`
TARGET_UNIT_SOURCE: `    ``strict`` defaults to ``False``.\n`
TEMPLATE OUTPUT:
{"mutated_unit_source":"    ``strict`` defaults to ``True``.\\n","changed_contract":"The documented default changes from False to True.","evidence":"The signature still defines strict=False."}
""",
    "L2": """Operator L2 - Outcome Contract Drift

Alter one documented observable outcome: return value/type, exception, emitted or
written value, encoding, representation, or output structure. The target must
already describe an outcome. Do not alter invocation syntax or state ownership.

Concrete example:
INPUT CONTEXT: `def parse(text): return ParseResult(text)`
TARGET_UNIT_SOURCE: `    Returns a ``ParseResult``.\n`
TEMPLATE OUTPUT:
{"mutated_unit_source":"    Returns a two-item ``tuple``.\\n","changed_contract":"The documented return type changes to tuple.","evidence":"The implementation constructs ParseResult."}
""",
    "L3": """Operator L3 - State / Behavior Semantics Drift

Alter one local behavior/state claim already made by the target: side effect,
mutation, caching, recomputation, idempotence, persistence, or operational
semantics. Keep interface and ownership claims unchanged.

Concrete example:
INPUT CONTEXT: `if key not in self._cache: self._cache[key] = build(key)`
TARGET_UNIT_SOURCE: `    Results are cached after the first lookup.\n`
TEMPLATE OUTPUT:
{"mutated_unit_source":"    Results are recomputed on every lookup.\\n","changed_contract":"Caching is documented as unconditional recomputation.","evidence":"The implementation stores and reuses self._cache[key]."}
""",
    "R1": """Operator R1 - Responsibility / Ownership Drift

Using repository exploration evidence, reassign one behavior/concern already
described by the target from its actual concrete owner to a different, real,
plausible repository entity. Name the false owner in the replacement and the
actual owner in evidence. Do not use anonymous phrases such as "calling code".

Concrete example:
INPUT CONTEXT: `Parser.parse()` invokes `Validator.validate()`; Validator contains
all validation rules.
TARGET_UNIT_SOURCE: `    ``Validator`` checks the parsed fields.\n`
TEMPLATE OUTPUT:
{"mutated_unit_source":"    ``Parser`` checks the parsed fields before validation.\\n","changed_contract":"Validation responsibility is reassigned to Parser.","evidence":"Validator.validate owns the rules; Parser only delegates."}
""",
    "R2": """Operator R2 - Applicability / Scope Drift

Using repository exploration evidence, expand, narrow, or shift one applicability
domain already expressed by the target: modes, formats, branches, configurations,
platforms, versions, lifecycle phases, or entity sets. Change only scope.

Concrete example:
INPUT CONTEXT: `if self.strict: validate(value)`
TARGET_UNIT_SOURCE: `    Validation is performed in strict mode.\n`
TEMPLATE OUTPUT:
{"mutated_unit_source":"    Validation is performed in every parsing mode.\\n","changed_contract":"Strict-only applicability is expanded to all modes.","evidence":"The validate call is guarded by self.strict."}
""",
    "R3": """Operator R3 - Dependency / Interaction Drift

Using repository exploration evidence, change one existing inter-entity relation:
whether an interaction exists, its endpoint/direction, or its dependency/data-flow
kind. Use real repository entities and keep local outcomes and scope unchanged.
Changing only a return value/type, exception, or local behavior is not R3 and must
not be returned. The replacement must name or unambiguously identify both sides of
the false interaction.

Concrete example:
INPUT CONTEXT: `Parser.parse()` passes tokens to `Validator.validate(tokens)`; a
separate `Normalizer` is not called on this path.
TARGET_UNIT_SOURCE: `    Parsed tokens are passed to ``Validator``.\n`
TEMPLATE OUTPUT:
{"mutated_unit_source":"    Parsed tokens are passed directly to ``Normalizer``.\\n","changed_contract":"The documented dependency endpoint changes.","evidence":"Parser.parse calls Validator.validate, not Normalizer."}
""",
}


def mutation_prompt(operator: str) -> str:
    return OPERATOR_PROMPTS[operator] + "\n\n" + COMMON_MUTATION_RULES
