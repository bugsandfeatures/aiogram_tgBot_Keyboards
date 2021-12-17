import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

loop    = asyncio.new_event_loop()
bot     = Bot(BOT_TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp      = Dispatcher(bot, loop=loop, storage=storage)

async def shutdown(dp):
    await storage.close()
    await bot.close()


if __name__ == '__main__':
    from handlers import dp, send_hello
    executor.start_polling(dp, on_startup=send_hello, on_shutdown=shutdown)