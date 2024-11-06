from aiogram.utils import executor
from bot_telegram import dp

from handlers.Client import register_handlers_client, register_handlers_admin

register_handlers_client(dp)
register_handlers_admin(dp)

async def on_start_up(_):
    print('Start telegram bot')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
