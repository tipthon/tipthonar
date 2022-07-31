import asyncio

import heroku3
import urllib3
from telegraph import Telegraph

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from tpthon import tipthon

from ..Config import Config
from ..core.managers import edit_or_reply
from ..sql_helper.globals import addgvar, gvarstatus

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY


plugin_category = "الادوات"


telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


TipthonVP_cmd = (
    "𓆩 [𝗧𝗶𝗽𝘁𝗵𝗼𝗻 𝗮𝗟 𝗔𝗿𝗮𝗯 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر الفـارات](t.me/E9N99) 𓆪\n\n"
    "**✾╎قائـمه اوامـر تغييـر زخـارف البروفايـل + الاسـم الوقـتي بأمـر واحـد فقـط - حقـوق لـ التـاريـخ 🦾 :** \n\n"
    "⪼ `.وقتيه 1` / `.الوقتي 1`\n\n"
    "⪼ `.وقتيه 2` / `.الوقتي 2`\n\n"
    "⪼ `.وقتيه 3` / `.الوقتي 3`\n\n"
    "⪼ `.وقتيه 4` / `.الوقتي 4`\n\n"
    "⪼ `.وقتيه 5` / `.الوقتي 5`\n\n"
    "⪼ `.وقتيه 6` / `.الوقتي 6`\n\n"
    "⪼ `.وقتيه 7` / `.الوقتي 7`\n\n"
    "⪼ `.وقتيه 8` / `.الوقتي 8`\n\n"
    "⪼ `.وقتيه 9` / `.الوقتي 9`\n\n"
    "⪼ `.وقتيه 10` / `.الوقتي 10`\n\n"
    "⪼ `.وقتيه 11` / `.الوقتي 11`\n\n"
    "⪼ `.وقتيه 12` / `.الوقتي 12`\n\n"
    "⪼ `.وقتيه 13` / `.الوقتي 13`\n\n"
    "⪼ `.وقتيه 14` / `.الوقتي 14`\n\n"
    "⪼ `.وقتيه 15`\n\n"
    "⪼ `.وقتيه 16`\n\n"
    "⪼ `.وقتيه 17`\n\n\n"
    "🛃 سيتـم اضـافة المزيـد من الزغـارف بالتحديثـات الجـايـه\n\n"
)


@tipthon.ar_cmd(pattern="وقتيه(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.pattern_match.group(1)
    app.config()
    zed = await edit_or_reply(
        event, "**✾╎جـاري اضـافة زخـرفـة الوقتيـه لـ بوتـك 💞🦾 . . .**"
    )

    if input_str == "1":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/ZThon.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "2":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Starjedi.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "3":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Papernotes.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "4":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Terserah.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "5":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Photography Signature.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "6":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Austein.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "7":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Dream MMA.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "8":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/EASPORTS15.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "9":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/KGMissKindergarten.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "10":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/212 Orion Sans PERSONAL USE.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "11":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/PEPSI_pl.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "12":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Paskowy.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "13":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Cream Cake.otf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "14":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Hello Valentina.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "15":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Alien-Encounters-Regular.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "16":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/Linebeam.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)
    elif input_str == "17":
        variable = "DEFAULT_PIC"
        zinfo = "tpthon/helpers/styles/EASPORTS15.ttf"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_PIC") is None:
            await zed.edit(
                "**✾╎تم اضـافـة زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفـة البروفـايل الوقـتي {} بنجـاح ☑️**\n\n**✾╎الان قـم بـ ارسـال الامـر ↶** `.البروفايل` **لـ بـدء البروفـايل الوقتـي . .**".format(
                    input_str
                )
            )
        addgvar(variable, zinfo)


@tipthon.ar_cmd(pattern="الوقتي(?:\s|$)([\s\S]*)")
async def hhhzelzal(event):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.pattern_match.group(1)
    heroku_var = app.config()
    zed = await edit_or_reply(
        event, "**✾╎جـاري اضـافة زخـرفـة الوقتيـه لـ بوتـك 💞🦾 . . .**"
    )

    if input_str == "1":
        variable = "ZI_FN"
        zinfo = "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "2":
        variable = "ZI_FN"
        zinfo = "𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "3":
        variable = "ZI_FN"
        zinfo = "١٢٣٤٥٦٧٨٩٠"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "4":
        variable = "ZI_FN"
        zinfo = "₁₂₃₄₅₆₇₈₉₀"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "5":
        variable = "ZI_FN"
        zinfo = "¹²³⁴⁵⁶⁷⁸⁹⁰"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "6":
        variable = "ZI_FN"
        zinfo = "➊➋➌➍➎➏➐➑➒✪"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "7":
        variable = "ZI_FN"
        zinfo = "❶❷❸❹❺❻❼❽❾⓿"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "8":
        variable = "ZI_FN"
        zinfo = "➀➁➂➃➄➅➆➇➈⊙"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "9":
        variable = "ZI_FN"
        zinfo = "⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "10":
        variable = "ZI_FN"
        zinfo = "①②③④⑤⑥⑦⑧⑨⓪"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "11":
        variable = "ZI_FN"
        zinfo = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "12":
        variable = "ZI_FN"
        zinfo = "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "13":
        variable = "ZI_FN"
        zinfo = "𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo
    elif input_str == "14":
        variable = "ZI_FN"
        zinfo = "１２３４５６７８９０"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit(
                "**✾╎تم تغييـر زغـرفة الاسـم الوقتـي {} بنجـاح ☑️**\n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        else:
            await zed.edit(
                "**✾╎تم اضـافة زغـرفة الاسـم الوقتـي {} بنجـاح ☑️** \n**✾╎بعـد اعـادة التشغيـل ارسـل ↶** `.الاسم تلقائي`\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(
                    input_str
                )
            )
        heroku_var[variable] = zinfo


@tipthon.ar_cmd(pattern="اوامر الوقتي")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, TipthonVP_cmd)
