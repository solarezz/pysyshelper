from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [
            KeyboardButton(text='DHCP'),
            KeyboardButton(text='DNS'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("""
🌟 Привет, дорогой системный администратор! 🌟

Этот бот создан, чтобы облегчить твою голову, которая и так полна "важной" информации. 🤯 Здесь ты найдёшь полезные советы по настройке DHCP, DNS и множеству других вопросов, которые могут возникнуть в процессе работы. 💻✨


Создатель бота: @solarezzov 👨‍💻
""", reply_markup=markup)