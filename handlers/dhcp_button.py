from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

dhcp_button = Router()

@dhcp_button.message(F.Text == 'DHCP')
async def dhcp_navigation(message: Message):
    kb = [
        [
            KeyboardButton(text='isc-dhcp-server'),
            KeyboardButton(text='MT DHCP'),
            KeyboardButton(text='Back')
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Выбери тип DHCP!", reply_markup=markup)

@dhcp_button.message(F.Text == 'Back')
async def dhcp_back(message: Message):
    kb = [
        [
            KeyboardButton(text='DHCP'),
            KeyboardButton(text='DNS'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вернул назад", reply_markup=markup)

@dhcp_button.message(F.Text == 'isc-dhcp-server')
async def dhcp_server(message: Message):
    await message.answer("")