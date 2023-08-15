from aiogram.dispatcher.filters import BoundFilter
from aiogram import Bot, Dispatcher, executor, types

class NotCommandFilter(BoundFilter):
    def __init__(self, buttons_list: list) -> None:
        self.buttons_list = buttons_list

    async def check(self, message: types.Message) -> bool:
        return message.text not in self.buttons_list


class CommandFilter(BoundFilter):
    def __init__(self, buttons_list: list) -> None:
        self.buttons_list = buttons_list

    async def check(self, message: types.Message) -> bool:
        return message.text in self.buttons_list