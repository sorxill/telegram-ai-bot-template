import asyncio
from aiogram import Bot, Dispatcher
from config.config import settings
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis




async def main():
    from database.session import create_tables
    await create_tables()

    redis = Redis(host=settings.REDIS_HOST)
    storage = RedisStorage(redis=redis)

    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher(storage=storage)

    from bot.handlers import info, echo, start

    dp.include_router(info.router)
    dp.include_router(start.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())