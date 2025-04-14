from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ  ❰ 𝗗𝗥𝗫 𝆺𝅥𝅃꯭𝗡𝗘𝗧𝗪𝗢𝗥𝗞 ❱ ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @DRX_SUPPORTCHAT ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/lll_DRX_NETWORK_lll"),
          InlineKeyboardButton("❰ 𝗗𝗥𝗫 𝆺𝅥𝅃꯭𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ❱", url="https://t.me/DRX_SUPPORTCHAT"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗗𝗥𝗫 𝆺𝅥𝅃꯭𝗕ᴏᴛs", url=f"https://t.me/lll_DRX_NETWORK_lll"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/EMPERORMUSIC_PROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/5musfg.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
