
@bot.on(admin_cmd(outgoing=True, pattern="gaali$"))
@bot.on(sudo_cmd(pattern="gaali$", allow_sudo=True))
async def cat(event):
    await edit_or_reply(
        event,
)
