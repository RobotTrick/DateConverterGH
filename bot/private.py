from pyrogram import Client, filters
from pyrogram.types import *

from bot.convert import convert, return_month, return_day, return_year, URL
from bot.msg import Msg

import requests


@Client.on_message(filters.text & filters.command("start"))
def start_msg(_, message: Message):
    if len(message.command) > 1:
        Msg.format_help(message)
        return

    message.reply(Msg.start_msg(message),
    disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([
                      [InlineKeyboardButton(Msg.convert_btn, switch_inline_query_current_chat="")],
                      [InlineKeyboardButton(Msg.today_btn, "today")]
                  ]))


@Client.on_callback_query()
def today(_, message: CallbackQuery):
    _2day = requests.get(URL).json()
    message.message.edit_text(Msg.json_to_msg(_2day))


he_re = r"^(?P<day>[א-ת\"' ]{1,4})[ ]+(?P<month>[א-ת-]*)[ ]+(?P<year>[א-ת\"']*)"

@Client.on_inline_query(filters.regex(he_re))
def he2ge(_, inline: InlineQuery):
    groups = inline.matches[0].groupdict()

    if groups["month"].startswith("ב"):
        groups["month"] = groups["month"][1:]

    day, month, year = return_day(groups['day']), return_month(groups['month']), return_year(groups['year'])

    if day and month and year:
        json = convert(day, month, year)
        inline.answer([Msg.json_to_msg(json, True)])

    else:
        inline.answer([], switch_pm_text=Msg.error_format, switch_pm_parameter="format")


ge_re = r"^(?P<day>[0-3]?\d)[ \/.-]*(?P<month>\d{1,2})[ \/.-]*(?P<year>\d{2,4})$"

@Client.on_inline_query(filters.regex(ge_re))
def ge2he(_, inline: InlineQuery):
    groups = inline.matches[0].groupdict()
    day, month, year = int(groups['day']), int(groups['month']), int(groups['year'])

    if day < 33 and month < 13 and year < 2050:

        json = convert(day, month, year, False)

        if not json.get('error'):
            inline.answer([Msg.json_to_msg(json, True)])

        else:
            inline.answer([], switch_pm_text=Msg.error_unknow, switch_pm_parameter="-")

    else:
        inline.answer([], switch_pm_text= Msg.error_format, switch_pm_parameter="format")


@Client.on_inline_query()
def meta(_, inline: InlineQuery):
    if inline.offset == "":
        inline.answer([], switch_pm_text=Msg.nav_btn, switch_pm_parameter="-")


@Client.on_message(filters.command('help'))
def help(_, message: Message):
    Msg.format_help(message)
