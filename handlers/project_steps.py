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
        await call.message.edit_media(**general_static_menus.project_nav)

        await call.answer()
        return


@router.callback_query(F.data.startswith("project_nav"))
async def project_navigation_main_handler(call:CallbackQuery):
    option = call.data.split('-')[1]
    if option == "back":
        return await call.message.edit_media(
            **(general_static_menus.main_back)
        )
    else:
        step_number = int(call.data.split('-')[1])

        await call.message.edit_media(
            **(await general_dynamic_menus.step(step_number))
        )
        await call.answer()


@router.callback_query(F.data.startswith("step_nav"))
async def step_nav_handler(call:CallbackQuery):
    step_number, option = call.data.split('-')[1:]
    print(option)

    if option == 'documents':
        await call.message.edit_media(
                **(await general_dynamic_menus.required_documents_for_step(step_number))
            )
    elif option == 'prev_step':
        if step_number == 1:
            return
        else:
            new_step_number = int(step_number)-1
            await call.message.edit_media(
                **(await general_dynamic_menus.step(new_step_number))
            )
    elif option == 'next_step':
        if step_number == 7:
            return
        else:
            new_step_number = int(step_number)+1
            await call.message.edit_media(
                **(await general_dynamic_menus.step(new_step_number))
                # caption=project_steps[new_step_number]["title"],
                # reply_markup=await project_steps_inline_dynamic.step_nav(new_step_number)
            )
    elif option == 'to_main':
        await call.message.edit_media(**general_static_menus.project_nav)

    await call.answer()

@router.callback_query(F.data.startswith('document'))
async def document_menu_handler(call:CallbackQuery):
    step_number,info = call.data.split('-')[1:]
    # print(step_number,info)
    if info=='back_to_step':
        await call.message.edit_media(**(await general_dynamic_menus.step(int(step_number))))
        await call.answer()

    else:
        #тут работаем
        await call.message.edit_media(
            **(await general_dynamic_menus.specific_document_for_step(step_number,int(info)))
            )
        await call.answer()


@router.callback_query(F.data.startswith("spec_document"))
async def specific_document_handler(call:CallbackQuery):
    step_number,info = call.data.split('-')[1:]

    if info == 'back':
        await call.message.edit_media(
            **(await general_dynamic_menus.required_documents_for_step(step_number))
        )
        await call.answer()
    else:
        from texts.project_documents import project_documents
        document_number = int(info)
        step_documents = project_documents[int(step_number)]
        document = step_documents[document_number]

        await call.message.answer_document(
            document=document["file_id"],
            caption = document["name"]
        )

        await call.answer()
