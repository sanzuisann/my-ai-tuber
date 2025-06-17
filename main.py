from chat_with_gpt import get_response
from speak_with_voicevox import speak_with_voicevox

def chat_and_speak(prompt: str):
    response = get_response(prompt)
    print("ChatGPT:", response)
    speak_with_voicevox(response)

if __name__ == "__main__":
    while True:
        user_input = input("あなた: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        chat_and_speak(user_input)
