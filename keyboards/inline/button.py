
from telebot.types import InlineKeyboardMarkup

from telebot import types


def keyboard_commands(command: str) -> InlineKeyboardMarkup:
    """
    Функция - создаёт inline-клавиатуру для команд.

    :param command: str
    :return: InlineKeyboardMarkup
    """
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if command == '/start':
        key_help = types.InlineKeyboardButton(text='Help', callback_data='/help')
        keyboard.add(key_help)
    elif command == '/help':
        key_lowprice = types.InlineKeyboardButton(text='Lowprice', callback_data='/lowprice')
        key_highprice = types.InlineKeyboardButton(text='Highprice', callback_data='/highprice')
        key_bestdeal = types.InlineKeyboardButton(text='Bestdeal', callback_data='/bestdeal')
        key_history = types.InlineKeyboardButton(text='History', callback_data='/history')
        keyboard.add(key_lowprice, key_highprice, key_bestdeal, key_history)
    return keyboard
