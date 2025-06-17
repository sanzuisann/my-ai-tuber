from chat_with_gpt import get_response, set_system_prompt, clear_history
from speak_with_voicevox import speak_with_voicevox

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
        command = user_input.lower()
        if command in {"exit", "quit"}:
            break
        if command == "reset":
            clear_history()
            print("会話履歴をリセットしました")
            continue
        chat_and_speak(user_input)
