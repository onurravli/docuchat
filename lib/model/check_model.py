import subprocess
from colorama import Fore, Style, init


def get_installed_models():
    init()
    try:
        result = subprocess.check_output(["ollama", "list"], stderr=subprocess.STDOUT)
        models_output = result.decode("utf-8")
        models = [
            line.split()[0] for line in models_output.splitlines()[1:] if line.strip()
        ]
        return models
    except Exception as e:
        print(f"{Fore.RED}Error running 'ollama list': {e}{Style.RESET_ALL}")
        return []


def check_model(model_name):
    models = get_installed_models()
    for model in models:
        if model_name in model:
            return True
    return False
