from aiogram import types

setting = types.InlineKeyboardButton('Наши лаки️', callback_data='MenuSetting')
information = types.InlineKeyboardButton('О нас ℹ️', callback_data='Information')
payment = types.InlineKeyboardButton('Оплатить 💳', callback_data='Payment')

menu = {
    'Настройки': setting,
    'Информация': information,
    'Оплата': payment
}
