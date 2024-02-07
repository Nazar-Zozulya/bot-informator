import aiogram
import aiogram.filters as filters
import asyncio
import sqlite3 as sql
# import db

# con = sql.connect("admin.db")
with sql.connect("admin.db") as con:
    con = sql.connect("admin.db")
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS admin")
    cursor.execute(""" CREATE TABLE IF NOT EXISTS admin (
                    email TEXT,
                    nickname TEXT,
                    password TEXT,
                    phone INTEGER
    )""")


                #    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
# con.close()

bot = aiogram.Bot(token = "6559949501:AAGXPvH1cOvMYrVo67L2n10ECx2QCf2jdQ4")

dp = aiogram.Dispatcher()

button_user = aiogram.types.KeyboardButton(text = "Користувач")
button_admin = aiogram.types.KeyboardButton(text = "Адміністратор")
start_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_user, button_admin]], resize_keyboard = True)

button_auth = aiogram.types.KeyboardButton(text = "Авторизація")
button_reg = aiogram.types.KeyboardButton(text = "Реєстрація")
reg_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_auth, button_reg]], resize_keyboard = True)

message_list = [    ]

@dp.message(filters.CommandStart())
async def start(message: aiogram.types.Message):
    await message.answer(text = "Hello", reply_markup = start_keyboard)
    

@dp.message()
async def registration(message: aiogram.types.Message):
    if message.text == "Адміністратор":
        await message.answer(text = "регистраційне меню", reply_markup = reg_keyboard)
    if message.text == "Реєстрація":
        print(123)
        await message.answer(text = "Введіть емайл")
        # cursor.execute(f"UPDATE admin SET {message.text} WHERE rowid")
        # cursor.execute(f"INSERT INTO admin () VALUES(?, ?)")

        # print(msg.message_id -1)
        print(message.answer(text = "Введіть емайл"))
        if message.answer(text = "Введіть емайл"):
            print(1234)
            # txt_id = message.message_id
            # txt_id = int(txt_id)
            # new_message = aiogram.types.Message(user_id=message.from_user.id, text=message.text,)
            cursor.execute(f"INSERT INTO admin(email, nickname, password, phone) VALUES ('{message.from_user}', 'pass', 'pass', 123)")
            txt = message.text
            print(txt)
            print(message.text)
            con.commit()
            print(12345)
        

async def main():
    await dp.start_polling(bot)
asyncio.run(main())