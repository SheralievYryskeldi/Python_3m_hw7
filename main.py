from aiogram import executor
from bot_instance import dp

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)