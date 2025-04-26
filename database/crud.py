from sqlalchemy import select
from database.models import User
from database.session import async_session


async def get_or_create_user(user_data: dict):
    async with async_session() as session:
        user_id = int(user_data.get("id"))

        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            user = User(
                id=user_id,
                username=user_data.get('username', ''),
                first_name=user_data.get('first_name', ''),
                last_name=user_data.get('last_name', '')
            )
            session.add(user)
            try:
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
            await session.refresh(user)

        return user