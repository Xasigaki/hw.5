from aiogram import types
from db.base import get_products

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(
    types.KeyboardButton("Книги"),
    types.KeyboardButton("Кружки")
)


def keyboard(product_id: int):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("Купить", callback_data=f"buy_product_{product_id}"))
    return kb


async def show_categories(message: types.Message):
    await message.reply("Наши товары", reply_markup=kb)


async def show_category_books(message: types.Message):
    await message.answer("Наши книги:")
    books = get_products()
    for book in books:
        await message.answer(book[1], reply_markup=keyboard(book[0]))


async def show_book(callback: types.CallbackQuery):
    await callback.message.answer("Это инфо о самой интересной книге")