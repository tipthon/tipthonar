# ๐๐๐๐๐๐ค๐ฃ ยฎ
# ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from tpthon import tipthon

from ..core.managers import edit_or_reply
from . import reply_id


@tipthon.ar_cmd(pattern="ุญุงูุงุช ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**โฎ . ุงูุซูุฑ ููู 500 ุญูุงูุงุช ูุงุชูุณ ูุตููุฑุฉ .. ุงุฑุณูู .ุญุงูุงุช ูุงุชุณ ๐ซโฐ**"
        )
    chat = "@amaterody_bot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุญูุงูุงุช ูุงุชูุณ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1569771593)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @amaterody_bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ุณุชูุฑู ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ . ุงูุซูุฑ ููู 1000 ุณุชููุฑูุงุช ุงูููู ูุตููุฑุฉ ููุทูุฑูููู.. ุงุฑุณูู .ุณุชูุฑู ุงููู ๐ซโฐ**",
        )
    chat = "@Chhhbbot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุณูุชูุฑู ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1915672327)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Chhhbbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ููุฏ ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ . ุงูุซูุฑ ููู 1000 ุงูุชูุงุฑุงุช ุงูููู ุดุจูุงุจ ููุทูุฑูููู.. ุงุฑุณูู .ููุฏ ุงููู ๐ซโฐ**",
        )
    chat = "@ZelTrbot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1354728480)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZelTrbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ุจูุช ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ . ุงูุซูุฑ ููู 1000 ุงูุชูุงุฑุงุช ุงูููู ุจููุงุช ููุทูุฑูููู.. ุงุฑุณูู ..ุจูุช ุงููู ๐ซโฐ**",
        )
    chat = "@Maroooosh_bot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1000915223)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Maroooosh_bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ุฑุฒุฒ ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ ููู ุจุงุถุงููุฉ ุฑูููู? ูู 130 - 1 ููุงููุฑ . . ูุซูุงู ( .ุฑุฑ 1 ) ...๐ซโฐ**",
        )
    chat = "@QQY_98BOT"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2088144968)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @QQY_98BOT .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ุฑููู ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**โฎ . ุงูุซูุฑ ูู 200 ุฑูููู ุดุฑุนููู .. ุตูุฏูู ุฌูุงุฑููู ๐ซโฐ**"
        )
    chat = "@ZlZZl77bot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุฑูููู ุงูุดูุฑุนูู ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1956894280)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZlZZl77bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ุฒุฒ ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ ููู ุจุงุถุงููุฉ ุฑูููู? ูู 130 - 1 ููุงููุฑ . . ูุซูุงู ( .ุฒุฒ 1 ) ...๐ซโฐ**",
        )
    chat = "@SSSS_sssiBOT"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2076530727)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @SSSS_sssiBOT .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ุจูุณุช ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ ููู ุจุงุถุงููุฉ ุฑูููู? ูู 29 - 1 ููุงููุฑ . . ูุซูุงู ( .ุจูุณุช 1 ) ...๐ซโฐ**",
        )
    chat = "@Zedthonbot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุชุญููู ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1863051724)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Zedthonbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@tipthon.ar_cmd(pattern="ุญุจ ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**โฎ ููู ุจุงุถุงููุฉ ุฑูููู? ูู 57 - 1 ููุงููุฑ . . ูุซูุงู ( .ุญุจ 1 ) ...๐ซโฐ**"
        )
    chat = "@ZlZZl777BOT"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุชุญููู ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2099294312)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZlZZl777BOT .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)
