from aiogram import types, Router, F
from aiogram.filters import Command
from keyboard import start_keyboard


start_router = Router()


users = []
@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    if message.from_user.id not in users:
        users.append(message.from_user.id)
    await message.answer(f'salam! {message.from_user.first_name},'
                         f' we serve {len(users)} users',
                         reply_markup=start_keyboard())


@start_router.callback_query(F.data == 'меню')
async def menu(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.answer('наше меню')


@start_router.callback_query(F.data == 'отзывы')
async def feedbacks(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.answer('наши отзывы')


@start_router.callback_query(F.data == 'contacts')
async def contacts(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.answer('0777 777 777')

