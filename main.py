from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import re
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv("TOKEN_BOT"))
dp = Dispatcher()




#Para nuevos usuarios de la app
#Kit de cupones de 100€
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



@dp.message(Command("start"))
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🆕 compro antes por temu")],
            [KeyboardButton(text="🎁 nunca compro por temu")],
                  
        ],
        resize_keyboard=True
        )
    await message.reply(
        
        "hola, a tu bot de rabajas de temu\n\nha comprado antes por temu?",
        reply_markup=keyboard
        
    )
    
    
@dp.message(lambda message: message.text in["🆕 compro antes por temu","🎁 nunca compro por temu"])    
async def hand_btn(message: Message):
    if message.text == "🆕 compro antes por temu":
        await message.reply(
            f"🎉 ¡Aquí tienes tu cupón para clientes existentes!\n\n"
            f"🔗 {link_todousr}"
        )
    
    elif message.text == "🎁 nunca compro por temu":
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
            f"🔗 cupón generar 1: {link_generar1}\n\n"
            f"🔗 cupón generar 2: {link_profund}\n\n"
            f"🎟️ Código generar : {codigo_cupon3}"
            
        )

    
async def runing():
    print("✅ Bot iniciado...")
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(runing())

