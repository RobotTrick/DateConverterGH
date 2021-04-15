from typing import Union
from pyrogram.types import InlineQueryResultArticle as InRes, InputTextMessageContent as InTXT
from pyrogram.types import *


class Msg:

    today_btn = "התאריך היום"
    convert_btn = "המרת תאריך"
    error_format = "פורמט שגוי. לחץ כאן!"
    error_unknow = "שגיאה לא ידועה :("
    nav_btn = 'להסבר שימוש לחץ כאן'

    def json_to_msg(json: dict, answer: bool = False) -> Union[str, InRes]:
        full_ge = lambda d: f"{d['gd']}/{d['gm']}/{d['gy']}"

        if not answer:
            msg = f'**תאריך עברי:** {json["hebrew"]}\n\n'
            msg += f'**תאריך לועזי:** {full_ge(json)}'
            return msg

        else:
            res = InRes(
                json['hebrew'] + " ~ " + full_ge(json),
                InTXT(f"**תאריך עברי:** {json['hebrew']}\n\n**תאריך לועזי:** {full_ge(json)}")
            )
            return res

    def format_help(message: Message):
        txt = "שימו לב, החיפוש תומך במגוון רחב של פורמטים לנוחיותכם.\n"
        txt += "לדוגמה, תוכלו להשתמש באחד מהפורמטים הבאים:\n"
        txt += """```כ"א סיוון תשע"א
ט' כסליו תש"פ
א סיון תשעז

```"""
        txt += "ובמקביל, בלועזי:\n"
        txt += """```01/12/2021
1-5-15
23 10 1999```

"""
        txt += "עם זאת, הבוט תומך כרגע בטווח תאריכים הגיוני ונורמלי, ללא התחייבות לתאריכים רחוקים מידי."

        message.reply(txt, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("לחיפוש תאריך", switch_inline_query_current_chat="")]]
        ))

    def start_msg(msg: Message):
        txt = f"""היי {msg.from_user.mention}!
ברובוט זה תוכל/י להמיר תאריך עברי ללועזי, וההפך.
אופן השימוש פשוט וקל, הקלידו בשורת הצ'אט את התיוג של הבוט, ואחריו את התאריך שתרצו להמיר. הרובוט יענה לכם עם התאריך המבוקש בלועזי ובעברית.
מעוניינים בעוד פירוט? שלחו לבוט /help."""

        return txt
