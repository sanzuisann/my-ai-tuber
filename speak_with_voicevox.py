"""Utility for synthesising speech using a local VOICEVOX server."""

from __future__ import annotations

import requests
import soundfile as sf
import simpleaudio as sa


def speak_with_voicevox(
    text: str,
    *,
    speaker_id: int = 1,
    host: str = "http://127.0.0.1:50021",
) -> None:
    """Synthesis ``text`` with VOICEVOX and play the resulting audio.

    Parameters
    ----------
    text:
        The text to be converted into speech.
    speaker_id:
        Identifier of the VOICEVOX speaker. ``1`` corresponds to 四国めたん.
    host:
        VOICEVOX engine host URL.
    """

    # 1. 音声合成用クエリ作成
    query_response = requests.post(
        f"{host}/audio_query", params={"text": text, "speaker": speaker_id}
    )
    query_response.raise_for_status()
    audio_query = query_response.json()

    # 2. 音声データ生成
    synthesis_response = requests.post(
        f"{host}/synthesis",
        params={"speaker": speaker_id},
        json=audio_query,
    )
    synthesis_response.raise_for_status()

    # 3. 音声データを再生
    audio_data = synthesis_response.content
    output_file = "output.wav"
    with open(output_file, "wb") as f:
        f.write(audio_data)

    data, samplerate = sf.read(output_file)
    sa.play_buffer((data * 32767).astype("int16"), 1, 2, samplerate).wait_done()


if __name__ == "__main__":  # pragma: no cover - manual testing entry point
    with open("chat_output.txt", "r", encoding="utf-8") as f:
        text = f.read().strip()

    speak_with_voicevox(text)
