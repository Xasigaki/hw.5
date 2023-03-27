
from aiogram import types


# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """Функция, которая обрабатывает команду /start"""
    # await message.answer("Привет")
    await message.reply("Я - добро пожаловать в книжний магазин!!!.")
    await message.delete()
    # with open('images/cat.jfif', 'rb') as img:
    #     await message.answer_photo(photo=img)


# @dp.message_handler(commands=["info"])
async def info(message: types.Message):
    """Ф-я которая обрабатывает команду info
    и отправляет юзеру его никнеймом"""
    await message.reply(f"Ты - {message.from_user.username}")


# @dp.message_handler()
# async def hello(message: types.Message):
#     """функция которая обрабатывает все сообщения
#     которые не подходдят под остальные фильтры"""
#     await message.answer("Привет")