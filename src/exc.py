from typing import Any
from aiogram.filters import BaseFilter
from aiogram import types, Bot 
from configparser import ConfigParser



class AdminException(BaseFilter):
    async def __call__(self, message: types.Message):
        config = ConfigParser()
        config.read('data.ini')
        admins = config.get('BOT', 'admin').split(',')
        user_id = message.from_user.id
        print(admins)
        if str(user_id) in admins:
            print(f"--------------------\nПользователь есть в базе данных!\nusername: @{message.from_user.username}\nfirst name, last name: {message.from_user.first_name}, {message.from_user.last_name if message.from_user.last_name else 'Фамилия отсутствует'}\n--------------------")
        return str(user_id) in admins and message.chat.type == 'private'
