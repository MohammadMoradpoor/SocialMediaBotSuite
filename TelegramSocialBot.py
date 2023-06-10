import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update

updater = Updater("5343061465:AAFOJ74PiOmYRl5SVG_JhEoDZ-cG0sN1bwg",
                  use_context=True)
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write /help to see the commands available.")
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /github - To get the github profile URL""")
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("Gmail URL =>\
    mohammadsalehmoradpoor@gmail.com/")
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/")
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => \
        https://www.linkedin.com/in/mohamad-moradpoor/")
def github_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "github id => https://github.com/MohamadsalehMoradpoor/")
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

# https://www.geeksforgeeks.org/create-a-telegram-bot-using-python/
# https://codeyad.com/Mag/Post/build-a-telegram-robot


# from requests import get
# token = "TOKEN"
# chat_id = "-732147790"
# text = "whats your name"
# url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token, chat_id, text)
# print(get(url))