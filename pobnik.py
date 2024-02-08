from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import aiogram.dispatcher.filters as filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_polling

bot = Bot(token='6368457366:AAEgMt-B74_Bj-DEhGc30iNB88p9GdBIO54')
dp = Dispatcher(bot, storage=MemoryStorage())

class HandleClient(StatesGroup):
    waiting_for_start = State()
    waiting_for_name = State()
    waiting_for_Surname = State()
    waiting_for_numder = State()
    waiting_for_gmail = State()
    waiting_for_finish1 = State()

async def start(message: types.Message, state: FSMContext):
    await message.answer('привет напишите да для продолжения')
    await HandleClient.waiting_for_name.set()

async def on_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer('скожите свое имя')
    await HandleClient.waiting_for_Surname.set()

async def on_Surname(message: types.Message, state: FSMContext):
    await state.update_data(Surname = message.text)
    await message.answer('скожите свою фамилию')
    await HandleClient.waiting_for_numder.set()

async def on_number(message: types.Message, state: FSMContext):
    await state.update_data(numder = message.text)
    await message.answer('скожите свой телефон')
    await HandleClient.waiting_for_gmail.set()   

async def on_gmail(message: types.Message, state: FSMContext):
    await state.update_data(gmail = message.text)
    await message.answer('скожите свой gmail')
    await HandleClient.waiting_for_finish1.set()

async def on_finish1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"{data['name']} {data['Surname']} {data['numder']} {data['gmail']}")
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(on_name, state=HandleClient.waiting_for_name)
    dp.register_message_handler(on_Surname, state=HandleClient.waiting_for_Surname)
    dp.register_message_handler(on_number, state=HandleClient.waiting_for_numder)
    dp.register_message_handler(on_gmail, state=HandleClient.waiting_for_gmail)
    dp.register_message_handler(on_finish1, commands="finish1", state="*")

register_handlers(dp)
