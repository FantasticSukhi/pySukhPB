from pyrogram.types import InlineKeyboardButton

async def start_cmd(Badmunda):
    x = await Badmunda.get_me()
    START_OP = [
        [
            InlineKeyboardButton(
                text="🌸 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌸", url=f"https://t.me/ll_BAD_MUNDA_ll"
            ),
            InlineKeyboardButton(
                text="💥 sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/PBX_CHAT"
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
                text="📂 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📂", url=f"https://t.me/HEROKUBIN_01/139"
            ),
            InlineKeyboardButton(
                text="✨ ᴜᴘᴅᴀᴛᴇ ✨", url=f"https://t.me/HEROKUBIN_01"
            ),
        ],
    ]
    return START_OP
  
