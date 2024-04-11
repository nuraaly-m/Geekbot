from aiogram import types


def start_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='наш адрес', url='https://2gis.kg/bishkek/geo/70000001019339201'),
                types.InlineKeyboardButton(text='наш контакт', callback_data='contacts')
            ],
            [
                types.InlineKeyboardButton(text='о нас', url='https://faiza.kg'),
                types.InlineKeyboardButton(text='наш сайт', url='https://faiza.kg'),
                types.InlineKeyboardButton(text='инстаграм', url='https://www.instagram.com/kover_samolet_kg/p/B_HnYeGjvf5/')
            ],
            [
                types.InlineKeyboardButton(text='меню', callback_data='меню'),
                types.InlineKeyboardButton(text='отзывы', callback_data='отзывы')
            ],
            [
                types.InlineKeyboardButton(text='оставить отзыв', callback_data='feedback')
            ]
        ]

    )
    return kb