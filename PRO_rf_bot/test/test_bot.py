import configparser as cnf
from typing import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.builtin import IDFilter
from aiogram.dispatcher.filters.builtin import ChatTypeFilter
import keyboards_2 as kb
import functions as func
from bot_filters import CommandFilter, NotCommandFilter



token = func.get_token()
storage = MemoryStorage()
bot = Bot(token = token)
texts = func.get_texts()
# Диспетчер для бота
dp = Dispatcher(bot, storage=storage)