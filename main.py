from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os
from dotenv import load_dotenv
from aiohttp import web

# تحميل المتغيرات البيئية
load_dotenv()

# المتغيرات
TOKEN_BOT = os.getenv("TOKEN_BOT")
afilit_nuser1 = os.getenv("AFILITE_NUSER1")
afilit_nuser2 = os.getenv("AFILIT_NUSER2")
codigo_cupon1 = os.getenv("CODIGO_CUPON1")

# 0€ por Regalos
regalo1 = os.getenv("REGALO1")
regalo2 = os.getenv("REGALO2")
codigo_cupon2 = os.getenv("CODIGO_CUPON2")

#Generar enlace
link_generar1 = os.getenv("LINK_GENERAR1")
link_profund = os.getenv("LINK_PROFUND")
codigo_cupon3 = os.getenv("CODIGO_CUPON3")


#Todos los usuarios
link_todousr = os.getenv("LINK_TODOUSR")

# التحقق من التوكن
if not TOKEN_BOT:
    raise ValueError("❌ BOT_TOKEN غير موجود!")

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher()

# ============ WEB SERVER (Koyeb) ============
async def health_check(request):
    """Health check endpoint"""
    bot_info = await bot.get_me()
    return web.Response(text=f"✅ Bot @{bot_info.username} is running!")

async def root_handler(request):
    """Root endpoint"""
    return web.Response(text="🤖 Temu Bot is active!")

async def start_web_server():
    """تشغيل HTTP server"""
    app = web.Application()
    app.router.add_get('/', root_handler)
    app.router.add_get('/health', health_check)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Koyeb يستخدم PORT environment variable
    port = int(os.getenv('PORT', 8000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 Web server running on port {port}")
    return site
# ================================================

@dp.message(Command("start"))
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🆕 Compré antes por Temu")],
            [KeyboardButton(text="🎁 Nunca compré por Temu")],
        ],
        resize_keyboard=True
    )
    await message.reply(
        "¡Hola! Bienvenido a tu bot de rebajas de Temu 🛍️\n\n"
        "¿Has comprado antes por Temu?",
        reply_markup=keyboard
    )

@dp.message(lambda msg: msg.text in ["🆕 Compré antes por Temu", "🎁 Nunca compré por Temu"])
async def handle_buttons(message: Message):
    if message.text == "🆕 Compré antes por Temu":
        await message.reply(
            f"🎉 ¡Aquí tienes tu cupón para clientes existentes!\n\n"
            f"🔗 {link_todousr}"
        )
    
    elif message.text == "🎁 Nunca compré por Temu":
        await message.reply(
            f"🎁 ¡Aquí tienes cupones para nuevos usuarios!\n\n"
            f"💰 Kit de cupones 100€:\n"
            f"🔗 Opción 1: {afilit_nuser1}\n"
            f"🔗 Opción 2: {afilit_nuser2}\n\n"
            f"🎟️ Código de cupón: `{codigo_cupon1}`\n\n"
            f"📦 Regalos gratis:\n"
            f"🔗 Regalo 1: {regalo1}\n"
            f"🔗 Regalo 2: {regalo2}\n"
            f"🎟️ Código: `{codigo_cupon2}`"
            f"💰 Generar enlace para nuevos usuarios de temu\n"
            f"🔗 cupón generar 1: {link_generar1}\n"
            f"🔗 cupón generar 2: {link_profund}\n"
            f"🎟️ Código generar: {codigo_cupon3}"
            
        )
async def main():
    print("=" * 50)
    print("🚀 Starting Temu Bot...")
    print("=" * 50)
    
    # معلومات البوت
    bot_info = await bot.get_me()
    print(f"✅ Bot: @{bot_info.username}")
    print(f"🆔 ID: {bot_info.id}")
    
    # تشغيل web server في background
    site = await start_web_server()
    print("✅ Web server started")
    
    # تشغيل البوت
    print("✅ Starting bot polling...")
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await site.stop()
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⛔ Bot stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
