import requests
import simpleaudio as sa
import os

text = "こんにちは、VOICEVOXです。"
speaker_id = 1
wav_file = "output.wav"

# クエリ生成
print("🎙 クエリ生成中...")
query_response = requests.post(
    "http://127.0.0.1:50021/audio_query",
    params={"text": text, "speaker": speaker_id}
)

if query_response.status_code != 200:
    print("❌ audio_query に失敗しました")
    exit()

query = query_response.json()

# 音声合成
print("🎧 音声合成中...")
synthesis_response = requests.post(
    "http://127.0.0.1:50021/synthesis",
    params={"speaker": speaker_id},
    json=query
)

if synthesis_response.status_code != 200:
    print("❌ synthesis に失敗しました")
    exit()

audio = synthesis_response.content

# ファイル保存
with open(wav_file, "wb") as f:
    f.write(audio)

print(f"✅ 音声ファイル保存完了: {wav_file}")

# ファイル再生
if os.path.exists(wav_file):
    print("🔊 音声を再生します...")
    wave_obj = sa.WaveObject.from_wave_file(wav_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    print("✅ 再生完了")
else:
    print("❌ 音声ファイルが存在しません")
