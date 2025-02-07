import os
from tqdm import tqdm
from colorama import Fore, Style, init

from lib.pdf.load_pdf_text import load_pdf_text
from lib.config import config


def load_documents_from_pdfs(pdf_dir="pdfs"):
    # Initialize colorama for Windows compatibility
    init()

    docs = []
    if not os.path.exists(pdf_dir):
        if config["logging"]:
            print(
                f"{Fore.RED}Directory '{pdf_dir}' not found. Please create it and add your PDF files.{Style.RESET_ALL}"
            )
        return docs

    # Get list of PDF files first
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        if config["logging"]:
            print(f"{Fore.RED}No PDF files found in the directory.{Style.RESET_ALL}")
        exit(1)

    if config["logging"]:
        print(
            f"{Fore.BLACK}Found {len(pdf_files)} PDF files to process...{Style.RESET_ALL}"
        )

    if config["logging"]:
        for filename in tqdm(
            pdf_files,
            desc=f"{Fore.BLACK}Loading PDFs{Style.RESET_ALL}",
            unit="file",
            ncols=80,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
        ):
            pdf_path = os.path.join(pdf_dir, filename)
            text = load_pdf_text(pdf_path)
            if text:
                docs.append(text)
    else:
        for filename in pdf_files:
            pdf_path = os.path.join(pdf_dir, filename)
            text = load_pdf_text(pdf_path)
            if text:
                docs.append(text)

    if not docs:
        if config["logging"]:
            print(
                f"{Fore.RED}No PDFs were loaded. Check if your PDFs contain extractable text.{Style.RESET_ALL}"
            )
        exit(1)
    if config["logging"]:
        print(
            f"{Fore.GREEN}Successfully loaded {Fore.CYAN}{len(docs)}{Fore.GREEN} documents!{Style.RESET_ALL}"
        )
    return docs
