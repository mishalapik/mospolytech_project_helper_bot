from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery

from menus.general import Static as menu_static

from inline.general import Static

router = Router()


@router.message(Command("start"))
async def start_command(message:Message,command:CommandObject):
    await message.answer_photo(**menu_static.main_menu)
    


@router.message(F.photo)
async def handle_photo(message: Message):
    # Получаем file_id самой большой версии фото
    file_id = message.photo[-1].file_id
    await message.reply(file_id)
