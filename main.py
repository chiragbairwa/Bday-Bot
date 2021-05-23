from telegram.ext import Updater, CommandHandler, MessageHandler
import json
import datetime

token = ''

with open('API.json',"r") as file:
    data = json.load(file)
    token = data['API']

def start_command(update, context):
    update.message.reply_text('Hello')

""" Command Handlers """
def write_on_db(data):
    pass
def bday_add(update, context):
    update.message.reply_text('Enter Name:')
    name = str(update.message.text)

    # telegram.inline.inputmessagecontent.InputMessageContent
    telegram.ReplyKeyboardMarkup
    update.message.reply_text('Enter Day:')
    day = str( update.message.text )
    
    update.message.reply_text('Enter Month:')
    month = str(update.message.text)
    data = {"name": name, "date": [day,month]}

    # with open("db.json") as file:
    #     data = json.load(file)
    print(data)

def bday_list(update, context):
    with open('db.json') as json_data:
        data = json.load(json_data)["data"]
    update.message.reply_text(data)

def bday_wish():
    update.message.reply_text('hbday')

def check(update, context):
    print("called..")
    with open('db.json', 'r') as json_data:
        data = json.load(json_data)["data"]
        print(data)
    
    # Desired value fetch
    for i in data:
        if (20 in i["date"]) and ("may" in i["date"]):
            print(i["name"])

""" main """
def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("add_bday", bday_add))
    dp.add_handler(CommandHandler("show_list", bday_list))
    dp.add_handler(CommandHandler("check", check))


    # if datetime.datetime.now().minute == 22:
    #     update.message.reply_text('Happy Bday')
    """IF TIME IS 12:00 THEN CALL WISH """
    updater.start_polling()
    updater.idle()
    
main()

# datetime.datetime.now().day()