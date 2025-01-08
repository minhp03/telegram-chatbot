import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder,ContextTypes, CommandHandler



BOT_TOKEN = "YOUR TOKEN HERE"
API_TOKEN = "API TOKEN HERE"
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


application = ApplicationBuilder().token(BOT_TOKEN).build()


application.run_polling()