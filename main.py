import asyncio
from aiogram import Bot
import logging

from config import bot, dp, set_my_menu, database
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.randompic import randompic_router
from handlers.menu import menu_router
from handlers.feedback import feedback_router
from handlers.generic_answer import echo_router
from handlers.house_link import house_router

async def on_startup(bot: Bot):
    await database.create_tables()


async def main():
    await set_my_menu()
    dp.include_router(start_router)
    dp.include_router(house_router)
    dp.include_router(myinfo_router)
    dp.include_router(randompic_router)
    dp.include_router(menu_router)
    dp.include_router(feedback_router)
    dp.include_router(echo_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
