from telethon import events
@bot.on(events.NewMessage(pattern="plugin", outgoing= True))
async def hi(event):
  await event.reply("""
`from telethon import events
@bot.on(events.NewMessage(pattern="", outgoing= True))
async def hi(event):`

`from userbot.utils import admin_cmd
@bot.on(admin_cmd(pattern=""))
async def hi(event):`

`@ultroid_cmd(pattern="")
async def hi(event):`

`from .. import *
@catub.cat_cmd(pattern="")
async def hi(event):`

`await bot.send_message(event.chat_id)`

`await event.respond()`
""")

