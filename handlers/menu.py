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


dishes = ['горячие блюда', 'холодные блюда', 'салаты', 'напитки']


@menu_router.message(F.text.lower().in_(dishes))
async def show_menu(message: types.Message):
    dish = message.text.lower()
    print(dish)
    kb = types.ReplyKeyboardRemove()
    await message.answer(f'все наши {dish}', reply_markup=kb)
