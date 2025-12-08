from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery

from inline.general import Static as general_inline_static
from inline.project_steps import Static as project_steps_inline_static
from inline.project_steps import Dynamic as project_steps_inline_dynamic


from texts.project_steps import project_steps
from menus.general import Static as general_static_menus
from menus.general import Dynamic as general_dynamic_menus
router = Router()



@router.callback_query(F.data.startswith('main_menu'))
async def main_menu_handler(call:CallbackQuery):
    option = call.data.split('-')[1]
    print(option)
    if option == "project_nav":
        await call.message.edit_caption(**general_static_menus.project_nav)

        await call.answer()
        return


@router.callback_query(F.data.startswith("project_nav"))
async def project_navigation_main_handler(call:CallbackQuery):
    step_number = int(call.data.split('-')[1])

    await call.message.edit_caption(
        **(await general_dynamic_menus.step(step_number))
    )
    await call.answer()


@router.callback_query(F.data.startswith("step_nav"))
async def step_nav_handler(call:CallbackQuery):
    step_number, option = call.data.split('-')[1:]
    print(option)

    if option == 'documents':
        await call.message.edit_caption(
                **(await general_dynamic_menus.required_documents_for_step(step_number))
            )
    elif option == 'prev_step':
        if step_number == 1:
            return
        else:
            new_step_number = int(step_number)-1
            await call.message.edit_caption(
                **(await general_dynamic_menus.step(new_step_number))
            )
    elif option == 'next_step':
        if step_number == 7:
            return
        else:
            new_step_number = int(step_number)+1
            await call.message.edit_caption(
                **(await general_dynamic_menus.step(new_step_number))
                # caption=project_steps[new_step_number]["title"],
                # reply_markup=await project_steps_inline_dynamic.step_nav(new_step_number)
            )
    elif option == 'to_main':
        await call.message.edit_caption(**general_static_menus.project_nav)

    await call.answer()

@router.callback_query(F.data.startswith('document'))
async def document_menu_handler(call:CallbackQuery):
    step_number,info = call.data.split('-')[1:]
    print(step_number,info)
    if info=='to_step':
        await call.message.edit_caption(**(await general_dynamic_menus.step(int(step_number))))
        await call.answer()

    else:
        await call.message.answer("Присылаем соответствующий документ")
        await call.answer()
