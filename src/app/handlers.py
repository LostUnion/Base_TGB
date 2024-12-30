from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from app.messages import START_MESSAGE, HELP_MESSAGE, INSTALL_WG_ANDROID, INSTALL_WG_IOS, INSTALL_WG_LINUX, INSTALL_WG_WINDOWS, GET_VPN
from aiogram.enums import ParseMode


# Commands start
async def start(message: types.Message) -> None:
    menu_builder = InlineKeyboardBuilder()
    menu_builder.button(
        text='Начать',
        callback_data='get_vpn'
    )

    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        ""
        f"{START_MESSAGE}",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=menu_builder.as_markup()
    )

# Command help
async def help(message: types.Message) -> None:
    await message.answer(
        f"{HELP_MESSAGE}",
        parse_mode=ParseMode.MARKDOWN
    )

# Command wg_install_android
async def wg_install_android(message: types.Message) -> None:
    await message.answer(
        INSTALL_WG_ANDROID,
        parse_mode=ParseMode.MARKDOWN
    )

# Command wg_install_ios
async def wg_install_ios(message: types.Message) -> None:
    await message.answer(
        INSTALL_WG_IOS,
        parse_mode=ParseMode.MARKDOWN
    )

# Command wg_install_linux
async def wg_install_linux(message: types.Message) -> None:
    await message.answer(
        INSTALL_WG_LINUX,
        parse_mode=ParseMode.MARKDOWN
    )

# Command wg_install_windows
async def wg_install_windows(message: types.Message) -> None:
    await message.answer(
        INSTALL_WG_WINDOWS,
        parse_mode=ParseMode.MARKDOWN
    )

# Command get_vpn
async def get_vpn(message: types.Message) -> None:
    menu_builder = InlineKeyboardBuilder()
    menu_builder.button(
        text='*GIVE MY CONFIG*',
        callback_data='get_vpn'
    )
    await message.answer(
        f"{GET_VPN}",
        reply_markup=menu_builder.as_markup(),
        parse_mode=ParseMode.MARKDOWN
    )

async def get_vpn_callback(call: types.CallbackQuery) -> None:
    menu_builder = InlineKeyboardBuilder()
    menu_builder.button(
        text='GIVE MY CONFIG',
        callback_data='get_vpn'
    )
    await call.message.answer(
        f"{GET_VPN}",
        reply_markup=menu_builder.as_markup(),
        parse_mode=ParseMode.MARKDOWN
    )