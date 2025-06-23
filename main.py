import os
import time
import argparse
from chat_with_gpt import get_response, set_system_prompt, reset_history
from speak_with_voicevox import speak_with_voicevox
from chat_log import append_chat_to_log

# system_prompt.txt が存在する場合は内容をシステムプロンプトとして設定
if os.path.exists("system_prompt.txt"):
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        file_prompt = f.read().strip()
        if file_prompt:
            set_system_prompt(file_prompt)


def show_typing_effect(text: str) -> None:
    """Write ``text`` to ``chat_output.txt`` one character at a time."""

    with open("chat_output.txt", "w", encoding="utf-8") as f:
        for ch in text:
            f.write(ch)
            f.flush()
            try:
                os.fsync(f.fileno())
            except OSError:
                pass
            time.sleep(0.05)


def chat_and_speak(prompt: str, *, speaker: int = 1, speed: float | None = None) -> None:
    """Send ``prompt`` to ChatGPT and speak the reply.

    Parameters
    ----------
    prompt:
        The user prompt to send to ChatGPT.
    speaker:
        VOICEVOX speaker ID passed to :func:`speak_with_voicevox`.
    speed:
        Optional speed scale forwarded to :func:`speak_with_voicevox`.
    """

    append_chat_to_log("user", prompt)
    response = get_response(prompt)
    append_chat_to_log("bot", response)
    print("ChatGPT:", response)

    # Show typing effect and update chat_output.txt
    show_typing_effect(response)

    # After the whole text is written start speaking
    speak_with_voicevox(response, speaker_id=speaker, speed=speed)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Chat with GPT and read responses aloud using VOICEVOX",
    )
    parser.add_argument(
        "--speaker",
        type=int,
        default=1,
        help="VOICEVOX speaker ID",
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=None,
        help="Speed scale for speech (1.0 is normal)",
    )
    args = parser.parse_args()

    system_prompt = input("システムプロンプトを入力してください (空でスキップ): ")
    if system_prompt:
        set_system_prompt(system_prompt)

    while True:
        user_input = input("あなた: ")
        lowered = user_input.lower()
        if lowered in {"exit", "quit"}:
            break
        if lowered == "!reset":
            reset_history()
            print("[履歴をリセットしました]")
            continue
        chat_and_speak(user_input, speaker=args.speaker, speed=args.speed)
