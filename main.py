import aiogram
import aiogram.filters as filters
# import logging
import asyncio
import sqlite3 as sql
# from db.admindb import *

# con = sql.connect("admin.db")
with sql.connect("admin.db") as con:
    con = sql.connect("admin.db")
    cursor = con.cursor()
    # cursor.execute("DROP TABLE IF EXISTS admin")
    cursor.execute(""" CREATE TABLE IF NOT EXISTS admin (
                    user_id INTEGER PRIMARY KEY,
                    email TEXT,
                    nickname TEXT,
                    password TEXT,
                    phone INTEGER
    )""")


                #    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
# con.close()
# logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(token = "6559949501:AAGXPvH1cOvMYrVo67L2n10ECx2QCf2jdQ4")

dp = aiogram.Dispatcher()

button_user = aiogram.types.KeyboardButton(text = "Користувач")
button_admin = aiogram.types.KeyboardButton(text = "Адміністратор")
start_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_user, button_admin]], resize_keyboard = True)

button_auth = aiogram.types.KeyboardButton(text = "Авторизація")
button_reg = aiogram.types.KeyboardButton(text = "Реєстрація")
reg_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_auth, button_reg]], resize_keyboard = True)

message_list = []

@dp.message(filters.CommandStart())
async def start(message: aiogram.types.Message):
    # if(not DB.exists(message.from_user.id)):
    #         DB.add_user(message.from_user.id)
    await message.answer(text = "Hello", reply_markup = start_keyboard)
    
    # else:
    #     await bot.send_message(message.from_user.id, "Ви ввели вже зарееструвалися", reply_markup = reg_keyboard)
    # await message.answer(text = "Hello", reply_markup = start_keyboard)
    previous_message_text = message.text.split("+1")
    print(previous_message_text)

@dp.message()
async def registration(message: aiogram.types.Message):
    if message.text == "Адміністратор":
        await message.answer(text = "регистраційне меню", reply_markup = reg_keyboard)
    
    elif message.text == "Реєстрація":
        await message.answer(text = "Введіть емайл")
        previous_message_text2 = message.text
        print(previous_message_text2)
        con.execute(f"INSERT INTO admin (email, nickname, password, phone) VALUES ('{message.text}', 'pass', 'pass', 123)")
        con.commit()
            
        print(123)
            
        print(1234)
        # txt_id = message.message_id
        # txt_id = int(txt_id)
        # new_message = aiogram.types.Message(user_id=message.from_user.id, text=message.text,)
        
        previous_message_text3 = message.text.split("+1")
        # if message.reply_to_message == "Введіть емайл":
        #     print(323123124)
        #     con.execute(f"INSERT INTO admin (email, nickname, password, phone) VALUES ('{message.text}', 'pass', 'pass', 123)")

        # await message.answer(text = "Введіть ім'я")
        # con.excute(f"UPDATE admin SET nickname = '{message.text}'")


        # txt = message.text
        # print(txt)
        # print(message.text)
        
        print(12345)
# @dp.message()
# async def test(message: aiogram.types.Message):
    



async def main():
    await dp.start_polling(bot)
asyncio.run(main())