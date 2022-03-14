from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


##


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'test!')


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='test')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='test.\n 😉',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f' code={code}')




@dp.message_handler(commands=['set1'])
async def process_hi2_command(message: types.Message):
    await message.reply("qq",
                        reply_markup=kb.greet_kb2)





@dp.message_handler(commands=['set4'])
async def process_hi5_command(message: types.Message):
    await message.reply("i'm tired",
                        reply_markup=kb.markup5)


@dp.message_handler(commands=['set5'])
async def process_hi6_command(message: types.Message):
    await message.reply("Эти две кнопки не зависят друг от друга",
                        reply_markup=kb.markup_request)


@dp.message_handler(commands=['set6'])
async def process_hi7_command(message: types.Message):
    await message.reply("test2",
                        reply_markup=kb.markup_big)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("go to hell",
                        reply_markup=kb.ReplyKeyboardRemove())

##


@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка",
                        reply_markup=kb.inline_kb1)


@dp.message_handler(commands=['menu'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки",
                        reply_markup=kb.inline_kb_full)

help_message = text(
    "Доступные команды:\n",
    "/start - приветствие",
    "\nШаблоны клавиатур:",
    "/set1 - ",
    "/set4 - ",
    "/set5 - запрос локации и номера телефона",
    "/set6 - "
    "/rm - ",
    "\nИнлайн клавиатуры:",
    "/1 - ",
    "/menu - ",
    sep="\n"
)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


if __name__ == '__main__':
    executor.start_polling(dp)
