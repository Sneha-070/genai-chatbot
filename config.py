import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-2.5-flash-lite"
    MAX_TOKENS = 800

print("API KEY LOADED:", Config.GEMINI_API_KEY)