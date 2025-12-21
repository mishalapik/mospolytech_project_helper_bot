from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts.project_documents import project_documents


class Static:
    project_nav = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='1. 💡 Предпроектная подготовка',callback_data='project_nav-1-preparation')],
            [InlineKeyboardButton(text='2. 🔍 Экспертиза',callback_data='project_nav-2-expertise')],
            [InlineKeyboardButton(text='3. 🎬 Инициация проекта',callback_data='project_nav-3-initiation')],
            [InlineKeyboardButton(text='4. 🗺️ Планирование проекта',callback_data='project_nav-4-planning')],
            [InlineKeyboardButton(text='5. 🏗️ Реализация и контроль',callback_data='project_nav-5-relisation_control')],
            [InlineKeyboardButton(text='6. 🏆 Закрытие проекта',callback_data='project_nav-6-closure')],
            [InlineKeyboardButton(text='7. 🤝 Перевод в операционную фазу',callback_data='project_nav-7-operating_phase')],
            [InlineKeyboardButton(text='🔙 Назад',callback_data='project_nav-back')]

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
        from texts.project_documents import project_documents
        documents = project_documents[int(step_number)]
        for i in range(len(documents)):
            document = documents[i]
            if document["has_template"] == True:
                inline_keyboard.append([InlineKeyboardButton(
                    text=f"{i+1}. 📝 {document['name']}",callback_data=f"document-{step_number}-{i}"
                    )])
            else:
                inline_keyboard.append([InlineKeyboardButton(
                    text=f"{i+1}. ✏️ {document['name']}",callback_data=f"document-{step_number}-{i}"
                    )])

        inline_keyboard.append([InlineKeyboardButton(text='Назад',callback_data=f'document-{step_number}-back_to_step')])

        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return keyboard
    
    async def specific_document(step_number:int, document_number:int):
        from texts.project_documents import project_documents

        inline_keyboard = []
        
        documents = project_documents[int(step_number)]

        document = documents[document_number]

        if document["has_template"] == True:
            inline_keyboard.append(
                [InlineKeyboardButton(
                    text=f"📥 Скачать шаблон",callback_data=f"spec_document-{step_number}-{document_number}")]
                    )
        inline_keyboard.append(
            [InlineKeyboardButton(
                text = "🔙 Назад",
                callback_data=f"spec_document-{step_number}-back"
            )]
        )

        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return keyboard
        