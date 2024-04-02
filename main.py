import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random
import os


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


users = []
@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    if message.from_user.id not in users:
        users.append(message.from_user.id)
    await message.answer(f'salam! {message.from_user.first_name}, we serve {len(users)} users')


@dp.message(Command('myinfo'))
async def start_cmd(message: types.Message):
    image_dir = 'images/random_photo'
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random_image = random.choice(image_files)
    file_path = os.path.join('images/random_photo', random_image)
    file = types.FSInputFile(file_path)
    await message.answer_photo(photo=file, caption=f'your id: {message.from_user.id}\n'
                         f'your username: {message.from_user.username}\n'
                         f'your first_name: {message.from_user.first_name}')


@dp.message(Command('random_pic'))
async def random_pic(message: types.Message):
    image_dir = 'images/random_photo'
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random_image = random.choice(image_files)
    file_path = os.path.join('images/random_photo', random_image)
    file = types.FSInputFile(file_path)
    await message.answer_photo(photo=file)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())