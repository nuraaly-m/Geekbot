from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from db.database import Database


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
database = Database(
    Path(__file__).parent / "db.sqlite"
)


async def set_my_menu():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='start'),
        types.BotCommand(command='menu', description='menu'),
    ])
