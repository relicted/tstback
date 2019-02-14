import aiohttp
import asyncio
import aiohttp_jinja2

from aiohttp import web
import random

class Handler(web.View):

    async def post(self):
        db = self.request.app.db
        try:
            data = await self.request.json()

            template = "INSERT INTO subscriber_info (name, city, age) VALUES ('{name}', '{city}', '{age}');".format(
                ** data
            )
            async with db.acquire() as conn:
                await conn.execute(
                    template
                )
            await asyncio.sleep(10)
            return web.json_response(data, status=201)

        except:
            await asyncio.sleep(10)

            return web.json_response({'error': 'Something wrong'}, status=400)

