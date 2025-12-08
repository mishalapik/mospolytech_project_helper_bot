from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Static:
    '''Класс статических клавиатур'''

    main_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='✈️ Навигатор по проекту', callback_data='main_menu-project_nav')],
            [InlineKeyboardButton(text='❔ Словарь(FAQ)', callback_data='main_menu-faq')]
        ]
    )
    