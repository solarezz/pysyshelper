import asyncio
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message
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
    await message.answer("ВСЕХ ПОПРОШУ ПЕРЕВЕРНУТЬ ТЕЛЕФОН ЧТО БЫ КОД НЕ ЛОМАЛСЯ!!!!!1\nЧерез 10 бот выдаст Ваш запрос!")
    await asyncio.sleep(10)
    await message.answer('И так, сейчас я помогу настроить DNS с помощью утилиты ```"BIND9"```', parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("Начинаем устанавливать утилиты ``` sudo apt install bind9\nsudo apt install dnsutils```", parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("""
Для начала прописываем ``` ip a``` и смотрим IP.
Предположим мой IP - 192.168.14.88
Заходим в файл - /etc/bind/named.conf.options
``` sudo nano /etc/bind/named.conf.options```
И прописываем там это:
```
forwarders {
    192.168.14.88; #- мой ip
};

listen-on {
    127.0.0.1;
    192.168.14.88;
};
listen-on-v6 {
    none;
};
```
После всего этого выходим из конфига и пишем:
```
sudo systemctl restart bind9
```

""", parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("""
    Заходим в /etc/bind/named.conf.local командой ``` sudo nano /etc/bind/named.conf.local```
```

zone "solarezzov.ru"    { # название вашего домена
    type master; # тип master указывает, что запросы относительно этой зоны будут обрабатываться этим сервером, и перенаправляться не будут
    file "/etc/bind/zones/db.solarezzov.ru"; # путь к файлу данных прямой зоны
};
 
zone "14.168.192.in-addr.arpa" { # ваш айпишник наоборот
    type master; # тип master указывает, что запросы, относящиеся к этой зоне, будут обрабатываться этим сервером, и перенаправляться не будут
    file "/etc/bind/zones/db.14.168.192"; # подсеть 192.168.14.0/24, путь к файлу данных
};
```
Сохраняем и выходим с конфига и пишем следующее в консоли:
```
sudo mkdir /etc/bind/zones 
sudo cp /etc/bind/db.local /etc/bind/zones/db.solarezzov.ru
sudo cp /etc/bind/db.127 /etc/bind/zones/db.14.168.192
sudo chown -R bind:bind /etc/bind/zones
```
""", parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("""
Далее заходим в след. конфиг - /etc/bind/zones/db.solarezzov.ru
```
sudo nano /etc/bind/zones/db.solarezzov.ru    
```
Заменяем мои значения на Ваши!
```
$TTL    604800
@   IN  SOA solarezzov.ru. admin.solarezzov.ru. (
                              5         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
; name servers - NS records - определяем имена DNS-серверов
    IN      NS      solarezzov.ru.
; name servers - A records - определяем адреса компьютеров, сначала сервер(ы) DNS
solarezzov.ru.      IN      A      192.168.14.88
; 192.168.32.0/24 - A records - а потом все остальные компьютер(ы) сети
host.solarezzov.ru. IN      A      192.168.14.32 ; IP КЛИЕНТА!!!!
```
Сохраняем и заходим в след. конфиг - /etc/bind/zones/db.14.168.192:
```
sudo nano /etc/bind/zones/db.14.168.192
```
Заменяем моиз начения на Ваши!
```

$TTL    604800
@   IN  SOA solarezzov.ru. admin.solarezzov.ru. (
                              5         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL ;
 
; name servers
    IN      NS      solarezzov.ru.
; PTR Records
88  IN      PTR     solarezzov.ru.        ; 192.168.14.88
32  IN      PTR     host.solarezzov.ru.   ; 192.168.14.32
```
Сохраняем и перезапускаем BIND9:
```
sudo systemctl restart bind9
```
""", parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(3)
    await message.answer("И чо сложно было?")