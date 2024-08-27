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
                BotCommand("birthday", "spam the chat with birthday message"),
                BotCommand("restart", "Restart The Bot"),
                BotCommand("eval", "Run Python Code"),
                BotCommand("exec", "Install The Requirements"),
                BotCommand("gm", "Spam The Chat with good morning message"),
                BotCommand("ga", "Spam The Chat With Good Afternoon Messages")
            ]
        )
    except:
        pass

