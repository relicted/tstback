import asyncio
import random


async def run_tasks():
    pass
#
#

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # asyncio.ensure_future(schedule(5, loop), loop=loop)
    loop.run_forever()
