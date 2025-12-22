from inline.general import Static as general_inline_static
from inline.project_steps import Static as project_steps_inline_static
from inline.project_steps import Dynamic as project_steps_inline_dynamic
from media.media_ids import Media_IDs
from texts.project_steps import project_steps as steps_texts
from aiogram.types import InputMediaPhoto

from texts.project_documents import TextGenerator as document_text_generator
from texts.project_steps import generate_step_text
from texts.general import main_texts



class Static:
    main_menu = {
        'photo' : Media_IDs.main_picture_id,
        'caption' : main_texts.main_info_text,
        'reply_markup' : general_inline_static.main_menu,
        'parse_mode':'HTML'
    }

    main_back={
        'media': InputMediaPhoto(media = Media_IDs.main_picture_id,caption=main_texts.main_info_text),
        'reply_markup' : general_inline_static.main_menu
    }

    project_nav = {
        'media': InputMediaPhoto(media = Media_IDs.navigator_main_id, caption = main_texts.main_step_navigator_text),
        'reply_markup' : project_steps_inline_static.project_nav,
    } 

    

class Dynamic:
    async def step(step_number:int)->dict:

        step = {
                'media' : InputMediaPhoto(media=Media_IDs.steps[step_number-1], caption =  await generate_step_text(step_number)),
                'reply_markup':await project_steps_inline_dynamic.step_nav(step_number)
                
            }
        
        return step
    
    async def required_documents_for_step(step_number:int)->dict:

        
        required_documents_for_step = {
                'media' : InputMediaPhoto(media = Media_IDs.steps[int(step_number)-1], caption =  await document_text_generator.generate_document_list_screen_text(step=int(step_number))),
                'reply_markup':await project_steps_inline_dynamic.document_list_for_step(step_number)
            }
        
        return required_documents_for_step
    

    async def specific_document_for_step(step_number:int,document_number:int)->dict:
        specific_document_for_step = {
            'media' : InputMediaPhoto(media = Media_IDs.steps[int(step_number)-1], caption = await document_text_generator.generate_specific_document_text(int(step_number),int(document_number))),
            'reply_markup':await project_steps_inline_dynamic.specific_document(int(step_number),int(document_number))
        }
        return specific_document_for_step


    
    