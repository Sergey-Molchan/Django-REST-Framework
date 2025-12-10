import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

print("=== Текущие настройки базы данных ===")
print(f"NAME: {os.getenv('NAME')}")
print(f"USER: {os.getenv('USER')}")
print(f"PASSWORD: {os.getenv('PASSWORD')}")
print(f"HOST: {os.getenv('HOST')}")
print(f"PORT: {os.getenv('PORT')}")
print(f"Текущий пользователь системы: {os.getenv('USERNAME')}")