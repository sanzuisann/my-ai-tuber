import os
from dotenv import load_dotenv
from openai import OpenAI

# .envからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAIクライアントを作成
client = OpenAI(api_key=api_key)

# ChatGPTに問い合わせ（GPT-4oモデル使用）
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "あなたは明るく元気なVTuberのAIキャラクターです。"},
        {"role": "user", "content": "こんにちは！今日のおすすめトピックは？"}
    ]
)

# 応答を表示
print(response.choices[0].message.content)
