from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def admin_panel(message: types.Message, bot: Bot):
    btn = [
        [KeyboardButton(text='Отправить опрос')],
    ]
    key = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=btn)
    await message.answer('Здравствуйте, Админ. Выберите действие: ', reply_markup=key)
    







