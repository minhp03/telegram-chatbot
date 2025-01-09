import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder,ContextTypes, CommandHandler


import os
from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import filters,ApplicationBuilder,ContextTypes, CommandHandler, MessageHandler


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)
chat_history = []


#function to appear the message
async def chat(update:Update, context: ContextTypes.DEFAULT_TYPE):
    global chat_history    
    messages =  []
    #let the bot know the previous conversation
    for user_message , bot_message in chat_history:
        messages.append({"role":"user","content":user_message})
        messages.append({"role":"assistant","content":bot_message})

    #update new message from user
    user_message = update.message.text
    messages.append({"role":"user","content":user_message})
    #bot response
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o-mini",
        #stream=True
    )

application.run_polling()
