## Portable Llama Chatbot

**Portable llama chatbot in USB drive.**

(It is only done for 64-bit Windows.)

- Very simple tech stack:
  - [Embeddable Python](https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip)
  - [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- No web server needed.
- It can run from USB drive. Plug and play.

## Quick start

- Git clone or download this repository.
- Download [Qwen3-4B-Q4_K_M.gguf](https://huggingface.co/Qwen/Qwen3-4B-GGUF/resolve/main/Qwen3-4B-Q4_K_M.gguf) and save it in `portable_llama_chatbot\models` folder.
- Run `chatbot_in_console.bat`.

## Build from scratch

- Make a folder `portable_llama_chatbot` and cd into it. It is the working directory.

  ```shell
  mkdir portable_llama_chatbot
  cd portable_llama_chatbot
  ```

- Make another 2 folders inside `portable_llama_chatbot`, `models` for model files, and `install` for temporary installation files.

  ```shell
  mkdir models
  mkdir install
  ```

- Download embeddable Python from https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip .

- Unzip it to folder `python-3.11.9-embed-amd64` which is inside `portable_llama_chatbot` folder.

- The embeddable Python does not come with pip. It has to be installed manually.
  Download the Python script from https://bootstrap.pypa.io/get-pip.py and save it as `portable_llama_chatbot\install\get-pip.py`.

- Install pip. The embeddable Python is not on system path. Run it with either full path or relative path.

  ```shell
  .\python-3.11.9-embed-amd64\python.exe install\get-pip.py
  ```

- Edit `.\python-3.11.9-embed-amd64\python311._pth` and replace its content with the text below:

  ```
  ..
  DLLs
  Lib/site-packages
  python311.zip 
  .

  # Uncomment to run site.main() automatically
  import site
  ```

- Install `llama-cpp-python`.

  - Install `scikit_build_core` which is required to build `llama-cpp-python`:

    ```shell
    .\python-3.11.9-embed-amd64\python.exe -m pip install scikit_build_core
    ```

  - Make sure Visual Studio C++ compiler and CMake are installed before building `llama-cpp-python`.

  - Install `llama-cpp-python`. It will take some time to build:

	```shell
	.\python-3.11.9-embed-amd64\python.exe -m pip install llama-cpp-python==0.3.9
	```

- Copy `llama_chatbot.py`, `chatbot_in_console.py` and `chatbot_in_console.bat` into `portable_llama_chatbot` folder.

- Download [Qwen3-4B-Q4_K_M.gguf](https://huggingface.co/Qwen/Qwen3-4B-GGUF/resolve/main/Qwen3-4B-Q4_K_M.gguf) and save it in `portable_llama_chatbot\models` folder.
  Any model that is supported by `llama-cpp-python` should work. Just need to modify `model_name` in `chatbot_in_console.py` script.

- Run `chatbot_in_console.bat` to use it.

- Refer to the documentation of [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) for customization.
