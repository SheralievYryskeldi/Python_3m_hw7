from aiogram import executor
from bot_instance import dp
from handlers import inline

inline.register_inline_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)