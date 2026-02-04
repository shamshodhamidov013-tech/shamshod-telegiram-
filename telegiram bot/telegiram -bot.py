from aiogram import Bot, Dispatcher, types,F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
import asyncio

TOKEN = "8429983629:AAFyk9p5fS4M4G8i5HGdDqbeiRNBCzaoN_g"
CHANNELS = ["@Tarjima_kinolar_uzb_tilda_z"]  # Majburiy obuna kanallari
ADMINS = [6000119173]
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Kanallardagi jami obunachilar sonini hisoblaydi (faqat adminlar ko‘radi)
async def get_subs_count():
    total = 0
    for channel in CHANNELS:
        count = await bot.get_chat_member_count(channel)  # aiogram v3 da to‘g‘ri metod
        total += count
    return total
async def check_subs(user_id: int) -> bool:
    for channel in CHANNELS:
        chat_member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        if chat_member.status in ["left", "kicked"]:
            return False
    return True

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if not await check_subs(user_id):
        instagram='movi_uz24'
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [
                [InlineKeyboardButton(text=f"{instagram}",url=f"https://www.instagram.com/movi_uz24?igsh=MTh2Y3U1ZjlmOWNlMA==")],  
                [InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]
            ]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
    else:
        text = "Xush kelibsiz! Botdan foydalanishingiz mumkin."
        if user_id in ADMINS:  # faqat adminlar uchun
            subs_count = await get_subs_count()
            text += f"\n📊 Jami obunachilar soni: {subs_count}"
        await message.answer(text)

@dp.callback_query(lambda call: call.data == "check_subs")
async def check_subs_callback(call: types.CallbackQuery):
    user_id = call.from_user.id
    if await check_subs(user_id):
        text = "Rahmat! Siz barcha kanallarga obuna bo‘lgansiz."
        if user_id in ADMINS:  # faqat adminlar uchun
            subs_count = await get_subs_count()
            text += f"\n📊 Jami obunachilar soni: {subs_count}"
        await call.message.edit_text(text)
    else:
        await call.answer("Siz hali ham barcha kanallarga obuna bo‘lmagansiz!", show_alert=True)



# @dp.message(F.video | F.photo | F.document | F.audio | F.voice)
# async def get_file_id(message: types.Message):
    
#     user_id = message.from_user.id
#     if await check_subs(user_id):
#         if message.video:
#             await message.answer(f"📹 Video File ID: `{message.video.file_id}`")
#     else:
#         await message.answer('telegram kanalga obuna boling')



@dp.message(F.video | F.photo | F.document | F.audio | F.voice)
async def get_file_id(message: types.Message):
    user_id = message.from_user.id

    # Faqat adminlarga ruxsat beramiz
    if user_id in ADMINS:
        if message.video:
            await message.answer(f"📹 Video File ID: `{message.video.file_id}`")
        elif message.photo:
            await message.answer(f"🖼 Photo File ID: `{message.photo[-1].file_id}`")
        elif message.document:
            await message.answer(f"📄 Document File ID: `{message.document.file_id}`")
        elif message.audio:
            await message.answer(f"🎵 Audio File ID: `{message.audio.file_id}`")
        elif message.voice:
            await message.answer(f"🎙 Voice File ID: `{message.voice.file_id}`")
    else:
        await message.answer("🚫 Ushbu buyruq faqat adminlar uchun mavjud!")

@dp.message(F.text == "1") #buyerga kino kodi kiritiladi
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIB7mjffyMGjHamuD2gWpH5dySLil2vAALnFwACI-6BUBpd5hYmbW6NNgQ" #buyerga kino id kiritiladi
        await message.answer_video(file_id, caption="""🎬  🎥 Mening yigitim zombi
📹 Sifati: HD 720p
📆 Yil: 2013
🎞 Janr: Komediya Triller 
🇺🇸 Davlat: AQSH
🇺🇿 Tarjima: O'zbek tilida
🗂 Yuklash: 1028""") #buyerga kino nomi kiritiladi
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
# 📌 2️⃣ Xabar "2" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "2")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAOxaNS-JLwYHlk_BtOjqJhZ58SvqxIAAuMKAAK-hqFKHs6_Ih9v0qI2BA"
        await message.answer_video(file_id, caption="Favqulotda qongiroq")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "3")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAOoaNAkfAxgMB-mjbTUr9fGLGeOTcgAAh0PAAJS5vFIXwwVOys71a02BA"
        await message.answer_video(file_id, caption="""Biz hayvonot bog'ini sotib oldik""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)





@dp.message(F.text == "4")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAO6aNTAuD-P1hkRT54xuNTk2bSw6iUAAhIaAAJqt6FLacWssGdHT242BA"
        await message.answer_video(file_id, caption="""Qo'lingdan Kelsa Tutib Ol [1080p]""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "5")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPLaN06iR9GYw9F0_uTnpByk8Rsa4cAAsENAALrJiBJoLM4cqeecKE2BA"
        await message.answer_video(file_id, caption="""Kino nomi;Fath[1080p]""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "6")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPQaN1VrnDvEYo54rRqJCUZbRVN9ZkAAllPAAK-9NFJx-y63-ouTA42BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: «172 kun» to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 6

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "7")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPTaN1XMwqZe--ck5ImMyitrp9FsW4AAltUAAKIXghJPkDy0sG2Ymc2BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: Jannat onalar oyog'i ostida to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 7

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "8")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPXaN1YgFVyf2HE646zmiOMHi07-i0AAuJUAAILRMhI0DiVpjJPiSk2BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: «Jannat rangi» to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 8

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)



@dp.message(F.text == "9")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPZaN1ZAAGFRzMf6Y1Vh1fEeRfc8YrJAAIULAACR8ugS4DttSPq1kxWNgQ"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: «Iftorlik suvi»  to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 9

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "10")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPvaN4NzWOZiaRpOCHpmYk3ARpDpZEAAoQUAAK4jfFKzLNPlW34YNY2BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: << Muqaddas Zamin>> to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2025-10-02
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 10

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "11")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICF2jfldbQq1IqAdigYvruuqwU0rleAALQIAACoARRSJ0H__nIiycUNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 1-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)



@dp.message(F.text == "12")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAICGWjflp780Dw0cbzBToZ20mpcPRMNAAL1AgAC8uNZRK73OyHZ65ydNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 2-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "13")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICG2jfluaUfww1gzRRhzvM3F5zYDA8AAIOJAACMSdwSJubOHSzH-4GNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 3-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "14")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICHWjflx8SgbJqL1A-94bD1QF43r8tAAIYEAACDD2BUCKbrJhB7G-kNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 4-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "15")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICH2jfl2Ff9v9JHyT5TnQLVtWAYu92AAJuDwACDD2JUB5lmH-5obvPNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 5-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "16")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICIWjfl5AnUoQw6bbALwpRF8-nnq5BAAK5DQACN5mgUFOvXwOGhXsQNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 6-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "17")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICI2jfl-gCVEqDUKQwAAE3yGRylUQQcwACqQ8AAmaMqVCQPTGFg7eIZTYE"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 7-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "18")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAICJWjfmBybTIIcGaJevMeZxrN9o87rAAJiAgACtAaxRDu0zQvmUR8wNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 8-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "19")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICN2jfmQyhmGg8kLvaY7s4nTdeq0DFAAKyGQAC9QGhUA_2YnUomY6jNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 1-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "20")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICOWjfmTk8MnxZ-MVf3pKkbXsJat17AALnGQAC9QGhUPIj54jrtNipNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 2-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "21")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICO2jfmWvj839-qmE7NZYYJRSzI9dqAAKrewAC-4egSKUecVSwGtRgNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 3-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "22")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICPWjfmZ83DnC9uO1I3rmhwxY1-SWNAALIewAC-4egSGPXPzY7_PBONgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 4-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "23")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICP2jfmdDOxuPZOJ-bQykIEPeXKQOuAAJlHAACJ1XAUf2_Uom-Cj5KNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 5-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "24")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICQWjfmgF2-N9cHw_auHYVSNT_DZAnAAKchgAChKnBSZ5IbXfph-arNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 6-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "25")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICQ2jfmi9VyJ_m1RajSobEHj3mPAkrAAKHggAChBnJSSZAiewXWh_XNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 7-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "26")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICRWjfmmuRYxBnyKS-HmpieYdsS6wIAAIGgwAChBnJSe-G2itus1-2NgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 8-qism ( final )
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)



# 📌 2️⃣ Xabar "2" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "28")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICbGjhBe1yE1MM_RgzkKNCe8rXGsfqAALuiwACR2oAAUuLnifVvxNqUDYE"
        await message.answer_video(file_id, caption="""⌨️ KOD: #28 
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


# 📌 2️⃣ Xabar "2" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "29")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICbmjhBlZWOEQ99VWC8FYzyNGjGayXAALbjgACR2oAAUtgut-rXkt7LDYE"
        await message.answer_video(file_id, caption="""⌨️ KOD: #29 
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


# 📌 2️⃣ Xabar "2" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "30")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICcGjhBn4xNa4MRlIPbCre1Pr1Kxa-AAJefwACR2oIS2-fzX8s0FE7NgQ"
        await message.answer_video(file_id, caption="""⌨️ KOD: #30
       bot; @UrtakKino_bot
       Qolgan qisimlari pasdagi kanalga joylanib boriladi 
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
# 📌 2️⃣ Xabar "2" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "32")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICf2jhIYKsQaZKLjKCAAFt8VEdhApUiwACrQ4AAvJmoVK0Q3DA8OBHlzYE"
        await message.answer_video(file_id, caption="""PREMYERA⚡️2023

🎥Nomi: So'nggi qirollik: 7 qirol o'lishi kerak
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 480P Mobile HD
🌏Davlat: AQSH
📆Yili: 2023-yil
🎞️Janri: #Jangari #Tarixiy #Drama
        ⌨️ KOD: #32
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "31")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAx0CbGPjfgACBHFo4SPP1niCp2s-S-EWv9NImplTfQACIBcAAqbwwFMjLX8Qp8idiDYE"
        await message.answer_video(file_id, caption="""⌨️ KOD: #31 
       bot; @UrtakKino_bot
        Qolgan qisimlari pasdagi kanalga joylanib boriladi 
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "33")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAICv2jh6JcAAeGPjr7tR8Q-VlcNifuyEwACUAMAAncLwUefwkp0RtNsjTYE"
        await message.answer_video(file_id, caption="""

🎥Nomi: 300 spartalik
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH
📆Yili: 2023-yil
🎞️Janri: #Jangari #Tarixiy #Drama
        ⌨️ KOD: #33
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "34")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAIC22jh_gaVxhqL2YNsbNfeTOITNpbuAAJOAwAC2pqBR-jUUT2dXqo4NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Himoyachilar
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Rossiya
📆Yili: 2023-yil
🎞️Janri: #Jangari #Tarixiy #Drama
        ⌨️ KOD: #34
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "35")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDAAFo4gABZHMkO0gNAsks5EEh8pisAAF-AAIcBwACs-WRUZ5q9SAKGQjeNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Yashil Fonus 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH
📆Yili:  2011-yil
🎞️Janri: #Jangari  #Drama #fantastik
        ⌨️ KOD: #35
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "36")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDBWjiAAFkfB0tAz14QnjZi0reUaLX8gACsBMAApA28FFFiTvKpS-LuDYE"
        await message.answer_video(file_id, caption="""

🎥Nomi: Oʻqchi | Snayper
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH
📆Yili:  2011-yil
🎞️Janri: #Jangari  #Drama #fantastik
        ⌨️ KOD: #36
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "37")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDBGjiAAFk-GnND2r88B-m7Qsl-8aR3wACDA8AAs_mmVBtIND7wIm1WTYE"
        await message.answer_video(file_id, caption="""

🎥Nomi: Tofon
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Hindiston 
📆Yili:  2011-yil
🎞️Janri: #Jangari  #Drama #fantastik 
        ⌨️ KOD: #37
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "38")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDAmjiAAFkwuEDK279Ls0eCKI9Mk7HhwAChwkAAnd7yFEi6oMthl7iAjYE"
        await message.answer_video(file_id, caption="""

🎥Nomi: Buyuk Devor 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH, Xitoy 
📆Yili:  2016-yil
🎞️Janri: #Jangari #Fantastik 
        ⌨️ KOD: #38
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "39")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIDAWjiAAFku8vZqAtcF3GwQ9rRViPvKQACLgkAAlW_KEigMx2HpOaveDYE"
        await message.answer_video(file_id, caption="""

🎥Nomi: T-34
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Rossiya
📆Yili:  2016-yil
🎞️Janri: #Jangari #Tank 
        ⌨️ KOD: #39
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "40")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIC_2jiAAFk6SRfr0jS6zXis-wo1mwt7AACMgoAAkQN0FCpyWmEbFwDpDYE"
        await message.answer_video(file_id, caption="""

🎥Nomi: Qahr
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Hindiston 
📆Yili:  2014-yil
🎞️Janri: #Jangari #urush #dramma
        ⌨️ KOD: #40
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "41")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgUAAxkBAAIDamjkceOABVTZxS6rQYnvQRnjIZW8AALTGQACuWHwVgWjjQyGOBoBNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Drakula
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH
📆Yili:  2025-yil
🎞️Janri: #Jangari #urush #dramma  #romantika #melodrama #fantastik 
        ⌨️ KOD: #41
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "42")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgUAAxkBAAIDsGjmHBFCQ_YZxbkVTk5Kl-MgumDrAAKxGQACdUPhVs7y0CZDBjNYNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Jingalak soch qiz | Chinakam muhabbat 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Janubiy Koreya filmi
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #42
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "43")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDsmjmHMvky_7_weugOtOt5v-h5CC-AAJ0GQACz7qpUejBqyKsZ94PNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Mening Oksford yilim
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #43
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "44")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDtGjmHTUFFk_bMcrFWTEvFq4AAY5E6AAC5RkAAg4_-VGfrBxjseyHtjYE"
        await message.answer_video(file_id, caption="""

🎥Nomi:  Qalbga yo'l
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: janubiy koreya
📆Yili:  2018-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #44
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "45")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDuGjmIlMX5RoIq-kIorF8B2bzhK3iAAKKGQACuosIUND-xyfo_-fYNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:   Yordamga  Arjun 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: hind filim
📆Yili:  2023-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #45
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "47")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIEFmjnJV-5Bb15JKPORLkojQkOAUg7AALFGwACTKyoUDgWkrgEEzzANgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:  Qaroqchi Ilya Muromistga qarshi
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Rossiya filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #47
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "46")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIDtmjmHfhIR-I5QjXd4HqD5rCBiQ44AAKdHQACG8d4UqVql0njBHM-NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:  on ikki koreys serial  
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:koreya serial
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #46
       bot; @UrtakKino_bot
qolgan qisimlari pasdagi kanalda
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "48")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIEkGjqeIZYnFB4Y2s-9LYsBsz6HzRWAAKXGgACEOnpUKFng5VGdMGaNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Yolg‘iz farzand 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:AQSH filim
📆Yili:  2004-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #48
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "49")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIEkmjqethGuQvGr9HD_Gudp1EPwUp6AAKyFAACsTCpUu_nulVrG63XNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Tug'ruqdan keyin
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:turkiya  filim
📆Yili:  2022-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #49
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "50")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIElGjqe0GJ-Qvk1t94VZ__MlAXwrJvAAICHgACDkGRUH1F9Z_ovk46NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Ajdar o'rgatuvchilar
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH  filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #50
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "51")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIEuGjrMax-hn1P3zsKR_XY5i5U-VYnAAJhGwACRT8YUDmG-XBXQpdWNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Qora jodu 4 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: hind filim
📆Yili:  2016-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #51
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "52")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIEumjrMlT7aPIB_lMpY1NW9XnL0fI6AAKLGQACRT8gUJssrTdpmG3-NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Taqiqlangan shahar
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Italiya filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #52
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "53")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIEvGjrMp23MwloL8HtFtJdolSZ4PjGAALYGgACQjwIU6sPr6WXA1U6NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Bir kun 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:AQSH filim
📆Yili:  2011-yil
🎞️Janri:  #romantika #komediya 
        ⌨️ KOD: #53
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "54")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIEvmjrMyYz-EqTp-sZMVySBMXfKvvJAAKNFQAC5JCZUkHvPLTlf9FJNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Mulla 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Qozogiston  filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya  
        ⌨️ KOD: #54
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "55")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIE9mjt3mYdxZDNFt9rv8BUWWmJr7kVAAI8GAACFrQJU5sU3wn3gS2BNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Yomon yigit va men
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:AQSH filim
📆Yili:  2024-yil
🎞️Janri:  #romantika #komediya  
        ⌨️ KOD: #55
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "56")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIE_Gjt4PtNONN8KA7dNdC6VroKV3pTAALsGAACEYKJUbDnoz1KGFdLNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Urma xotinjon
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: HINDISTONfilim
📆Yili:  2022-yil
🎞️Janri:  #romantika #komediya  
        ⌨️ KOD: #56
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "57")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIE_mjt4UbNZv3Gc7ZglvaJfxIjw-F6AAIKGgACu45wUstZlrrIMjwNNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Sevishganlar
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Fransiya filim
📆Yili:  2012-yil
🎞️Janri:  #romantika #komediya  
        ⌨️ KOD: #57
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "58")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFAAFo7eHoP2rJG3EGIBqskZ2CDul_zwACHhsAAriN0VJDklXpb8dL6TYE"
        await message.answer_video(file_id, caption="""

🎥Nomi:Harbiy  asir
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #58
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "59")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFGGjuNKWnNcOTAyHFVh-B71g4zQwCAAI9FgACSZ7hUVd8d8OqMUqcNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Kelinjon 2 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Qozoq filim
📆Yili:  2023-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #59
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "60")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgUAAxkBAAIFGmjuNLKjuqF-SJrBGWWVX2IHLuPvAAJbGwACBj2BVmxNAqWAdBIMNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Qizil Sonya 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: AQSH filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #60
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "61")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFHGjuNMHPOIdYUFfPLKcuzBP9jdB2AAKhFwACoB9JUySVWWlCeOwtNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Unitilgan sevgi 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: janubiy koreya filim
📆Yili:  2023-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #61
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "62")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFHmjuNOekuzts-T14sXuJkHavXB0yAALcGQACEYKBUcQDWz_3LsqkNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:100 yil oldin
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat: Rossiya  filim
📆Yili:  2024-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #62
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "63")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFIGjuNP8_LV2LAAGRIJIYDrPcDBS-XAACpRoAAuFKGFMnEjBtzyerWTYE"
        await message.answer_video(file_id, caption="""

🎥Nomi: Guntur Kaaram
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Hindiston filim
📆Yili:  2024-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #63 
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "64")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFhmjzNn2qxaQshL6ZzHXesu1ahHPbAAJSFgACKUi5UqbshiOcP-tPNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Bezori yigitlar : Qonunsizlar
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Janubiy koreya filim
📆Yili:  2019-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #64 
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "65")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFiGjzN5u4n0k7PubeM1nN-ilBCH02AAJcFgACeCPxUQUb_-ylWH8rNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Sig'indi Quda 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Qozogiston filim
📆Yili:  2020-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #65
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "66")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFimjzOFz5UD3CviJtMFv9X9RUcFlrAAKuEQACv1UYUk3Vo6lgRuX-NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Narkoz
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:AQSH filim
📆Yili:  2007-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #66
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "67")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgUAAxkBAAIFrGjzv_ZSTmoxNWClvlSG9D3aX6GvAAKoGQACNg9hVwMrj_ZSOZI8NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Kseno
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:AQSH filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #67
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "68")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgUAAxkBAAIFrmjz9D145NRIH_rC7grdR9R82IlAAAIFHQACWvc5V0hoUW1bblcHNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Parijdagi akula 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:AQSH filim
📆Yili:  2024-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #68
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "69")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFsGjz9OrRhIyB0KXCraH-o77OW70aAAJmGQACRiNRUseL0o2eF6CONgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Orzular ro'yxati 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:AQSH filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #69
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "70")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFsmjz9ZjM2wNb0En2k3Aq0KEWxZthAAJAFgACjDHBU1_ovddrB171NgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:Ogirlangan kuyovlar 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Hind  filim
📆Yili:  2019-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #70
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "71")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFtGjz9gLjErY_tCAcPZAo7TEOnxEbAAIqGAACFK2BUoKxtgP7LD7tNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Sohibjamol va Mahluq
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Fransiya filim
📆Yili:  2014-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #71
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "72")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFtmjz9j_ClFpR1wchgDGzcBkh0ELHAAKkFwAC3s1wUhDlrmlYivRxNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi: Eflatun
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Turkiya filim
📆Yili:  2022-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #72
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "73")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIFuGjz9mo3bKEzC2nmpGn6hwNM-Jw1AAJyFwAC3s1wUmjcm3VLmZ-tNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:  Ikkinchi xotin 
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Hind filim
📆Yili:  2022-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #73
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "74")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIGDGklMYqFF-qZB3d364o_ntrEk-IQAAJQGQACHtsJUdil0pvUEk6UNgQ"
        await message.answer_video(file_id, caption="""

🎥Nomi:  Aqldan ozdirasan
➖➖➖➖➖➖➖➖➖➖
🌍Tili: Oʻzbek Tilida 
📀Sifati: 1080P Mobile HD
🌏Davlat:Rossiya filim
📆Yili:  2025-yil
🎞️Janri:  #romantika #komediya #jangari
        ⌨️ KOD: #74
       bot; @UrtakKino_bot

        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "75")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIGgGmBm3-kOGRhNwjICSwTnpVtVcmJAAL3EQACrXxAUqJs2anM5KF4OAQ"
        await message.answer_video(file_id, caption="""
🎬 Nomi: Eh, Belinda

💽Sifati: 720p HD
🌎Davlati: Turkiya 
🎭Janir: #Komediya #Drama #Melodrama
        ⌨️ KOD: #75
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "76")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIHHWmB9GlPu_BbCcPib6lum1hUG49YAAIxHAACiax4Ug5FKHeViT2fOAQ"
        await message.answer_video(file_id, caption="""
🗂 Yuklash: 6510
        ⌨️ KOD: #76
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "77")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIHG2mB9ETRYM31BYAd55j4TStdQ4DWAAJ1IQACAtNYUZCo2roDD3XrOAQ"
        await message.answer_video(file_id, caption="""
🗂 Yuklash: 6510
        ⌨️ KOD: #77
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "78")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIHH2mB9Yqj9qdoxLgSlLd6rvQydpoRAALZGgACcq5AUB8RNEAmcSmIOAQ"
        await message.answer_video(file_id, caption="""
🗂 Yuklash: 6510
        ⌨️ KOD: #78
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
   @dp.message(F.text == "79")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIH0mmC9yg0oEa5B3EHiuVghqJhF8cSAAJLHQAC6GX4U5GsboZnRuEyOAQ"
        await message.answer_video(file_id, caption="""
🗂 Yuklash: 6510
        ⌨️ KOD: #79
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
     @dp.message(F.text == "80")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIH1GmC910tipm8fu59WStnZ1Ok0M2AAAJ1HAACtLtxU4hcKzZqfMGyOAQ"
        await message.answer_video(file_id, caption="""
🗂 Yuklash: 6510
        ⌨️ KOD: #80
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)




async def main():
    print('bot ishladi....')
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())

