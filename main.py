from telegram.ext import Updater, CommandHandler, MessageHandler
import json

token = ''

with open('API.json',"r") as file:
    data = json.load(file)

def start_command(update, context):
    update.message.reply_text('Hello')

""" Command Handlers """
def bday_add():
    pass

def bday_list():
    pass

def bday_wish():
    pass

""" main """
def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("add_bday", bday_add))
    dp.add_handler(CommandHandler("show_list", bday_list))

    """IF TIME IS 12:00 THEN CALL WISH """
    updater.start_polling()
    updater.idle()
    
main()
