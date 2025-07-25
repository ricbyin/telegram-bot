import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7581801542:AAHK5se8HwkPhOkkdjAxiOVxLRnJEO0H_pw"
CHAT_ID = 7808787087

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot aktif di Render!")

async def kirim_pesan_awal(app):
    await app.bot.send_message(chat_id=CHAT_ID, text="🤖 Bot dari Render aktif!")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await kirim_pesan_awal(app)
    await app.run_polling()

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
