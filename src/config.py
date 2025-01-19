import os
from dotenv import load_dotenv

load_dotenv()

def get_env_or_raise(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set")
    return value

DATABASE_URL = get_env_or_raise("DATABASE_URL")
TG_API=get_env_or_raise("TG_API")