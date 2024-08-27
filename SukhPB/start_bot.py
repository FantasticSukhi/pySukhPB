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
                BotCommand("ga", "sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ ᴍᴇssᴀɢᴇs"),
                BotCommand("gn", "sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴍᴇssᴀɢᴇs"),
                BotCommand("raid", "Sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʀᴀɪᴅ"),
                BotCommand("rraid", "Sᴛᴀʀᴛ ᴛʜᴇ ʀᴀɪᴅ ɪɴ ᴄʜᴀᴛ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴘᴇʀsᴏɴ"),
                BotCommand("draid", "Sᴛᴏᴘ ᴛʜᴇ ʀᴀɪᴅ ɪɴ ᴄʜᴀᴛ"),
                BotCommand("listraid", "ᴄʜᴇᴄᴋ ᴛʜᴇ ʟɪsᴛ ᴏɴ sᴛᴀʀᴛᴇᴅ ʀᴀɪᴅ ᴏɴ ɪᴛ"),
                BotCommand("shayri", "Sᴘᴀᴍ ɪɴ ᴄʜᴀᴛ ᴡɪᴛʜ sʜᴀʏʀɪ"),
                BotCommand("stop", "ᴛᴏ sᴛᴏᴘ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ,ʀᴀɪᴅ,ᴀʙᴜsᴇ"),
                BotCommand("dspam", "sᴛᴀʀᴛ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ᴅᴇʟᴀʏ sᴘᴀᴍ"),
                BotCommand("pspam", "ᴘᴏʀɴsᴘᴀᴍ ᴡɪᴛʜ ʀᴀɪᴅ"),
                BotCommand("hang", "sᴛᴀʀᴛ ʜᴀɴɢ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇᴅ ᴛᴏ ʜᴀɴɢ ᴛʜᴇ ᴄʜᴀᴛ"),
            ]
        )
    except:
        pass

