> [!NOTE]  
> Still under development! The code is a bit spaghetti-ish right now (we've all been there 🍝), but, it works! Feel free to contribute and help make it better!

## DocuChat

Chat with your PDFs using a local LLM.

### Get Started

1. Clone the repository

```bash
git clone https://github.com/onurravli/docuchat.git
```

2. Install the dependencies

```bash
pip install -r requirements.txt

# or

uv sync
```

3. Create `pdfs` directory in the root of the project

```bash
mkdir pdfs
```

4. Add your PDFs to the `pdfs` directory

5. Start the chat

```bash
python main.py
```

### Usage

```bash
usage: main.py [-h] [--model MODEL] [--logging] [--quiet] [--temperature TEMPERATURE] [--streaming]

Chat with your PDFs using a local LLM.

options:
  -h, --help            show this help message and exit
  --model MODEL         Ollama model name to use (default: llama3.2)
  --logging             Enable logging (default: False)
  --quiet               Enable quiet mode (default: False)
  --temperature TEMPERATURE
                        Temperature for the LLM (default: 0.7)
  --streaming           Enable streaming (default: True)
```

### License

This project is licensed under the MIT License. See the [LICENSE.md](./LICENSE.md) file for details.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### Acknowledgements

- [Ollama](https://ollama.com/)
- [LangChain](https://langchain.com/)
- [LangChain-Ollama](https://github.com/ollama/langchain-ollama)
- [LangChain-HuggingFace](https://github.com/huggingface/langchain-huggingface)
- [LangChain-Community](https://github.com/langchain-ai/langchain-community)

### **Disclaimer**

> [!CAUTION]
> This project is not affiliated with Ollama or LangChain. I don't accept any responsibility for the use of this project, generated content or any other content.
