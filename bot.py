from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import texts
import os
from keyboards import trapped_kb, barrel_kb, friend_kb, note_kb, beach_kb, boat_kb, congrats_kb, light_note_kb
import config

logging.basicConfig(level=logging.INFO)

# API_TOKEN = str(os.environ.get('BOT_TOKEN'))
API_TOKEN = config.BOT_TOKEN

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

class State(StatesGroup):
    trapped_s = State()
    barrel_s = State()
    friend_s = State()
    note_s = State()
    beach_s = State()
    boat_s = State()
    congrats_s = State()
    light_note_s = State()


@dp.message_handler(commands=['start'], state='*')
async def get_trapped(message: types.Message):
    await State.trapped_s.set()
    await message.answer("<i>мок - разрабатываемый вариант.тестовый квест по мотивам 4 сезона 11 серии MR.ROBOT. возможно продолжение</i>", parse_mode='HTML')
    await message.answer_photo(photo=types.InputFile('images/trapped.jpg'),
                                caption=texts.trapped,
                                reply_markup=trapped_kb)


@dp.message_handler(state=State.trapped_s)
async def get_barrel(message: types.Message):
    input = message.text
    if input == 'Подвинуть бочку':
        await message.answer_photo(photo=types.InputFile('images/barrel.jpg'),
                                    caption=texts.barrel,
                                    reply_markup=barrel_kb)
        await State.barrel_s.set()
    elif input == 'Сесть рядом с другом':
        await message.answer_photo(photo=types.InputFile('images/darknote.jpg'),
                                    caption=texts.dark_friend,
                                    reply_markup=friend_kb)
        await State.friend_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=trapped_kb)


@dp.message_handler(state=State.barrel_s)
async def get_friend(message: types.Message):
    input = message.text
    if input == 'Войти в туннель':
        await message.answer_photo(photo=types.InputFile('images/friend.jpg'),
                                    caption=texts.friend,
                                    reply_markup=friend_kb)
        await State.friend_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=barrel_kb)


@dp.message_handler(state=State.friend_s)
async def get_note(message: types.Message):
    input = message.text
    if input == 'Прочесть записку':
        await message.answer_photo(photo=types.InputFile('images/note.jpg'),
                                    caption=texts.note,
                                    reply_markup=note_kb)
        await State.note_s.set()
    elif input == 'Зажечь спичку':
        await message.answer_photo(photo=types.InputFile('images/dontleave.jpg'),
                                    caption=texts.light_note,
                                    reply_markup=light_note_kb)
        await State.light_note_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=friend_kb)


@dp.message_handler(state=State.light_note_s)
async def get_congrats(message: types.Message):
    input = message.text
    if input == 'Остаться':
        await message.answer_photo(photo=types.InputFile('images/end.png'),
                                    reply_markup=congrats_kb)
        await message.answer(texts.ending, parse_mode='HTML')
        await State.congrats_s.set()
    elif input == 'Уйти':
        await(get_beach(message))
    else:
        await message.answer(texts.default_ans, reply_markup=light_note_kb)


@dp.message_handler(state=State.note_s)
async def get_beach(message: types.Message):
    input = message.text
    if input == 'Уйти':
        await message.answer_photo(photo=types.InputFile('images/beach.jpg'),
                                    caption=texts.beach,
                                    reply_markup=beach_kb)
        await State.beach_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=note_kb)


@dp.message_handler(state=State.beach_s)
async def get_boat(message: types.Message):
    input = message.text
    if input == 'Изучить':
        await message.answer_photo(photo=types.InputFile('images/boat.jpg'),
                                    caption=texts.boat,
                                    reply_markup=boat_kb)
        await State.boat_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=beach_kb)


@dp.message_handler(state=State.boat_s)
async def get_congrats(message: types.Message):
    input = message.text
    if input == 'Взайти на судно':
        await message.answer_photo(photo=types.InputFile('images/congrats.jpg'),
                                    caption=texts.congrats,
                                    reply_markup=congrats_kb)
        await State.congrats_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=boat_kb)


@dp.message_handler(state=State.congrats_s)
async def get_menu(message: types.Message):
    if message.text == 'Да':
        await get_trapped(message)
    else:
        await message.answer(texts.default_ans, reply_markup=congrats_kb)

@dp.message_handler()
async def get_stateless(message: types.Message):
    await message.answer(texts.default_ans)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)