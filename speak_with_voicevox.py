import requests
import soundfile as sf
import simpleaudio as sa

# 音声化したいテキストを取得（ファイルからでもOK）
with open("chat_output.txt", "r", encoding="utf-8") as f:
    text = f.read()

# VOICEVOX設定
speaker_id = 1  # 例：四国めたん（ノーマル）
host = "http://127.0.0.1:50021"

# 1. 音声合成用クエリ作成
query = requests.post(
    f"{host}/audio_query",
    params={"text": text, "speaker": speaker_id}
)
query.raise_for_status()
audio_query = query.json()

# 2. 音声データ生成
synthesis = requests.post(
    f"{host}/synthesis",
    params={"speaker": speaker_id},
    json=audio_query
)
synthesis.raise_for_status()

# 3. 音声データを再生
audio_data = synthesis.content
with open("output.wav", "wb") as f:
    f.write(audio_data)

data, samplerate = sf.read("output.wav")
sa.play_buffer((data * 32767).astype("int16"), 1, 2, samplerate).wait_done()
