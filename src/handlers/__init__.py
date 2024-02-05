from aiogram import Router
from aiogram.filters import CommandStart
from . import handlers_start


def register_user_commands(router: Router) -> None:
    router.message.register(
        handlers_start.process_start_command, CommandStart()
    )
