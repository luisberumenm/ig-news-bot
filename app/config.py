from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
ENVIRONMENT = os.getenv("ENVIRONMENT")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")