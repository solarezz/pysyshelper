from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

def dns_navigation():
    kb = [
        [
            KeyboardButton(text='BIND9'),
            KeyboardButton(text='fly-admin-bind'),
            KeyboardButton(text='Back'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)
    return markup

def dhcp_navigation():
    kb = [
        [
            KeyboardButton(text='isc-dhcp-server'),
            KeyboardButton(text='MT DHCP'),
            KeyboardButton(text='Back'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return markup

def back():
    kb = [
        [
            KeyboardButton(text='DHCP'),
            KeyboardButton(text='DNS'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return markup