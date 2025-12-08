import aiogram
import logging
import asyncio
import sys

logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

async def main():
    from aiogram import Bot, Dispatcher
    from aiogram.enums import ParseMode
    from aiogram.client.default import DefaultBotProperties
    from handlers import general,project_steps

    from config import BotData

    logger.info("Запуск бота...")
    try:
        bot = Bot(BotData.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        dp = Dispatcher()
        dp.include_routers(general.router,project_steps.router)

        await dp.start_polling(bot)
        logger.info("Бот успешно запущен")
    finally:
        print("Не удалось запустить бот.")


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    asyncio.run(main())
