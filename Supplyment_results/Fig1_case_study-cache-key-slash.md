# Case 1: Are `/` Characters Allowed in pytest Cache Keys?

## One-Sentence Conclusion

The documentation for pytest's `cache` fixture states that cache keys **must not contain `/`**, but the `Cache` object returned by the fixture explicitly splits keys on `/` and maps the resulting parts to a hierarchical directory structure on disk. Meanwhile, the repository's documentation for `Cache.get`, `Cache.set`, and the cache usage guide all correctly use slash-separated keys.

This case illustrates two phenomena at the same time:

1. The same software fact is documented in multiple places in the repository, but those documentation locations are not all synchronized.
2. The incorrect statement appears in the `cache(request)` fixture, while the actual semantics of cache keys belong to the `Cache` object returned by that fixture. Reading only the fixture itself is therefore insufficient to determine whether the documentation is correct.

## Case Information

- Repository: `pytest-dev/pytest`
- Case ID: `c8eba0fa88b8f6e5546f1cc4`
- Inconsistent snapshot: `e9240f7eeeca501bcc87a052f3dc763d31eba119`
- Documentation-fix commit: `a808e092040c9575312b372b3779cff2e9fee4da`
- Fix date: 2015-09-30
- Fix commit message: "fix docstring for cache fixture regarding ``/`` on keys"

All incorrect documentation, correct documentation, implementation details, and tests discussed below come from the same inconsistent snapshot, so states from different versions are not mixed together.

## 1. What Does the Cache Do?

The pytest cache is used to **persist state across test runs**. In this historical version, it mainly served two types of users:

- pytest itself used the cache to record tests that failed in the previous run, allowing `py.test --lf` to rerun only the previously failing tests and `--ff` to prioritize them.
- Plugins or a project's `conftest.py` could store JSON-compatible data through `config.cache` or the `cache` fixture, avoiding repeated expensive computation in subsequent runs.

The data is stored under `.cache` in the project root. For example, a plugin could reuse data across test runs as follows:

```python
@pytest.fixture
def mydata(request):
    val = request.config.cache.get("example/value", None)
    if val is None:
        val = expensive_computation()
        request.config.cache.set("example/value", val)
    return val
```

The first run performs the computation and writes the result to the cache; later runs retrieve the result using the same key. Here, `example` acts as the namespace for the plugin or application, while `value` is the specific entry within that namespace.

pytest itself stores last-failed state in the same way:

```python
class LFPlugin:
    def __init__(self, config):
        self.config = config
        active_keys = 'lf', 'failedfirst'
        self.active = any(config.getvalue(key) for key in active_keys)
        if self.active:
            self.lastfailed = config.cache.get("cache/lastfailed", {})
        else:
            self.lastfailed = {}

    def pytest_sessionfinish(self, session):
        config = self.config
        if config.getvalue("cacheshow") or hasattr(config, "slaveinput"):
            return
        config.cache.set("cache/lastfailed", self.lastfailed)
```

Therefore, `/` is not an incidental character. It is part of the public key format used by both pytest itself and external plugins to organize cache namespaces.

## 2. The Full Function Containing the Incorrect Documentation

The incorrect statement appears in the fixture function at `_pytest/cacheprovider.py:187-200`:

```python
@pytest.fixture
def cache(request):
    """
    Return a cache object that can persist state between testing sessions.

    cache.get(key, default)
    cache.set(key, value)

    Keys must be strings not containing a "/" separator. Add a unique identifier
    (such as plugin/app name) to avoid clashes with other cache users.

    Values can be any object handled by the json stdlib module.
    """
    return request.config.cache
```

The contradictory sentence is:

```text
Keys must be strings not containing a "/" separator.
```

However, note that the function body contains only one line:

```python
return request.config.cache
```

The fixture neither receives a key nor calls `split`, and it does not create cache files. Even after reading the entire function, a reader can only learn that the fixture returns `request.config.cache`; the function itself provides no way to determine whether `/` is a valid character in a key. This is why the case cannot be validated within the current entity alone.

## 3. Where Does the Object Returned by the Fixture Come From?

The analysis must first cross over to the `pytest_configure` hook in the same file:

```python
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.cache = Cache(config)
    config.pluginmanager.register(LFPlugin(config), "lfplugin")
```

This code shows that `request.config.cache` is an instance of `Cache(config)`. Therefore, to determine whether the documentation is true or false, the relevant implementation to inspect is the `Cache` class rather than the `cache(request)` fixture itself.

The call relationship can be summarized as follows:

```text
test/plugin requests `cache` fixture
              |
              v
cache(request) returns request.config.cache
              |
              v
pytest_configure previously assigned Cache(config)
              |
              v
Cache.get/set -> Cache._getvaluepath -> filesystem under .cache/v/
```

## 4. The Actual `Cache` Implementation

### 4.1 Cache Root Directory

`Cache.__init__` sets the storage location to `.cache` under the project root. The relevant logic is shown below, with tracing-related details omitted:

```python
class Cache(object):
    def __init__(self, config):
        self.config = config
        self._cachedir = config.rootdir.join(".cache")
        self.trace = config.trace.root.get("cache")
        if config.getvalue("cacheclear"):
            if self._cachedir.check():
                self._cachedir.remove()
            self._cachedir.mkdir()
```

### 4.2 Mapping a Key to a Filesystem Path

The semantics of `/` are determined by `_getvaluepath`:

```python
def _getvaluepath(self, key):
    return self._cachedir.join('v', *key.split('/'))
```

The method explicitly performs `key.split('/')`. Therefore:

```text
"example/value"    -> .cache/v/example/value
"cache/lastfailed" -> .cache/v/cache/lastfailed
"plugin/a/b"       -> .cache/v/plugin/a/b
```

In other words, `/` is interpreted as a hierarchy separator. The fixture docstring's claim that keys must not contain `/` directly contradicts this implementation.

### 4.3 The `get` Method

```python
def get(self, key, default):
    """ return cached value for the given key.  If no value
    was yet cached or the value cannot be read, the specified
    default is returned.

    :param key: must be a ``/`` separated value. Usually the first
         name is the name of your plugin or your application.
    :param default: must be provided in case of a cache-miss or
         invalid cache values.
    """
    path = self._getvaluepath(key)
    if path.check():
        try:
            with path.open("r") as f:
                return json.load(f)
        except ValueError:
            self.trace("cache-invalid at %s" % (path,))
    return default
```

`get` first converts the slash-separated key into a path and then deserializes JSON from the corresponding file. If the file does not exist or contains invalid JSON, the method returns the caller-provided default value.

### 4.4 The `set` Method

```python
def set(self, key, value):
        """ save value for the given key.

    :param key: must be a ``/`` separated value. Usually the first
         name is the name of your plugin or your application.
    :param value: must be of any combination of basic
          python types, including nested types
          like e. g. lists of dictionaries.
    """
    path = self._getvaluepath(key)
    try:
        path.dirpath().ensure_dir()
    except (py.error.EEXIST, py.error.EACCES):
        self.config.warn(
            code='I9', message='could not create cache path %s' % (path,)
        )
        return
    try:
        f = path.open('w')
    except py.error.ENOTDIR:
        self.config.warn(
            code='I9', message='cache could not write path %s' % (path,))
    else:
        with f:
            self.trace("cache-write %s: %r" % (key, value,))
            json.dump(value, f, indent=2, sort_keys=True)
```

`set` likewise uses `_getvaluepath` to interpret `/`, creates any required intermediate directories, and then serializes the value as JSON.

## 5. An Important but Easy-to-Confuse API Distinction

The same `Cache` class also provides `makedir(name)`. For this API, the `name` argument **really must not contain path separators**:

```python
def makedir(self, name):
    """Return a directory path object with the given name.

    :param name: must be a string not containing a ``/`` separator.
    """
    if _sep in name or _altsep is not None and _altsep in name:
        raise ValueError("name is not allowed to contain path separators")
    return self._cachedir.ensure_dir("d", name)
```

The two contracts must therefore be distinguished:

| API | Input | Rule for `/` | Purpose |
|---|---|---|---|
| `Cache.get/set(key, ...)` | Logical value key | Allowed and used to define hierarchy | Store JSON values under `.cache/v/` |
| `Cache.makedir(name)` | A single directory name | Path separators are forbidden | Create a plugin directory under `.cache/d/` |

The fixture documentation describes `cache.get` and `cache.set`, but gives a no-slash constraint that applies only to `makedir`. This distinction is invisible if the fixture is examined in isolation; the implementations and contracts of multiple referenced methods must be compared.

## 6. Why the Documentation in a Single Snapshot Is Out of Sync

In commit `e9240f7e...`, the same fact about cache-key format appears in at least five independent locations:

| Synchronization State | Location and Entity | Original Text or Example |
|---|---|---|
| Incorrect | `_pytest/cacheprovider.py:187-200`, fixture `cache` | `Keys must be strings not containing a "/" separator.` |
| Incorrect | `doc/en/builtin.rst:76-85`, checked-in fixture reference | Also states that `/` is forbidden |
| Correct | `_pytest/cacheprovider.py:42-60`, `Cache.get` docstring | Key must be a `/`-separated value |
| Correct | `_pytest/cacheprovider.py:62-87`, `Cache.set` docstring | Key must be a `/`-separated value |
| Correct | `doc/en/cache.rst:156-172`, cache guide | Calls `get/set` with `"example/value"` |

This is not a comparison between older and newer versions of the documentation. These states coexist **within the same repository snapshot**: the fixture documentation and its checked-in RST copy had not yet been synchronized, while the method-level API documentation and usage guide were already consistent with the implementation.

## 7. Behavioral Tests Provide the Final Evidence

`testing/test_cache.py:73-86` uses a key containing `/` through the public fixture:

```python
def test_cachefuncarg(self, testdir):
    testdir.makepyfile("""
        import pytest
        def test_cachefuncarg(cache):
            val = cache.get("some/thing", None)
            assert val is None
            cache.set("some/thing", [1])
            val = cache.get("some/thing", [])
            assert val == [1]
    """)
    result = testdir.runpytest()
    assert result.ret == 0
    result.stdout.fnmatch_lines(["*1 passed*"])
```

This test rules out the interpretation that `_getvaluepath` may split on `/` internally while the public fixture still forbids users from supplying such keys. The test calls `get/set("some/thing", ...)` through the `cache` fixture itself and verifies that the value can be written and read back successfully.

Another test specifically checks that `makedir("key/name")` raises `ValueError`. Together, the two tests confirm that the slash rule depends on which API is being called rather than applying uniformly to the entire cache object.

## 8. What Did the Fix Change?

Commit `a808e092...` changed no executable code. It modified only the fixture docstring:

```diff
- Keys must be strings not containing a "/" separator. Add a unique identifier
- (such as plugin/app name) to avoid clashes with other cache users.
+ Keys must be a ``/`` separated value, where the first part is usually the
+ name of your plugin or application to avoid clashes with other cache users.
```

The implementation, the `get/set` docstrings, the tests, and the guide did not undergo corresponding behavioral changes. This shows that the commit corrected an existing documentation-code inconsistency rather than introducing a new cache behavior.



