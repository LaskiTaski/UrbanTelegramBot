from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from aiogram import Bot
import os

load_dotenv()

TOKEN = os.getenv('TOKEN_API')
ADMIN_ID = os.getenv('ADMIN_ID')

bot = Bot(token=TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot)
