import os
from typing import Dict, List

from dotenv import load_dotenv
from openai import OpenAI


# .env ファイルから環境変数を読み込む
load_dotenv()

# APIキーを環境変数から取得してクライアントを初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Conversation management -------------------------------------------------

_system_prompt: str = ""
_conversation_history: List[Dict[str, str]] = []


def set_system_prompt(prompt: str) -> None:
    """Set the system prompt and clear conversation history."""

    global _system_prompt, _conversation_history
    _system_prompt = prompt
    _conversation_history.clear()


def _build_messages(user_prompt: str) -> List[Dict[str, str]]:
    """Return the messages list to send to the OpenAI API."""

    messages: List[Dict[str, str]] = []
    if _system_prompt:
        messages.append({"role": "system", "content": _system_prompt})

    # Keep only the last 10 messages (combined user and assistant)
    messages.extend(_conversation_history[-10:])
    messages.append({"role": "user", "content": user_prompt})
    return messages


def _update_history(user_prompt: str, assistant_reply: str) -> None:
    """Append the latest conversation turn and trim to 10 messages."""

    _conversation_history.append({"role": "user", "content": user_prompt})
    _conversation_history.append({"role": "assistant", "content": assistant_reply})
    if len(_conversation_history) > 10:
        del _conversation_history[:-10]


def get_response(prompt: str) -> str:
    """Send ``prompt`` to the ChatGPT API and return the reply."""

    messages = _build_messages(prompt)
    response = client.chat.completions.create(
        model="gpt-4o",  # 他に gpt-4-turbo や gpt-3.5-turbo も可
        messages=messages,
        max_tokens=200,
    )
    reply = response.choices[0].message.content.strip()
    _update_history(prompt, reply)
    return reply

if __name__ == "__main__":
    prompt = input("ユーザーの発言: ")
    reply = get_response(prompt)

    # OBSで表示する用のテキストファイルに書き出す
    with open("chat_output.txt", "w", encoding="utf-8") as f:
        f.write(reply)

    print("ChatGPTの返答:", reply)
