import httpx
from parsel import Selector
from aiogram import F, Router, types


house_router = Router()

class HouseCrawler:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    async def get_page(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.MAIN_URL)
            self.page = response.text
            return response

    async def get_house_links(self):
        html = Selector(self.page)
        links = html.css('.title a::attr(href)').getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links[:3]


@house_router.callback_query(F.data == 'house')
async def house_links(cb: types.CallbackQuery):
    crawler = HouseCrawler()
    await crawler.get_page()
    links = await crawler.get_house_links()
    for link in links:
        await cb.message.answer(str(link))

