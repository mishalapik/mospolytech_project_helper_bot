from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts.project_steps import project_documents


class Static:
    project_nav = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Предпроектная подготовка',callback_data='project_nav-1-preparation')],
            [InlineKeyboardButton(text='Экспертиза',callback_data='project_nav-2-expertise')],
            [InlineKeyboardButton(text='Инициация проекта',callback_data='project_nav-3-initiation')],
            [InlineKeyboardButton(text='Планирование проекта',callback_data='project_nav-4-planning')],
            [InlineKeyboardButton(text='Реализация и контроль',callback_data='project_nav-5-relisation_control')],
            [InlineKeyboardButton(text='Закрытие проекта',callback_data='project_nav-6-closure')],
            [InlineKeyboardButton(text='Перевод в операционную фазу',callback_data='project_nav-7-operating_phase')]
        ]
    )

class Dynamic:

    async def step_nav(step_number:int)->InlineKeyboardMarkup:
        step_nav = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Документы',callback_data=f'step_nav-{step_number}-documents')],
                [
                    InlineKeyboardButton(text='<',callback_data=f'step_nav-{step_number}-prev_step'),
                    InlineKeyboardButton(text='>',callback_data=f'step_nav-{step_number}-next_step')
                ],
                [InlineKeyboardButton(text='Назад',callback_data=f'step_nav-{step_number}-to_main')]
            ]
        )

        return step_nav
    
    async def document_list_for_step(step_number:int)->InlineKeyboardMarkup:
        inline_keyboard = []
        names = [x["name"] for x in project_documents[int(step_number)]]
        for i in range(len(names)):
            inline_keyboard.append([InlineKeyboardButton(text=names[i],callback_data=f"document-{step_number}-{i}")])
        inline_keyboard.append([InlineKeyboardButton(text='Назад',callback_data=f'document-{step_number}-to_step')])

        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return keyboard