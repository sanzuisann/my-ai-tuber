"""Chat logging helper functions."""

from __future__ import annotations


def append_chat_to_log(role: str, message: str, path: str = "chat_log.txt") -> None:
    """Append a chat ``message`` with ``role`` to ``path``.

    Parameters
    ----------
    role:
        Role name, e.g. ``"user"`` or ``"bot"``.
    message:
        Chat message to log.
    path:
        Log file path relative to the current working directory. Defaults to
        ``"chat_log.txt"`` in the repository root.
    """

    line = f"{role}::{message}\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(line)
