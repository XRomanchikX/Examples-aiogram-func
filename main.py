# import logging                            ### DEBUG ###
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
# from handler import *                     ### ФАЙЛ С КОМАНДАМИ ###

async def start():
    # logging.basicConfig(level=logging.INFO, format="%(asctime)s") ### DEBUG ###
    bot = Bot(token=" TOKEN ", parse_mode='HTML')
    dp = Dispatcher()

    ### COMMANDS ###

    # dp.message.register(example, Command(commands=["command_name"]))           # with use command
    # dp.message.register(example, F.data == "text")                             # with use any text

    # dp.callback_query.register(example, F.data.startswith("text_"))            # with use callback_query с нескольким вариантом выбора
    # dp.callback_query.register(example, F.data == "text")                      # with use callback_query с одним вариантом выбора

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())