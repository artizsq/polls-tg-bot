import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
import asyncio
from src.poll import poll_message
from src.admin.rega import admin_panel
from src.exc import AdminException
from configparser import ConfigParser

logging.basicConfig(level=logging.INFO)


async def start_bot():
    config = ConfigParser()
    config.read('data.ini')

    # Здесь нужно указать ваш TOKEN и CHAT_ID
    TOKEN = config.get('BOT', 'token')
    ADMINS = config.get('BOT', 'admin').split()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.message.register(poll_message, F.text == "Отправить опрос", AdminException())
    dp.message.register(admin_panel, Command("panel"), AdminException())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())