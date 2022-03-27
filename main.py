
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from bot_commands import *
from for_bot_tokens import *



updater = Updater(bot_token)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('game', game_command))
updater.dispatcher.add_handler(CallbackQueryHandler(button_game))
updater.dispatcher.add_handler(CommandHandler('wtr', weather_command))
updater.dispatcher.add_handler(MessageHandler(Filters.all, get_weather))

print('server start')
updater.start_polling()
updater.idle()

# import telebot
#
# bot = telebot.TeleBot(' 5137278585:AAEpmuFntgTDQXAkY6NMZXwDEchrMqMMJJ8')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_game(chat_id=message.chat.id, game_short_name='tictactoe')
#
# @bot.callback_query_handler(func=lambda callback_guery: callback_guery.game_short_name == 'tictactoe')
# def game(call):
#     bot.answer_callback_query(callback_query_id=call.id, url='https://multoigri.ru/game/igra-krestiki-noliki-na-beskonechnom-pole')
# if __name__ == "__main__":
#     bot.polling()