from pyrogram.types import InlineKeyboardButton

import config
from MOONMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="💘 𝐆𝚁𝙾𝚄𝙿 💘", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="💘 𝐆𝐀𝐋𝐀𝐗𝐘 💘", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="💘 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 💘", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="💘  𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 💘 ", callback_data="settings_back_helper")
        ],
    ]
    return buttons
