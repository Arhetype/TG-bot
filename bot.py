import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import types
import config, consts
from aiogram import F

logging.basicConfig(level=logging.INFO)

token = config.getTgToken()
bot = Bot(token, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    keyboard = consts.getGlobalKeyboard()
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    await message.answer(f"Добро пожаловать!", reply_markup=keyboard)


@dp.callback_query(F.data == "start")
async def query_random(callback: types.CallbackQuery):
    keyboard = consts.getGlobalKeyboard()
    await callback.message.edit_text(f"Добро пожаловать!", reply_markup=keyboard)


@dp.callback_query(F.data == "balance")
async def cmd_balance(callback: types.CallbackQuery):
    balance = 5000.00
    keyboard = consts.getBackKeyboard()
    await callback.message.edit_text(f"Ваш баланс {balance} 💸", reply_markup=keyboard)


@dp.callback_query(F.data == "history_bet")
async def cmd_historyBet(callback: types.CallbackQuery):
    history = "Example history"
    keyboard = consts.getBackKeyboard()
    await callback.message.edit_text(f"Ваша история {history}", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
