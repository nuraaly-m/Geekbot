from aiogram import Router, F, types
from aiogram.filters import Command


menu_router = Router()

@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='горячие блюда'),
                types.KeyboardButton(text='холодные блюда')
            ],
            [
                types.KeyboardButton(text='салаты'),
                types.KeyboardButton(text='напитки')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('выберите блюдо', reply_markup=kb)


@menu_router.message(F.text.lower() == 'горячие блюда')
async def menu(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    print(message.text)
    await message.answer('наши горячие блюда', reply_markup=kb)


@menu_router.message(F.text.lower() == 'холодные блюда')
async def menu(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    print(message.text)
    await message.answer('наши холодные блюда', reply_markup=kb)


@menu_router.message(F.text.lower() == 'напитки')
async def menu(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    print(message.text)
    await message.answer('наши напитки', reply_markup=kb)


@menu_router.message(F.text.lower() == 'салаты')
async def menu(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    print(message.text)
    await message.answer('наши салаты', reply_markup=kb)