# My AI Tuber

This project chats with GPT and reads the response aloud using VOICEVOX.

## Setup

1. Install dependencies (``obsws-python`` is now required):
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the repository root and set your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
3. Start the VOICEVOX engine so that it listens on `http://127.0.0.1:50021`.
4. Prepare OBS with the obs-websocket plugin enabled on port ``4455`` and
   password ``yuki123``. The text source that displays replies must be named
   ``ChatText``.

## Usage

Run the main script:
```bash
python main.py
```
If a `system_prompt.txt` file exists in the repository root, its contents will
be used as the system prompt automatically. You'll still be prompted for an
optional system prompt when the script starts, which can override the file
contents.
After that, type your prompt. The last 10 messages are kept as context and
the reply from ChatGPT will be spoken aloud. Each response is limited to
200 tokens.
Responses will also appear sequentially in OBS.
