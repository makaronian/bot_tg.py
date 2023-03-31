from dotenv import load_dotenv, find_dotenv
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

