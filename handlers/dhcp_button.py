import asyncio
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

dhcp = Router()



@dhcp.message(F.text == "DHCP")
async def dhcp_navigation(message: Message):
    kb = [
        [
            KeyboardButton(text='isc-dhcp-server'),
            KeyboardButton(text='MT DHCP'),
            KeyboardButton(text='Back'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Выбери тип DHCP!", reply_markup=markup)

@dhcp.message(F.text == 'Back')
async def dhcp_back(message: Message):
    kb = [
        [
            KeyboardButton(text='DHCP'),
            KeyboardButton(text='DNS'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Вернул назад", reply_markup=markup)

@dhcp.message(F.text == 'isc-dhcp-server')
async def dhcp_server(message: Message):
    await message.answer("Привет, сейчас я помогу тебе развернуть DHCP через утилиту - ```isc-dhcp-server```", parse_mode=ParseMode.MARKDOWN)

@dhcp.message(F.text == 'MT DHCP')
async def dhcp_mikrotik(message: Message):
    await message.answer("Привет, сейчас я помогу тебе развернуть DHCP через - ```MikroTik```", parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("Для начала зайти в настройки **Виртуальной машины** и добавь еще одну сеть - Изолированную сеть. Такой же путь проделайте на **клиенте**", parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("Перезагрузка МикроТика... - system reboot")
    await asyncio.sleep(3)
    await message.answer("""Для проверки сетей напишите ```  interface print```\n\nДолжно быть примерно так - 
```    
    Flags: X - disabled, R - running
 #   NAME      TYPE        MTU  STATE  
 0 R ether1   ether       1500 running
 1 R ether2   ether       1500 running
 ```
 
 ether1 - NAT
 ether2 - iso
 """, parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("""Далее прописываем эти команды: 
```
#- примечание, все команды пишем в одну строку!
/ip address add address=192.168.1.1/24 interface=ether2
=== этой командой присваиваем IP изолированной сети ===
/ip pool add name=dhcp-pool1 ranges=192.168.1.10-192.168.1.100
=== этой командой назначаем имя пулу IP, который будет выдавать наш DHCP ===
/ip dhcp-server add address-pool=dhcp-pool1 disabled=no interface=ether2 lease-time=3d name=dhcp-server1
=== этой командой создаём DHCP, назначаем пул, назначаем интерфейс к которому принадлежит DHCP, время работы DHCP, название DHCP ===
/ip dhcp-server network add address=192.168.1.0/24 dns-server=8.8.8.8 gateway=192.168.1.1 netmask=24 
=== в этой команде настройка DHCP ===
```
""", parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("""Далее заходим на клиента, пишем команды: 
```
ip a

#- пишем эту команду для просмотра IP-адреса
```
```
sudo dhclient -r

#- пишем эту команду что бы убить процесс назначания адресов    
```
```
sudo dhclient
ip a

#- пишем эти команды, что бы восстановить процесс назначения адресов и проверяем назначение IP, нашим DHCP
```
""", parse_mode=ParseMode.MARKDOWN)
    await message.answer("Вот и всё, DHCP настроен.")