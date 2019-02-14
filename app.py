import os
import asyncio
import jinja2
from aiohttp_jinja2 import setup as setup_templates
from aiohttp_cors import ResourceOptions, setup as setup_cors
from aiopg.sa import create_engine
from aiojobs.aiohttp import setup as job_setup
from aiohttp import web

import motor.motor_asyncio
import pathlib
from main.routes import routes
from main.middlewares import middlewares


async def init_pg(app):
    engine = await create_engine(
        database=os.getenv('DATABASE_NAME'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        host=os.getenv('DATABASE_HOST', 'localhost'),
        port=os.getenv('DATABASE_PORT', '5432'),

    )
    return engine


async def startup(app):
    app.db = await init_pg(app)
    app.websockets = []


async def shutdown(app):
    pass


async def create_app(loop):
    app = web.Application(loop=loop)

    job_setup(app)

    app.on_startup.append(startup)
    app.on_shutdown.append(shutdown)

    app.middlewares.extend(middlewares)

    for route in routes:
        app.router.add_route(**route)
    setup_templates(app, loader=jinja2.FileSystemLoader('templates/'))

    # CORS SETUP
    cors = setup_cors(app, defaults={
        "*": ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods='*',
        )
    })

    for resource in app.router.resources():
        cors.add(resource)
    return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    web.run_app(create_app(loop))
