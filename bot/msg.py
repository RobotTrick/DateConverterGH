from typing import Union
from pyrogram.types import InlineQueryResultArticle as InRes, InputTextMessageContent as InTXT
from pyrogram.types import *


class Msg:
    today_btn = "馃棑 讛转讗专讬讱 讛讬讜诐 馃棑"
    convert_btn = "馃攧 讛诪专转 转讗专讬讱 馃攧"
    error_format = "驻讜专诪讟 砖讙讜讬. 诇讞抓 讻讗谉 馃敇"
    error_unknow = "鈿狅笍 砖讙讬讗讛 诇讗 讬讚讜注讛 鈿狅笍"
    nav_btn = '诇讛住讘专 砖讬诪讜砖 诇讞抓 讻讗谉 馃敇'


    def json_to_msg(json: dict, answer: bool = False) -> Union[str, InRes]:
        """ convert the answer from the api, to msg format """
        full_ge = lambda d: f"{d['gd']}/{d['gm']}/{d['gy']}"

        if not answer:  # simple telegram message
            msg = f'**转讗专讬讱 注讘专讬:** {json["hebrew"]}\n\n'
            msg += f'**转讗专讬讱 诇讜注讝讬:** {full_ge(json)}'
            return msg

        else:  # inline telegram message
            res = InRes(
                json['hebrew'] + " ~ " + full_ge(json),
                InTXT(f"**转讗专讬讱 注讘专讬:** {json['hebrew']}\n\n**转讗专讬讱 诇讜注讝讬:** {full_ge(json)}"),
                thumb_url="https://telegra.ph/file/2388b677bba4403ee2f7e.png"
            )
            return res


    def format_help(message: Message):
        """ return a help and support message """
        txt = "砖讬诪讜 诇讘, 讛讞讬驻讜砖 转讜诪讱 讘诪讙讜讜谉 专讞讘 砖诇 驻讜专诪讟讬诐 诇谞讜讞讬讜转讻诐.\n"
        txt += "诇讚讜讙诪讛, 转讜讻诇讜 诇讛砖转诪砖 讘讗讞讚 诪讛驻讜专诪讟讬诐 讛讘讗讬诐:\n"
        txt += "\n`@DateConverterHGbot <转讗专讬讱 诇讛诪专讛>`\n\n"
        txt += """```讻"讗 住讬讜讜谉 转砖注"讗
讟' 讻住诇讬讜 转砖"驻
讗 住讬讜谉 转砖注讝

```"""
        txt += "讜讘诪拽讘讬诇, 讘诇讜注讝讬:\n"
        txt += """```01/05/2015
1-5-15
1 5 2015```

"""
        txt += "注诐 讝讗转, 讛讘讜讟 转讜诪讱 讻专讙注 讘讟讜讜讞 转讗专讬讻讬诐 讛讙讬讜谞讬 讜谞讜专诪诇讬, 诇诇讗 讛转讞讬讬讘讜转 诇转讗专讬讻讬诐 专讞讜拽讬诐 诪讬讚讬."
        txt += "\n诇讞讬驻讜砖 转讗专讬讱 讘讞讜讚砖 讗讚专 讘', 讛讝讬谞讜: `讗讚专-讘`."

        message.reply(txt, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("诇讞讬驻讜砖 转讗专讬讱", switch_inline_query_current_chat="")]]
        ))


    def start_msg(msg: Message):
        """ return a start message """
        txt = f"""讛讬讬 {msg.from_user.mention}! 讘专讜讘讜讟 讝讛 转讜讻诇讜 诇讛诪讬专 转讗专讬讱 注讘专讬 诇诇讜注讝讬 讘讗讜驻谉 讚讜 爪讚讚讬. 讗讜驻谉 讛砖讬诪讜砖 
        驻砖讜讟 讜拽诇, 讛拽诇讬讚讜 讘讻诇 爪'讗讟 讗转 讬讜讝专 讛讘讜讟, 讜讗讞专讬讜 讗转 讛转讗专讬讱 砖转专爪讜 诇讛诪讬专. 讛专讜讘讜讟 讬爪讬讙 讘驻谞讬讻诐 讗转 讛转讗专讬讱 讛诪讘讜拽砖 
        讘诇讜注讝讬 讜讘注讘专讬. 

诪注讜谞讬讬谞讬诐 讘驻讬专讜讟 谞讜住祝? 砖诇讞讜 诇讘讜讟 /help.

讘讜讟 讝讛 谞讜爪专 注诇 讬讚讬 [Yeuda-By](t.me/m100achuzMe) 诪爪讜讜转 [专讜讘讜讟专讬拽](t.me/robot_trick_channel)."""

        return txt
