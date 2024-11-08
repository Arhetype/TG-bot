import os

from dotenv import load_dotenv
from pathlib import Path


def getTgToken() -> str:
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    token = os.getenv("TG_TOKEN")
    return token


