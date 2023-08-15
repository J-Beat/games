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

buttons_list = func.get_all_buttons(texts['keyboards'])

@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    print(message.get_args())
    await message.answer(texts['main_page']['main_greating'], reply_markup=kb.main_keybord)


@dp.message_handler(NotCommandFilter(buttons_list), ChatTypeFilter(chat_type = 'private'))
async def regexp_example(message: types.Message):
    # await message.answer('Хочешь менеджерам написать? (Заглушка)')
    await message.forward("-886375390", message.text)

@dp.message_handler(IDFilter(chat_id = "-886375390"))
async def start(message: types.Message):
    await bot.send_message(message.reply_to_message.forward_from.id, message.text)

@dp.message_handler(filters.Text(equals= texts['keyboards']['main_menu']['site']))
async def process_callback_site(message: types.Message):
    await message.answer(texts['main_page']['main_site'], reply_markup=kb.site_channek_link_keyboard)

@dp.message_handler(filters.Text(equals= texts['keyboards']['main_menu']['about']))
async def process_callback_site(message: types.Message):
    await message.answer(texts['main_page']['main_about'])

@dp.message_handler(CommandFilter([texts['keyboards']['main_menu']['price'], texts['keyboards']['main_menu']['subscribe']]))
async def process_callback_site(message: types.Message):
    await message.answer(texts['main_page']['price_subscribe'], reply_markup=kb.price_subscribe_link_keyboard)

@dp.message_handler(filters.Text(equals= texts['keyboards']['main_menu']['faq']))
async def process_callback_site(message: types.Message):
    await message.answer(texts['knowlege_base']['main'], reply_markup=kb.base_knowlege_keyboard)

@dp.message_handler(filters.Text(equals= texts['keyboards']['faq']['main']['faq']))
async def process_callback_site(message: types.Message):
    await message.answer(texts['FAQ']['main'], reply_markup=kb.faq_keyboard)

@dp.message_handler(filters.Text(equals= texts['keyboards']['faq']['main']['back_to_main']))
async def process_callback_site(message: types.Message):
    await message.answer('🔙 В главное меню', reply_markup=kb.main_keybord)
    await message.delete()

@dp.message_handler(CommandFilter(texts['keyboards']['faq']['faq'].values()))
async def process_callback_site(message: types.Message):
    await message.answer(texts['auto_reply'])

@dp.message_handler(filters.Text(equals= texts['keyboards']['main_menu']['question']))
async def process_callback_site(message: types.Message):
    await message.answer(texts['main_page']['main_question'])

@dp.message_handler(filters.Text(equals= texts['keyboards']['faq']['main']['functional']))
async def process_callback_site(message: types.Message):
    await message.answer(texts['knowlege_base']['general_func_main'], reply_markup= kb.base_knowlege_pages_keyboard)

@dp.message_handler(CommandFilter(list(texts['keyboards']['faq']['functional'].values())[:3]))
async def process_callback_site(message: types.Message):
    if message.text == texts['keyboards']['faq']['functional']['main']:
        await message.answer(texts['knowlege_base']['service_pages']['main'])
    elif message.text == texts['keyboards']['faq']['functional']['search']:
        await message.answer(texts['knowlege_base']['service_pages']['search'])
    elif message.text == texts['keyboards']['faq']['functional']['brands']:
        await message.answer(texts['knowlege_base']['service_pages']['brands'])







if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)