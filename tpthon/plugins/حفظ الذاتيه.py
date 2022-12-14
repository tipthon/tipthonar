from asyncio import sleep

from tpthon import tipthon
from tpthon.core.logger import logging

from ..sql_helper.globals import gvarstatus

plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

POSC = gvarstatus("Z_POSC") or "(مم|ذاتية|ذاتيه|جلب الوقتيه)"


@tipthon.ar_cmd(pattern=f"{POSC}(?: |$)(.*)")
async def oho(event):
    if not event.is_reply:
        return await event.edit("**- ❝ ⌊بالـرد علـى صورة ذاتيـة التدميـر 𓆰...**")
    zzzzl1l = await event.get_reply_message()
    pic = await zzzzl1l.download_media()
    await tipthon.send_file(
        "me", pic, caption=f"**- ❝ ⌊تـم حفـظ الصـورة ذاتيـة التدمير بنجـاح ☑️ 🥳𓆰...**"
    )
    await event.delete()


@tipthon.ar_cmd(
    pattern="تست (\d*) ([\s\S]*)",
    command=("sdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time.",
        "الاسـتخـدام": "{tr}sdm [number] [text]",
        "مثــال": "{tr}sdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()


@tipthon.ar_cmd(
    pattern="محترقه (\d*) ([\s\S]*)",
    command=("selfdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time. and in message will show the time.",
        "الاسـتخـدام": "{tr}selfdm [number] [text]",
        "مثــال": "{tr}selfdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    text = message + f"\n\n`This message shall be self-destructed in {ttl} seconds`"

    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()
