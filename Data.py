from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("⩩ بدء استخراج الجلسة ☆.", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="⩩ الصفحة الرئيسية ☆.", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "●○𝐑𝐄𝐅𝐙○●", url="https://t.me/def_Zoka"
            )
        ],
        [
            InlineKeyboardButton("طريقة استخدام البوت ☆", callback_data="help"),
            InlineKeyboardButton("حول ⩩", callback_data="about"),
        ],
        [InlineKeyboardButton("َժٍᥱُ᥎", url="https://t.me/IC_X_K")],
    ]

    START = """
📟¦اهلا بـك عزيـزي 📬 {},
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة

بواسطـة :  𓆩˹𓏺َِ 𝙎𓏺𝞝𝙉𝙕𝙄𝙍 ٍٍٍٍٍٍّّّّّّّ『المـبـ ـࢪمـج ⏎』🇸🇾↺
    """

    HELP = """
 **الأوامر المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - لاستخراج الجلسات 
/cancel - لإلغاء الاستخراج 
/restart - لترسيت البوت
"""

    # About Message
    ABOUT = """
**حول البوت** 
●○━━━━‌‌‏𝐑𝐄𝐅𝐙━━━━○●
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
⩩ انا بوت استخراج جلسات من سورس ريفز
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
قناة السورس :@def_Zoka
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
َժٍᥱُ᥎ : @IC_K_K
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
●○━━━━‌‌‏𝐑𝐄𝐅𝐙━━━━○●
    """

    # Repo Message
    REPO = """
⋖━━❲𖣂❳━━●○𝐑𝐄𝐅𝐙○●━━❲𖣂❳━━⋗
⩩ انا بوت استخراج جلسات خاص بسورس ريفز
●○━━━━‌‌‏𝐑𝐄𝐅𝐙━━━━○●

⩩ السورس [●○𝐑𝐄𝐅𝐙○●](https://t.me/def_Zoka)

●○━━━━‌‌‏𝐑𝐄𝐅𝐙━━━━○●
إذا كان لديك أي سؤال ، فراسل » المطور » [َժٍᥱُ᥎] @IC_X_K
⋖━━❲𖣂❳━━●○𝐑𝐄𝐅𝐙○●━━❲𖣂❳━━⋗
   """
