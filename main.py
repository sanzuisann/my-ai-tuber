import os
from chat_with_gpt import get_response, set_system_prompt
from speak_with_voicevox import speak_with_voicevox

# system_prompt.txt が存在する場合は内容をシステムプロンプトとして設定
if os.path.exists("system_prompt.txt"):
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        file_prompt = f.read().strip()
        if file_prompt:
            set_system_prompt(file_prompt)

def chat_and_speak(prompt: str):
    response = get_response(prompt)
    with open("chat_output.txt", "w", encoding="utf-8") as f:
        f.write(response)
    print("ChatGPT:", response)
    speak_with_voicevox(response)

if __name__ == "__main__":
    system_prompt = input("システムプロンプトを入力してください (空でスキップ): ")
    if system_prompt:
        set_system_prompt(system_prompt)

    while True:
        user_input = input("あなた: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        chat_and_speak(user_input)
