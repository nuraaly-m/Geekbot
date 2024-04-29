from aiogram import types, F
from crawler.house_kg import house_router, HouseCrawler


@house_router.callback_query(F.data == 'house')
async def house_links(cb: types.CallbackQuery):
    crawler = HouseCrawler()
    await crawler.get_page()
    links = await crawler.get_house_links()
    for link in links:
        await cb.message.answer(str(link))