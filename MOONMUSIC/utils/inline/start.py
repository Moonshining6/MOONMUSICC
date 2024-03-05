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
            InlineKeyboardButton(text="★ 𝗚𝗥𝗢𝗨𝗣 ★", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="★ 𝗦𝗘𝗧 ★", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="★ 𝗚𝗥𝗢𝗨𝗣 ★", url=config.SUPPORT_CHAT),
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
            InlineKeyboardButton(text="★ 𝗚𝗔𝗟𝗔𝗫𝗬 ★", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="★ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ★", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="★ 𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦 ★ ", callback_data="settings_back_helper")
        ],
    ]
    return buttons
