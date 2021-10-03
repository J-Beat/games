import logging
from typing import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import misc
from random import randint
from map_creator import MapCreator
import pictures as pc
from player import Player
from river import River
import os
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = misc.token

bot = Bot(token = token)
# Диспетчер для бота
dp = Dispatcher(bot, storage=storage)
greating = '''
Привет друг! Этот бот представляет собой упрощенную версию игры DND. 
Здесь тебе нужно будет передвигаться по карте с помощью стрелочек на клавиатуре внизу, также ты в любой момент можешь посмотреть на карту, нажав соответствующкю кнопку.
Если ты готов, нажимай кнопку и удачи!'''

# States
class Form(StatesGroup):
    map = State()
    position = State()
    player = State()
    location = State()


# mapsize = 30
#         map = MapCreator().creator(mapsize)
#         player = Player([randint(0, mapsize-1), randint(0, mapsize-1)], mapsize)
#         location = map[player.y][player.x]
#         pc.map_paint(map)


@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Поехали!")
    await message.reply(greating, reply_markup=markup)



@dp.message_handler(lambda message: message.text == 'Поехали!')
async def start_game(message: types.Message, state: FSMContext):
    mapsize = 10
    await Form.map.set()
    await state.update_data(u_map=MapCreator().creator(mapsize))
    # await Form.start_position.set()
    # await state.update_data(u_position=[randint(0, mapsize), randint(0, mapsize)])
    await Form.player.set()
    data = await state.get_data()
    await state.update_data(u_player=Player(data['u_map'], 'knight'))
    await Form.location.set()
    await state.update_data(u_location= [randint(0, mapsize), randint(0, mapsize)])
    pc.map_paint(data['u_map'])
    await state.reset_state(with_data=False)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sides = ['north', 'west', 'east', 'south', 'map']
    markup.add(*sides)
    await message.reply('В какую сторону пойдем?', reply_markup=markup)

@dp.message_handler(lambda message: message.text in ['north', 'west', 'east', 'south', 'map'])#
async def game(message: types.Message, state: FSMContext):
    # print(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sides = ['north', 'west', 'east', 'south', 'map']
    markup.add(*sides)
    action = message.text
    # data = await state.get_data()
    # print(data)
    if action  in ["north", 'west', 'east', 'south']:
        data = await state.get_data()
        position = data['u_player'].move(action, data['u_location'][0], data['u_location'][1])
        print('player_position -- ', position, data['u_location'][0], data['u_location'][1])

        if type(position) == list:
            await Form.location.set()
            await state.update_data(u_location= [position[-1][0], position[-1][1]])
            await Form.map.set()
            map = data['u_map']
            for pos in position:
                map[pos[0]][pos[1]].opened=True
            await state.update_data(u_map = map)
            pc.map_paint(data['u_map'])
            await state.reset_state(with_data=False)
            await message.answer(data['u_map'][position[-1][0]][position[-1][1]].description, reply_markup=markup)
        else:
            await message.answer('Вы не можете туда идти, там стена')
    elif action == 'map':
        photo = open("D:\Python\games\map.png", 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
	