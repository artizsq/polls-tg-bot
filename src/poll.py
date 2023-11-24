from aiogram import Bot, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import configparser

async def poll_message(message: types.Message, bot: Bot):
    config = configparser.ConfigParser()
    config.read('data.ini')
    CHAT_ID = config.getint('CHAT', 'id')
    question = 'Кто как ел?'
    options = ['Полностью', 'Без салата', 'Не ел', 'Оплатил']
    try:
        message.answer("Опрос создан!")
        await bot.send_poll(chat_id=CHAT_ID, question=question, options=options, is_anonymous=False)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")