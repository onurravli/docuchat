from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from colorama import Fore, Style, init

from lib.config import config


def create_vector_store(docs):
    init()
    if config["logging"]:
        print(f"{Fore.BLACK}Creating vector store...{Style.RESET_ALL}")
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    texts = []
    for doc in docs:
        texts.extend(text_splitter.split_text(doc))
    if config["logging"]:
        print(f"{Fore.GREEN}Vector store created successfully!{Style.RESET_ALL}")
        print(f"{Fore.BLACK}Loading embeddings model...{Style.RESET_ALL}")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(texts, embeddings)
    if config["logging"]:
        print(f"{Fore.GREEN}Embeddings model loaded successfully!{Style.RESET_ALL}")
    return vector_store
