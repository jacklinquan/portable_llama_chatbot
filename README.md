# Portable Llama Chatbot

**Portable llama chatbot in USB drive.**

(It is only done for 64-bit Windows.)

- Very simple tech stack:
  - Embedded Python
  - [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- No web server needed.
- It can run from USB drive. Plug and play.

## Quick start

- Download [portable_llama_chatbot.zip](https://github.com/jacklinquan/portable_llama_chatbot/raw/main/portable_llama_chatbot.zip) and unzip it.
- Download [qwen2-1_5b-instruct-q4_0.gguf](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct-GGUF/resolve/main/qwen2-1_5b-instruct-q4_0.gguf) and save it in `portable_llama_chatbot\models` folder.
- Run `chatbot_in_console.bat`.
