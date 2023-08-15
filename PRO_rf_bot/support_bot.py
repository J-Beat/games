import configparser as cnf
from typing import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import IDFilter
from aiogram.dispatcher.filters.builtin import ChatTypeFilter
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import keyboards as kb
import texts as tx

configPath = '/home/ivan/Projects/git/games/PRO_rf_bot/config/config.ini'
config = cnf.ConfigParser()  # создаём объекта парсера
config.read(configPath)
token = config['TOKEN']['SUPPORT_TOKEN']
print(token)

bot = Bot(token = token)
# Диспетчер для бота
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    args = message.get_args()
    if args == 'subscribe':
        await message.answer('Здесь Вам помогут оформить подписку! Вы можете оформить подписку перейдя на сайт -  Продажи.рф в раздел подписки или задать свой вопрос здесь.', reply_markup=kb.support_subscribe_keyboard)
    if not args:
        await message.answer(tx.support_greating, reply_markup=kb.support_main_keyboard)

@dp.message_handler(ChatTypeFilter(chat_type = 'private'))
async def start(message: types.Message):
    await message.forward("-886375390", message.text)
    # await bot.send_message("-886375390", message.text)


@dp.message_handler(IDFilter(chat_id = "-886375390"))
async def start(message: types.Message):
    await bot.send_message(message.reply_to_message.forward_from.id, message.text)
    # reply_to_message.forward_from.id


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)