from pyrogram.types import BotCommand


async def start_bot(Client):
    await Client.start()
    try:
        x = await Client.get_me()
        print(f"Client - [INFO]: @{x.username} get started ")
    except Exception as e:
        print(f"Error - {e}")
    try:
        print("Settings All Commands")
        await Client.set_bot_commands(
            [
                BotCommand("start", "sᴛᴀʀᴛ ʙᴏᴛ ʙʏ ᴀɴʏᴏɴᴇ"),
                BotCommand("ping", "ᴄʜᴇᴄᴋ ᴛʜᴀᴛ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ"),
                BotCommand("banall", "ʙᴀɴᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀ ɪɴ ɢʀᴏᴜᴘ"),
                BotCommand("birthday", "sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙɪʀᴛʜᴅᴀʏ ᴍᴇssᴀɢᴇ"),
                BotCommand("restart", "ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
                BotCommand("eval", "ʀᴜɴ ᴘʏᴛʜᴏɴ ᴄᴏᴅᴇ"),
                BotCommand("exec", "ɪɴsᴛᴀʟʟ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴍᴇɴᴛs"),
                BotCommand("gm", "sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴍᴇssᴀɢᴇ"),
                BotCommand("ga", "sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ ᴍᴇssᴀɢᴇs")
            ]
        )
    except:
        pass

