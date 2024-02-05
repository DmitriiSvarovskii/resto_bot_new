from aiogram.types import Message

from src.db import customer_db
from src.keyboards.main_keyboards import create_keyboard_main
from src.lexicons.lexicon_ru import LEXICON_RU


async def process_start_command(message: Message):

    await customer_db.create_new_user_on_start(message=message)

    keyboard = await create_keyboard_main(message.chat.id)

    await message.answer(
        text=LEXICON_RU['start'],
        reply_markup=keyboard
    )
