# if __name__ == "__main__":
#   app.run()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import date
import datetime, pytz
import time


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello " + update.effective_user.first_name)

def getDate(update: Update, context: CallbackContext) -> None:
    today = date.today()
    update.message.reply_text("Today is " + today.strftime("%m-%d-%Y"))

def repeat(update: Update, context: CallbackContext) -> None:
    text = str(update.message.text)
    update.message.reply_text("Text is " + text)

def callback_auto_message(context):
    context.bot.send_message(chat_id = '1415800793', text='Automatic message!')

def start_auto_messaging(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(callback_auto_message, 2, context = chat_id, name = str(chat_id))
    # context.job_queue.run_once(callback_auto_message, 3600, context=chat_id)
    # context.job_queue.run_daily(callback_auto_message, time=datetime.time(hour=9, minute=22), days=(0, 1, 2, 3, 4, 5, 6), context=chat_id)

def stop_notify(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id = chat_id, text='Stopping automatic messages!')
    job = context.job_queue.get_jobs_by_name(str(chat_id))
    job[0].schedule_removal()

def saveText(update: Update, context: CallbackContext):
    file = open("data.txt", "w")
    file.write(str(update.message.text).split()[1])
    file.close()

def notify(context: CallbackContext):
    context.bot.send_message(chat_id = '1415800793', text = 'Daily notification!')

def turnOn(update: Update, context: CallbackContext):
    context.job_queue.run_daily(notify, 
        datetime.time(hour = 13, minute = 11, second = 40, tzinfo = pytz.timezone('Asia/Ho_Chi_Minh')), 
        context = update.message.chat_id)

def stop(update: Update, context: CallbackContext):
    global updater
    updater.stop()

LiHeng_TOKEN = "5259465400:AAH-10RgdWJTF1FKxzdUpm-ZD6yQUWCYeYg"
DevBot_TOKEN = "5782089032:AAFreSMLXRSlIFJLOa6WQB9jss7xAw0vng4"

updater = Updater(LiHeng_TOKEN)
updater.dispatcher.add_handler(CommandHandler("auto", start_auto_messaging))
updater.dispatcher.add_handler(CommandHandler("stop", stop_notify))
updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("date", getDate))
updater.dispatcher.add_handler(CommandHandler("repeat", repeat))
updater.dispatcher.add_handler(CommandHandler("save", saveText))
updater.dispatcher.add_handler(CommandHandler("turnOn", turnOn, pass_job_queue = True))
updater.job_queue.run_daily(notify,
    datetime.time(hour = 13, minute = 11, second = 40, tzinfo = pytz.timezone('Asia/Ho_Chi_Minh')), 

)
updater.start_polling()
updater.idle()