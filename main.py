from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import executor
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот Tiho.ai. Давай вместе помедитируем и послушаем музыку.")

@dp.message_handler(commands=['music'])
async def send_music(message: Message):
    await message.answer("Сейчас играет позитивная музыка 🎵 Для лучшего настроения!")

@dp.message_handler(commands=['meditation'])
async def send_meditation(message: Message):
    await message.answer("Включаем медитацию... 🧘 Спокойствие и умиротворение наполняют тебя.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
