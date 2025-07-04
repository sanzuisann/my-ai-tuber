# My AI Tuber

This project chats with GPT and reads the response aloud using VOICEVOX.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the repository root and set your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
3. Start the VOICEVOX engine so that it listens on `http://127.0.0.1:50021`.

## Usage

Run the main script:
```bash
python main.py
```
You can optionally pass a VOICEVOX speaker ID and speaking speed:
```bash
python main.py --speaker 8 --speed 1.2
```
If a `system_prompt.txt` file exists in the repository root, its contents will
be used as the system prompt automatically. You'll still be prompted for an
optional system prompt when the script starts, which can override the file
contents.
After that, type your prompt. The last 10 messages are kept as context and
the reply from ChatGPT will be spoken aloud. Each response is limited to
200 tokens.

### Adjusting speaking speed

You can change how fast the audio is spoken by passing a ``speed`` value to
``speak_with_voicevox``. For example, ``speed=1.2`` will speak about 20% faster:

```python
from speak_with_voicevox import speak_with_voicevox

speak_with_voicevox("こんにちは", speed=1.2)
```


### Selecting a voice

Each VOICEVOX voice is identified by a `speaker_id`. Pass this value to
`speak_with_voicevox` to choose which speaker to use:

```python
speak_with_voicevox("text", speaker_id=8)
```
