import asyncio
import random

from . import catmemes

@bot.on(outgoing=True, pattern="merry$")
@bot.on(pattern="merry$", allow_sudo=True)
async def cat(event):
    await edit_or_reply(
        event, MERRY CHRISTMAS TO YOU TOO DEAR!!!
)
