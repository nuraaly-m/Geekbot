from aiogram import Router, F, types
from aiogram.filters import Command
from config import database

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


kinds = ['горячие блюда', 'холодные блюда', 'салаты', 'напитки']


@menu_router.message(F.text.lower().in_(kinds))
async def show_menu(message: types.Message):
    kind = message.text.lower()
    print(kind)
    kb = types.ReplyKeyboardRemove()
    data = await database.fetch(
        """
        SELECT products.* FROM products
        JOIN kinds ON products.kind_id = kinds.id
        WHERE kinds.name = ?
        """,
        (kind,),
        fetch_type='all'
    )
    if not data:
        await message.answer('по вашему заапросу ничего не найдено', reply_markup=kb)
        await message.answer(f'все наши {kind}: ')

    for product in data:
        price = product['price']
        name = product['name']
        photo = types.FSInputFile(product['picture'])
        await message.answer_photo(photo=photo, caption=f'{name}\nцена: {price} сом')