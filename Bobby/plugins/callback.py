from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏ !
ᴛʜɪs ɪs ʀᴀɪᴅᴇɴ ᴍᴜsɪᴄ sʏsᴛᴇᴍ ᴡɪᴛʜ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗂 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cmds")                    
                ]                                
           ]
        ),
    )
