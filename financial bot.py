from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

# 🔹 Твой токен (не передавай его другим!)
TOKEN = "8492691594:AAFSmXXPnv3lL_SEwyJJs9rumwQtisM7r_U"

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! 👋\nЯ бот-помощник от dias_helper.\nНапиши /menu, чтобы открыть меню.")

# Команда /menu
@dp.message(Command("menu"))
async def menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💰 Финансовая пирамида"),
                KeyboardButton(text="🎣 Фишинг"),
            ],
            [
                KeyboardButton(text="🏦 Финансовая безопасность"),
                KeyboardButton(text="👤 Кто такие дропы"),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer("Выбери интересующую тему 👇", reply_markup=keyboard)


# 💰 Ответ про финансовую пирамиду
@dp.message(lambda message: message.text == "💰 Финансовая пирамида")
async def pyramid_info(message: types.Message):
    await message.answer(
        "💰 **Финансовая пирамида** — это схема, где прибыль участников выплачивается не из реального бизнеса, "
        "а из вложений новых участников.\n\n🚫 Такие схемы незаконны и могут привести к потере денег."
    )


# 🎣 Ответ про фишинг
@dp.message(lambda message: message.text == "🎣 Фишинг")
async def phishing_info(message: types.Message):
    await message.answer(
        "🎣 **Фишинг** — это способ обмана, когда мошенники выдают себя за банки или сервисы, "
        "чтобы получить твои пароли и данные карт.\n\n⚠️ Никогда не переходи по подозрительным ссылкам!"
    )


# 🏦 Ответ про финансовую безопасность
@dp.message(lambda message: message.text == "🏦 Финансовая безопасность")
async def safety_info(message: types.Message):
    await message.answer(
        "🏦 **Финансовая безопасность** — это умение защищать свои деньги и личные данные "
        "от мошенников и финансовых рисков.\n\n✅ Проверяй источники, не передавай пароли и будь внимателен онлайн."
    )


# 👤 Ответ про дропов
@dp.message(lambda message: message.text == "👤 Кто такие дропы")
async def drops_info(message: types.Message):
    await message.answer(
        "👤 **Дроп (денежный мул)** — человек, который за вознаграждение позволяет использовать "
        "свой банковский счёт для перевода чужих денег.\n\n⚠️ Это незаконно и может привести к уголовной ответственности."
    )


# Запуск бота
async def main():
    print("✅ Бот запущен и работает...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
