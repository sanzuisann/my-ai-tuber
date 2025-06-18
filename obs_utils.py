"""Utilities for interacting with OBS via obs-websocket."""

from __future__ import annotations

from obsws_python import obsws, requests


_OBS_HOST = "localhost"
_OBS_PORT = 4455
_OBS_PASSWORD = "yuki123"


def update_obs_text(text: str) -> None:
    """Update the ``ChatText`` source in OBS with ``text``.

    The function connects to OBS, sends the update request, and then
    disconnects. If the connection fails, the error is printed and
    silently ignored.
    """

    ws = obsws(_OBS_HOST, _OBS_PORT, _OBS_PASSWORD)
    try:
        ws.connect()
        ws.call(
            requests.SetInputSettings(
                inputName="ChatText",
                inputSettings={"text": text},
                overlay=False,
            )
        )
    except Exception as e:  # pragma: no cover - OBS may not be running
        print(f"[OBS ERROR] {e}")
    finally:
        try:
            ws.disconnect()
        except Exception:
            pass

