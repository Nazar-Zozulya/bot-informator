import asyncio
import aiogram
import aiogram.filters as filters
import logging
import sqlite3


bot = aiogram.Bot(token = "6301213892:AAFroswyF2YXLE1EbY2Hza1h0bZXp_lhhvM")

dp = aiogram.Dispatcher()

con = sqlite3.connect("admin.db")
pen = con.cursor()


button_user = aiogram.types.KeyboardButton(text = "Користувач")
button_admin = aiogram.types.KeyboardButton(text = "Адміністратор")
start_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_user, button_admin]], resize_keyboard = True)

button_auth = aiogram.types.KeyboardButton(text = "Авторизація")
button_reg = aiogram.types.KeyboardButton(text = "Реєстрація")
reg_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_auth, button_reg]], resize_keyboard = True)



@dp.message(filters.CommandStart())
async def start(message: aiogram.types.Message):
    pochta = map(str.strip, message.text.split(","))
    await message.answer("Hello", reply_markup = start_keyboard)
    print(pochta)

@dp.message()
async def admin(message: aiogram.types.Message):
    if message.text == "Адміністратор":
        await message.answer(text = "регистраційне меню", reply_markup = reg_keyboard)
        

@dp.message()
async def reg(message: aiogram.types.Message):
    if message.text == "Реєстрація":
        await message.answer(text = "Реєстрація")

# dp.start_polling(bot)
async def main():
    await dp.start_polling(bot)
asyncio.run(main())