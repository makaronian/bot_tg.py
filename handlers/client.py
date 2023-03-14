from aiogram import types, Dispatcher
from create_bot import dp, bot

#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Саламалейкум, родной!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Semen_jr_bot')

#@dp.message_handler(commands=['Расписание'])
async def schedule(message : types.Message):
    await bot.send_message(message.from_user.id, 'Понедельник : 1.2.3.')

#@dp.message_handler(commands=['Погода'])
async def nature(message : types.Message):
    await bot.send_message(message.from_user.id, 'Понедельник : Жара, +28')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(schedule, commands=['Расписание'])
    dp.register_message_handler(nature, commands=['Погода'])