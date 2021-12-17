from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_MACBOOK, URL_IPHONE13

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='btn1'),
            KeyboardButton(text='btn2')
        ],
        [
            KeyboardButton(text='btn3')
        ]
    ],
    resize_keyboard=True
)

cb = CallbackData('buy', 'id', 'name', 'price')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Iphone 13', callback_data='buy:0:phone:1000'),
            InlineKeyboardButton(text='MacBook', callback_data='buy:1:mac:999999')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

phone_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Купить', url=URL_IPHONE13)
        ]
    ]
)

mac_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Купить', url=URL_MACBOOK)
        ]
    ]
)