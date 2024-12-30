__all__ = [
    'regiser_user_commands'
]

from aiogram import Router, F
from aiogram.filters import Command
from app.handlers import *

def regiser_user_commands(router: Router) -> None:
    router.message.register(
        start,
        Command(commands=['start'])
    )

    # router.callback_query.register(
    #     start_callback,
    #     F.data == 'start'
    # )

    router.message.register(
        get_vpn,
        Command(commands=['get_vpn'])
    )

    router.callback_query.register(
        get_vpn_callback,
        F.data == 'get_vpn'
    )

    router.message.register(
        help,
        Command(commands=['help'])
    )

    router.message.register(
        wg_install_android,
        Command(commands=['wg_install_android'])
    )

    router.message.register(
        wg_install_ios,
        Command(commands=['wg_install_ios'])
    )

    router.message.register(
        wg_install_linux,
        Command(commands=['wg_install_linux'])
    )

    router.message.register(
        wg_install_windows,
        Command(commands=['wg_install_windows'])
    )