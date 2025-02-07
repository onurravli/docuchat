import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Chat with your PDFs using a local LLM."
    )
    parser.add_argument(
        "--model",
        type=str,
        default="llama3.2",
        help="Ollama model name to use (default: llama3.2)",
    )
    parser.add_argument(
        "--logging",
        action="store_true",
        help="Enable logging (default: False)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Enable quiet mode (default: False)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Temperature for the LLM (default: 0.7)",
    )
    parser.add_argument(
        "--streaming",
        action="store_true",
        help="Enable streaming (default: True)",
    )
    args = parser.parse_args()
    return args
