from bot_telegram import bot
from aiogram import Dispatcher, types

from keyboards.kb_client import menu


# from bot_telegram import ADMIN_ID


# @dp.message_handler(commands=['start'], state='*')
async def cmd_Start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)

    # kb.row(*keyboard_menu["Меню настроек"])
    # kb.row(*keyboard_menu["Прочее"])

    kb.row(menu["Настройки"])

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вступительный текст[ТУТ ССЫЛКА?]'
                                '(https://telegra.ph/Moyo-video-o-tom-chem-my-segodnya-budem-zanimatsya-11-06)',
                           reply_markup=kb)


# @dp.callback_query_handlers(text='MenuSetting', state='*')
async def cb_products(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(menu["Информация"])

    await callback.message.edit_text('Настройте стратегию для сортировки[ ](https://goo.su/VKUr)', reply_markup=kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_Start, commands=["start"])
    dp.register_callback_query_handler(cb_Setting, text='MenuSetting')


