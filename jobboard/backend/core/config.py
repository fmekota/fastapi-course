import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / "jobboard/backend/.env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE:  str = "Jobboard"
    PROJECT_VERSION:    str = "0.1.1"

    POSTGRES_USER:  str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD:   str = "aab44ke3Yd4bONgE"
    POSTGRES_SERVER:    str = "34.91.227.127"
    POSTGRES_PORT:  str = "5432"
    POSTGRES_DB:    str = "fmekota"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()