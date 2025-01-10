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
    #update chat history
    bot_message = chat_completion.choices[0].message.content
    chat_history.append([user_message,bot_message])

    #update bot message
    # each bot have a different chat_id, so we update effective_chat id to send message 
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=bot_message)
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Hàm này sẽ được gọi khi bạn gửi lệnh /start
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Mình là bot, bạn có câu hỏi gì không!")



#
application = ApplicationBuilder().token(BOT_TOKEN).build()

start_handler = CommandHandler("start", start)
application.add_handler(start_handler)

chat_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chat)
application.add_handler(chat_handler)

print("Bot is running")
application.run_polling()
