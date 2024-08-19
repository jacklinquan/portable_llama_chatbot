import os
from pathlib import Path
import asyncio

from llama_cpp import Llama

from llama_chatbot import (
    run_console_chatbot,
    run_thread_chatbot_in_console,
    run_async_thread_chatbot_in_console,
)


def main():
    os.system("cls")

    # https://huggingface.co/Qwen/Qwen2-1.5B-Instruct-GGUF/resolve/main/qwen2-1_5b-instruct-q4_k_m.gguf
    model_name = "qwen2-1_5b-instruct-q4_k_m.gguf"
    chat_format = "qwen"

    # https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
    # model_name = "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    # chat_format = "llama-3"

    model_folder_name = "models"
    model_path = Path(__file__).parent / model_folder_name / model_name

    model = Llama(
        model_path=str(model_path),
        n_ctx=8192,
        chat_format=chat_format,
        verbose=False,
    )

    system_prompt = "You are a helpful assistant."

    # Console chatbot
    run_console_chatbot(model, system_prompt)

    # Thread chatbot in console
    # run_thread_chatbot_in_console(model, system_prompt)

    # Async thread chatbot in console
    # asyncio.run(run_async_thread_chatbot_in_console(model, system_prompt))


if __name__ == "__main__":
    main()
