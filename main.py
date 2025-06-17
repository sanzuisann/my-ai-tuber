from chat_with_gpt import get_response, set_system_prompt
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
        if user_input.lower() in {"exit", "quit"}:
            break
        chat_and_speak(user_input)
