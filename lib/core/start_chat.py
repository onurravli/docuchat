from langchain_ollama import OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from lib.helpers.exit_gracefully import exit_gracefully
from colorama import Fore, Style, init
from lib.config import config
from lib.helpers.print_logo import print_logo
import readline
import os

APP_NAME = "DocuChat"
APP_VERSION = "0.1.0"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def start_chat(vector_store, model_name, temperature, streaming):
    init()
    # Set up readline to handle Control-L
    readline.parse_and_bind('"\C-l": clear-screen')

    retriever = vector_store.as_retriever(search_kwargs={"k": 2})
    local_ollama = OllamaLLM(
        model=model_name, temperature=temperature, streaming=streaming
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=local_ollama,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
    )
    if config["logging"]:
        print("")
    print(
        f"{Fore.CYAN}Welcome to {Fore.GREEN}{APP_NAME}{Fore.CYAN}! Type '{Fore.YELLOW}quit{Fore.CYAN}' to exit. \
{Fore.BLACK}Version: {APP_VERSION}, Model: {model_name}{Style.RESET_ALL}"
    )
    while True:
        try:
            query = input(f"\n{Fore.GREEN}You: {Style.RESET_ALL}")
            if query.lower() in ["exit", "quit"]:
                exit_gracefully()
            print(f"{Fore.BLUE}AI: {Style.RESET_ALL}", end="", flush=True)
            qa_chain.invoke(
                {"query": query}, {"callbacks": [StreamingStdOutCallbackHandler()]}
            )
            print()
        except KeyboardInterrupt:
            print("\n")
            continue
