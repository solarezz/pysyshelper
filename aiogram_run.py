import asyncio
from create_bot import bot, dp
from handlers.start import start_router
from handlers.dhcp_button import dhcp
from handlers.dns_button import dns


async def main():
    dp.include_router(dhcp)
    dp.include_router(dns)
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())