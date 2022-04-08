from aiogram import Bot, executor, Dispatcher, types
from decouple import config
import logging

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    question = "Столица Китая?"
    answers = ['Шанхай', 'Пекин']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1
                        )


@dp.message_handler(commands=['mem'])
async def mem_1(message: types.Message):
    photo = open("Media/images.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)


