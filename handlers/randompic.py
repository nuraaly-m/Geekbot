from aiogram import types, Router
from aiogram.filters import Command
import random
import os


randompic_router = Router()

@randompic_router.message(Command('randompic'))
async def random_pic(message: types.Message):
    image_dir = 'images/random_photo'
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random_image = random.choice(image_files)
    file_path = os.path.join('images/random_photo', random_image)
    file = types.FSInputFile(file_path)
    await message.answer_photo(photo=file)