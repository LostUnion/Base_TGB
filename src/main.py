import logging
import asyncio
from app.logger import logger

from datetime import datetime

from aiohttp import web

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from decouple import config
from app import regiser_user_commands

TOKEN = config(
    "BOT_TOKEN",
    cast=str
)

BASE_WEBHOOK_URL = config(
    "BASE_WEBHOOK_URL",
    cast=str
)

WEBHOOK_PATH = config(
    "WEBHOOK_PATH",
    default="/webhook",
    cast=str
)

WEBHOOK_SECRET = config(
    "WEBHOOK_SECRET",
    default="my-secret",
    cast=str
)

WEB_SERVER_HOST = config(
    "WEB_SERVER_HOST",
    default="localhost",
    cast=str
)

WEB_SERVER_PORT = config(
    "WEB_SERVER_PORT",
    default=8080,
    cast=int
)

# router = Router()

# Текущая дата и время с заданным форматом
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

router = Router()

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",
        secret_token=WEBHOOK_SECRET
    )

def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    regiser_user_commands(dp)
    dp.startup.register(on_startup)
    bot = Bot(token=TOKEN)

    app = web.Application()

    webh_req_hand = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )

    webh_req_hand.register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(app,
                host=WEB_SERVER_HOST,
                port=WEB_SERVER_PORT
    )

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        main()
    except KeyboardInterrupt as quit:
        logging.basicConfig(level=logging.INFO)
