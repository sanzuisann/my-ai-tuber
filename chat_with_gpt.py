import os
from openai import OpenAI
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込む
load_dotenv()

# APIキーを環境変数から取得してクライアントを初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",  # 他に gpt-4-turbo や gpt-3.5-turbo も可
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    prompt = input("ユーザーの発言: ")
    reply = get_response(prompt)

    # OBSで表示する用のテキストファイルに書き出す
    with open("chat_output.txt", "w", encoding="utf-8") as f:
        f.write(reply)

    print("ChatGPTの返答:", reply)
