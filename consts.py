from aiogram import types


def getGlobalKeyboard() -> types.InlineKeyboardMarkup:
    inlKb = [
        [types.InlineKeyboardButton(text="Баланс 💸", callback_data="balance"),
         types.InlineKeyboardButton(text="Мои ставки 👑", callback_data="history_bet")],

        [types.InlineKeyboardButton(text="Сделать ставку 🏆", callback_data="3")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=inlKb)
    return keyboard


def getBackKeyboard() -> types.InlineKeyboardMarkup:
    inlKb = [[types.InlineKeyboardButton(text="Назад", callback_data="start")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=inlKb)
    return keyboard
