# animation code for zed edit by @E9N99

import asyncio
from collections import deque
import os
import random
from urllib.parse import quote_plus
from collections import deque
from telethon.tl.types import ChannelParticipantsAdmins
from tpthon.core.logger import logging
from tpthon import tipthon
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, deEmojify, mention


plugin_category = "الترفيه"



@tipthon.ar_cmd(pattern="جو$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@tipthon.ar_cmd(pattern="كليم$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😏/\n/▌ \n/ \\n████\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\😦\n╬╬/▌\n╬╬/\`"
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@tipthon.ar_cmd(pattern="نار$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`"
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@tipthon.ar_cmd(pattern="انتحر$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@tipthon.ar_cmd(pattern="مذاكره$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "`📔📚             📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`"
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@tipthon.ar_cmd(pattern=r"القمر$")
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕",
    )


@tipthon.ar_cmd(pattern=r"مدينه$")
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        """☁️☁️☁️🌞      ☁️     ☁️  ☁️ ☁️
  ☁️ ☁️  ✈️    ☁️    🚁    ☁️    ☁️            
☁️  ☁️    ☁️       ☁️     ☁️   ☁️ ☁️
       🏬🏨🏫🏢🏤🏥🏦🏪🏫
         🌲/         l🚍  \🌳👭
        🌳/  🚘  l 🏃   \🌴 👬                       
 👬🌴/          l  🚔    \🌲
     🌲/   🚖   l              \                               
   🌳/🚶        |   🚍     \ 🌴🚴🚴
  🌴/               |                \🌲""",
    )


Fun8_cmd = (

"**الاوامــر : **"
"  •  `.جو`"
"  •  `.كليم`"
"  •  `.نار`"
"  •  `.انتحر`"
"  •  `.مذاكره`"
"  •  `.القمر`"
"  •  `.مدينه`"
  
"**للنســخ : ** __اضغط ع الامـر لنسخـه__"
)


@tipthon.ar_cmd(pattern="تسليه8")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, Fun8_cmd)
