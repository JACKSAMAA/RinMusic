import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

from time import time
from datetime import datetime

from Bobby.setup.filters import command
from Bobby.config import SUPPORT

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""𝗕𝗮𝗸𝗮𝗮 {message.from_user.mention()} 🙂
𝗧𝗵𝗶𝘀 𝗜𝘀 𝗞𝗼𝘂𝘀𝗲𝗶 𝗔𝗿𝗶𝗺𝗮 𝗠𝘂𝘀𝗶𝗰 𝗦𝘆𝘀𝘁𝗲𝗺 𝗪𝗶𝘁𝗵 𝗔 𝗟𝗼𝘁 𝗢𝗳 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝗕𝗮𝘀𝗲𝗱 𝗢𝗻 𝗔.𝗜 𝗔𝗻𝗱 𝗛𝗶𝗴𝗵 𝗦𝗼𝘂𝗻𝗱 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗢𝗳 𝗦𝗼𝗻𝗴𝘀.
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀", callback_data="cmds")                    
                ]                               
           ]
        ),
    )


@Client.on_message(command(["ping"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("𝗣𝗶𝗻𝗴..... 👀")
    delta_ping = time() - start
    await m_reply.edit_text("𝗣𝗼𝗻𝗴.... 🙂\n" f"`{delta_ping * 1000:.3f} ᴍx`")
