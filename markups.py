import aiogram

button_user = aiogram.types.KeyboardButton(text = "Користувач")
button_admin = aiogram.types.KeyboardButton(text = "Адміністратор")
start_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_user, button_admin]], resize_keyboard = True)

button_auth = aiogram.types.KeyboardButton(text = "Авторизація")
button_reg = aiogram.types.KeyboardButton(text = "Реєстрація")
reg_keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_auth, button_reg]], resize_keyboard = True)

buy_inline_button = aiogram.types.InlineKeyboardButton(text = "BUY", callback_data = "buy_product")
# decline_inline_button = aiogram.types.InlineKeyboardButton(text = "DECLINE", callback_data = "decline")
info_inline_button = aiogram.types.InlineKeyboardButton(text = "INFO", callback_data = "info_product")
accept_button = aiogram.types.InlineKeyboardButton(text = "ACCEPT", callback_data = "accept")
confirm_button = aiogram.types.InlineKeyboardButton(text = "CONFIRM", callback_data = "confirm_product")
keyboard_inline = aiogram.types.InlineKeyboardMarkup(inline_keyboard = [[buy_inline_button, info_inline_button], [accept_button], [confirm_button]])

accept_inline_button = aiogram.types.InlineKeyboardButton(text = "Підтвердити", callback_data = "accept_callback")
decline_inline_button = aiogram.types.InlineKeyboardButton(text = "Відхилити", callback_data = "decline_callback")

accept_admin_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard= [[accept_inline_button, decline_inline_button]])