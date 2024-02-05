from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from src.models import Store
from src.schemas.store_schemas import ReadStore


async def crud_get_store_info(
    session: AsyncSession
) -> Optional[ReadStore]:
    query = (
        select(Store)
    )
    result = await session.execute(query)
    store = result.scalar()
    return store


async def crud_change_is_active_bot(
    session: AsyncSession,
):
    stmt = (
        update(Store)
        .values(is_active=~Store.is_active)
    )

    await session.execute(stmt)
    await session.commit()
    return {"message": "Статус для is_active изменен"}
