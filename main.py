import os
import time
from chat_with_gpt import get_response, set_system_prompt, reset_history
from speak_with_voicevox import speak_with_voicevox
from obsws_python import obsws, requests
from obs_utils import update_obs_text

# system_prompt.txt が存在する場合は内容をシステムプロンプトとして設定
if os.path.exists("system_prompt.txt"):
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        file_prompt = f.read().strip()
        if file_prompt:
            set_system_prompt(file_prompt)


def _update_obs_typing(text: str) -> None:
    """Update the ``ChatText`` source in OBS with ``text`` during typing."""

    try:
        ws = obsws("localhost", 4455, "yuki123")
        ws.connect()
        ws.call(
            requests.SetInputSettings(
                inputName="ChatText",
                inputSettings={"text": text},
                overlay=False,
            )
        )
        ws.disconnect()
    except Exception as e:  # pragma: no cover - OBS may not be running
        print(f"[OBS ERROR] {e}")

def chat_and_speak(prompt: str):
    response = get_response(prompt)
    with open("chat_output.txt", "w", encoding="utf-8") as f:
        f.write(response)
    print("ChatGPT:", response)

    # show typing effect in OBS
    typed = ""
    for ch in response:
        typed += ch
        _update_obs_typing(typed)
        time.sleep(0.05)

    speak_with_voicevox(response)
    # ensure the final text is set in OBS
    update_obs_text(response)

if __name__ == "__main__":
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
        chat_and_speak(user_input)
