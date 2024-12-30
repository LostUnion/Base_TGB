from aiogram import types
from messages import GET_VPN
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
