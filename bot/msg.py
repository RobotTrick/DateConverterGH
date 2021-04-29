from typing import Union
from pyrogram.types import InlineQueryResultArticle as InRes, InputTextMessageContent as InTXT
from pyrogram.types import *


class Msg:
    today_btn = "🗓 התאריך היום 🗓"
    convert_btn = "🔄 המרת תאריך 🔄"
    error_format = "פורמט שגוי. לחץ כאן 🔘"
    error_unknow = "⚠️ שגיאה לא ידועה ⚠️"
    nav_btn = 'להסבר שימוש לחץ כאן 🔘'


    def json_to_msg(json: dict, answer: bool = False) -> Union[str, InRes]:
        """ convert the answer from the api, to msg format """
        full_ge = lambda d: f"{d['gd']}/{d['gm']}/{d['gy']}"

        if not answer:  # simple telegram message
            msg = f'**תאריך עברי:** {json["hebrew"]}\n\n'
            msg += f'**תאריך לועזי:** {full_ge(json)}'
            return msg

        else:  # inline telegram message
            res = InRes(
                json['hebrew'] + " ~ " + full_ge(json),
                InTXT(f"**תאריך עברי:** {json['hebrew']}\n\n**תאריך לועזי:** {full_ge(json)}"),
                thumb_url="https://telegra.ph/file/2388b677bba4403ee2f7e.png"
            )
            return res


    def format_help(message: Message):
        """ return a help and support message """
        txt = "שימו לב, החיפוש תומך במגוון רחב של פורמטים לנוחיותכם.\n"
        txt += "לדוגמה, תוכלו להשתמש באחד מהפורמטים הבאים:\n"
        txt += "\n`@DateConverterHGbot <תאריך להמרה>`\n\n"
        txt += """```כ"א סיוון תשע"א
ט' כסליו תש"פ
א סיון תשעז

```"""
        txt += "ובמקביל, בלועזי:\n"
        txt += """```01/05/2015
1-5-15
1 5 2015```

"""
        txt += "עם זאת, הבוט תומך כרגע בטווח תאריכים הגיוני ונורמלי, ללא התחייבות לתאריכים רחוקים מידי."
        txt += "\nלחיפוש תאריך בחודש אדר ב', הזינו: `אדר-ב`."

        message.reply(txt, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("לחיפוש תאריך", switch_inline_query_current_chat="")]]
        ))


    def start_msg(msg: Message):
        """ return a start message """
        txt = f"""היי {msg.from_user.mention}! ברובוט זה תוכלו להמיר תאריך עברי ללועזי באופן דו צדדי. אופן השימוש 
        פשוט וקל, הקלידו בכל צ'אט את יוזר הבוט, ואחריו את התאריך שתרצו להמיר. הרובוט יציג בפניכם את התאריך המבוקש 
        בלועזי ובעברי. 

מעוניינים בפירוט נוסף? שלחו לבוט /help.

בוט זה נוצר על ידי [Yeuda-By](t.me/m100achuzMe) מצוות [רובוטריק](t.me/robot_trick_channel)."""

        return txt
