from aiogram.types import Message
from typing import Optional

from src.crud.customer_crud import add_tg_user, get_user
from src.database import get_async_session
from src.schemas.customer_schemas import CreateCustomer, ReadCustomerInfo


async def create_new_user_on_start(message: Message):
    async for session in get_async_session():
        if message.text.strip() == "/start":
            resourse = None
        else:
            resourse = message.text.replace("/start", "").strip()
        new_customer_data = (
            CreateCustomer(
                user_id=message.from_user.id,
                resourse=resourse,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username,
            )
        )
        await add_tg_user(
            data=new_customer_data,
            session=session
        )
        break


async def get_user_info_from_db(user_id: int) -> Optional[ReadCustomerInfo]:
    async for session in get_async_session():
        respone = await get_user(
            user_id=user_id,
            session=session
        )
        break
    return respone
