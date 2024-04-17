from aiogram import Bot, Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

bot = Bot(config('TOKEN'), parse_mode='html', disable_web_page_preview=True)
# storage = MemoryStorage()
dp = Dispatcher(bot)
# dp = Dispatcher(bot, storage=storage)