# if __name__ == "__main__":
#   app.run()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import date
import time


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello " + update.effective_user.first_name)

def getDate(update: Update, context: CallbackContext) -> None:
    today = date.today()
    update.message.reply_text("Today is " + today.strftime("%m-%d-%Y"))

def repeat(update: Update, context: CallbackContext) -> None:
    text = str(update.message.text)
    update.message.reply_text("Text is " + text)

updater = Updater("5259465400:AAH-10RgdWJTF1FKxzdUpm-ZD6yQUWCYeYg")
updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("date", getDate))
updater.dispatcher.add_handler(CommandHandler("repeat", repeat))
updater.start_polling()
updater.idle()