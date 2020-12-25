import asyncio
import random

from . import catmemes

@bot.on(outgoing=True, pattern="merry$")
@bot.on(pattern="merry$", allow_sudo=True)
async def cat(event):
    await edit_or_reply(
        event, MERRY CHRISTMAS TO YOU TOO DEAR!!!
)
import random

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async
