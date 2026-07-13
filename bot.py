from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8437700020:AAFmCBvTZGNeTUIIhSzrLJNHITkldxkxpPU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot successfully chal raha hai. 🤖")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()

