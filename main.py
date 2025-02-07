from lib.model.check_model import check_model, get_installed_models
from lib.helpers.exit_gracefully import exit_gracefully
from lib.pdf.load_documents_from_pdfs import load_documents_from_pdfs
from lib.vector.create_vector_store import create_vector_store
from lib.core.start_chat import start_chat
from lib.core.parse_args import parse_args
from colorama import Fore, Style, init
from lib.config import config
from lib.helpers.print_logo import print_logo

if __name__ == "__main__":
    if not config["quiet"]:
        print_logo()
    init()
    args = parse_args()
    model = args.model
    if not check_model(model):
        print(
            f"{Fore.RED}Model {Fore.YELLOW}{model}{Fore.RED} is not installed. "
            f"Please install it first by running {Fore.CYAN}`ollama pull {model}`{Style.RESET_ALL}"
        )
        installed_models = get_installed_models()
        print(
            f"{Fore.GREEN}Installed models: {Fore.CYAN}{installed_models}{Style.RESET_ALL}"
        )
        exit(1)
    docs = load_documents_from_pdfs()
    if not docs:
        print(f"{Fore.RED}No documents loaded. Exiting.{Style.RESET_ALL}")
        exit(1)
    try:
        vector_store = create_vector_store(docs)
        start_chat(
            vector_store,
            model_name=model,
            temperature=config["temperature"],
            streaming=config["streaming"],
        )
    except (KeyboardInterrupt, EOFError):
        exit_gracefully()
