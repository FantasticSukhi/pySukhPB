from pyrogram.types import InlineKeyboardButton

async def start_cmd(Badmunda):
    x = await Badmunda.get_me()
    START_OP = [
        [
            InlineKeyboardButton(
                text="🌸 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌸", url=f"https://t.me/CENSORED_POLITICSSS"
            ),
            InlineKeyboardButton(
                text="💥 sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/MBV_CHATS"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👻 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ  👻",
                url=f"https://t.me/{x.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📂 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📂", url=f"https://xhamster.com"
            ),
            InlineKeyboardButton(
                text="✨ ᴜᴘᴅᴀᴛᴇ ✨", url=f"https://t.me/MBV_NETWORK"
            ),
        ],
    ]
    return START_OP
  
