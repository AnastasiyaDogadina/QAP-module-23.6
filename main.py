
from dotenv import load_dotenv
load_dotenv()
from app_modules.telegram_module import tgbot


if __name__ == "__main__":
    tgbot.start_bot()

