import asyncio
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from keyboards import all_keyboards

dns = Router()

@dns.message(F.text == 'DNS')
async def dns_navigation(message: Message):
    await message.answer("Выбери утилиту для DNS:", reply_markup=all_keyboards.dns_navigation())

@dns.message(F.text == 'Back')
async def dns_back(message: Message):
    await message.answer("Вернул назад", reply_markup=all_keyboards.back())

@dns.message(F.text == 'BIND9')
async def dns_bind(message: Message):
    await message.answer('И так, сейчас я помогу настроить DNS с помощью утилиты ```"BIND9"```', parse_mode=ParseMode.MARKDOWN)
