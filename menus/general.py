from inline.general import Static as general_inline_static
from inline.project_steps import Static as project_steps_inline_static
from inline.project_steps import Dynamic as project_steps_inline_dynamic
from media.media_ids import Media_IDs
from texts.project_steps import project_steps as steps_texts

class Static:
    main_menu = {
        'photo' : Media_IDs.main_picture_id,
        'caption' : 'Приветственное сообщение',
        'reply_markup' : general_inline_static.main_menu
    }

    project_nav = {
        'photo' : Media_IDs.main_picture_id,
        'caption' : 'Текст для навигации по шагам реализации проекта',
        'reply_markup' : project_steps_inline_static.project_nav
    } 

    

class Dynamic:
    async def step(step_number:int)->dict:
        step = {
                'caption':f'{step_number}. {steps_texts[step_number]["title"]}\n\n{steps_texts[step_number]["description"]}\n\nЧто нужно делать?\n{steps_texts[step_number]["student_actions"]}',
                'reply_markup':await project_steps_inline_dynamic.step_nav(step_number)
            }
        
        return step
    
    async def required_documents_for_step(step_number:int)->dict:
        step = {
                'caption':f'Необходимые документы на текущем шаге:',
                'reply_markup':await project_steps_inline_dynamic.document_list_for_step(step_number)
            }
        
        return step