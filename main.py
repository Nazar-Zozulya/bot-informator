import asyncio
import aiogram
import aiogram.filters as filters
import logging
import sqlite3 as sql
from aiogram.types import InputFile 
import os
import markups as m
# import db

admindb = sql.connect("admin.db")
admindb = sql.connect("products.db")
admindb = sql.connect("cart.db")
with sql.connect("admin.db") as con:
    pen = con.cursor()
    pen.execute("""CREATE TABLE IF NOT EXISTS carts(
                user_id TEXT,
                email TEXT,
                nickname TEXT,
                password TEXT,
                phone INTEGER
    )""")
    pen.execute("SELECT  * FROM carts") 
with sql.connect("products.db") as con:
    pen = con.cursor()
    pen.execute("""CREATE TABLE IF NOT EXISTS carts(
                image BLOB,
                name TEXT,
                description TEXT
    )""")
    pen.execute("SELECT  rowid, * FROM carts") 
with sql.connect("cart.db") as con:

    pen = con.cursor()
    pen.execute("""CREATE TABLE IF NOT EXISTS carts(
                count INTEGER
    )""")
    pen.execute("SELECT  * FROM carts") 

admins_chat_id = -4181816820
bot = aiogram.Bot(token = "6301213892:AAFroswyF2YXLE1EbY2Hza1h0bZXp_lhhvM")
dp = aiogram.Dispatcher()
count = 0
dict_buy = {
    'count2': count
}

admindb = sql.connect("admin.db")
admindb = sql.connect("products.db")
admindb = sql.connect("cart.db")

PATH = os.path.abspath(__file__+"/.."+"/images")
burger_image = aiogram.types.FSInputFile(PATH + "/1.jpg")


@dp.message(filters.CommandStart())
async def start(message: aiogram.types.Message):
    await message.answer(text = "Hello", reply_markup = m.reg_keyboard)
    
@dp.message()
async def reg(message: aiogram.types.Message):
    if message.text == "Реєстрація":
        await message.answer(text = "Реєстраційне вікно", reply_markup = m.start_keyboard)
        # await message.answer(admins_chat_id,text = "123",)
        await bot.send_message(chat_id = admins_chat_id, text="Бажаєте додати нового адміністратора?\nEmail\nNickname\nPassword\nPhone Number", reply_markup = m.accept_admin_inline_keyboard)
        pen.execute(f"INSERT INTO cart VALUES(3124214124)")
    elif message.text == "Адміністратор":
        await message.answer(text = "Введіть\nEmail\nNickname\nPassword\nPhone Number")

        
@dp.callback_query()
async def call_back_handler(callback: aiogram.types.CallbackQuery):
    
    if callback.data == "buy_product":
        dict_buy["count2"] += 1
        callback.message.reply_markup.inline_keyboard[0][0].text = f"BUY {dict_buy['count2']}"
        await callback.message.edit_reply_markup(inline_message_id = callback.inline_message_id, reply_markup = callback.message.reply_markup)
    if callback.data == "info_product":
        await callback.message.answer(text = "ТУТ БУДЕ ІНФОРМАЦІЯ") 
    if callback.data == "confirm_product":
        await callback.message.answer(text = "ЗАМОВЛЕННЯ ПІДТВЕРДЖЕНО ✅")
        print(dict_buy['count2'])
        count1 = dict_buy['count2']
        pen.execute(f"INSERT INTO cart VALUES(3124214124)")
    elif callback.data == "accept_callback":
        await callback.message.answer(text = "ваш запит прийнято")
    elif callback.data == "decline_callback":
        await callback.message.answer(text = "ваш запит відхиленно")
        



# dp.start_polling(bot)
async def main():
    await dp.start_polling(bot)
asyncio.run(main())