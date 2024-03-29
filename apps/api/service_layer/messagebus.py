# pylint: disable=broad-except, attribute-defined-outside-init
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Callable, Dict, Type, Union

from apps.api.domain import commands

if TYPE_CHECKING:
    from . import unit_of_work

logger = logging.getLogger(__name__)

Message = Union[commands.Command]


class MessageBus:
    def __init__(
        self,
        uow: unit_of_work.AbstractUnitOfWork,
        command_handlers: Dict[Type[commands.Command], Callable],
    ):
        self.uow = uow
        self.command_handlers = command_handlers

    def handle(self, message: Message):
        if isinstance(message, commands.Command):
            return self.handle_command(message)
        else:
            raise Exception(f'{message} was not an Event or Command')

    def handle_command(self, command: commands.Command):
        logger.debug('handling command %s', command)
        try:
            handler = self.command_handlers[type(command)]
            return handler(command)
        except Exception:
            logger.exception('Exception handling command %s', command)
            raise
