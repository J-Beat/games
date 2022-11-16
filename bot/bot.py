import configparser as cnf
from typing import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.builtin import IDFilter
from aiogram.dispatcher.filters.builtin import ChatTypeFilter
import functions as func
from cam import get_photo
from PIL import Image


token, ID = func.get_token()
storage = MemoryStorage()
bot = Bot(token = token)
# Диспетчер для бота
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    nums = message.get_args()
    if message.from_id == int(ID):
        for i in range(int(nums)):
            get_photo('Photo_bot')
            # img = Image.open('g4g.png')
            photo = open('image/Photo_bot.jpg', 'rb')
            await message.answer_photo(photo, caption="caption") 



if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)