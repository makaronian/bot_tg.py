from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот в сети.')
'**********************************КЛИЕНТСКАЯ ЧАСТЬ***************************************'
@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Саламалейкум, родной!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Semen_jr_bot')

@dp.message_handler(commands=['Расписание'])
async def schedule(message : types.Message):
    await bot.send_message(message.from_user.id, 'Понедельник : 1.2.3.')

@dp.message_handler(commands=['Погода'])
async def schedule(message : types.Message):
    await bot.send_message(message.from_user.id, 'Понедельник : Жара, +28')
'**********************************АДМИНСКАЯ ЧАСТЬ****************************************'

'*************************************ОБЩАЯ ЧАСТЬ*****************************************'

@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет!')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)