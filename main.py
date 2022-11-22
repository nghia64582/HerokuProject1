from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import date


def hello(update: Update, context: CallbackContext) -> None:
	update.message.reply_text("Hello " + update.effective_user.first_name)

def getDate(update: Update, context: CallbackContext) -> None:
	today = date.today()
	update.message.reply_text("Today is " + today.strftime("%m-%d-%Y"))

updater = Updater("5259465400:AAH-10RgdWJTF1FKxzdUpm-ZD6yQUWCYeYg")
updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("date", getDate))
updater.start_polling()
updater.idle()