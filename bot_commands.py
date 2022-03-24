import datetime, random
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext


def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help')

def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')


def candle_command(update: Update, context: CallbackContext):

    msg = update.message.text
    items = msg.split()
    candy = 21
    candy_stap = 3
    update.message.reply_text(f'На столе --- {candy} конфета')
    while candy > 1:

        update.message.reply_text(f'Возьмите от 1 до {candy_stap} конфет... ')
        if candy > 0:
            player_1 = int(items[1])
            candy -= player_1
        update.message.reply_text(f'На столе --- {candy}')
        if candy == 0:
            update.message.reply_text('Победил 1 игрок')
            break
        if candy == 1:
            update.message.reply_text('Победил 2 игрок')
            break

        player_2 = random.randint(1, 3)
        candy -= player_2
        update.message.reply_text(f'На столе --- {candy}')
        msg = update.message.text
        items = msg.split()

        if candy == 0:
            update.message.reply_text('Победил 2 игрок')
        if candy == 1:
            update.message.reply_text('Победил 1 игрок')


def on_message(update: Update, context: CallbackContext):
    a = update.message.text
    return a


def game_command(update: Update, context: CallbackContext):
    item = [InlineKeyboardButton('камень', callback_data='rock'),
            InlineKeyboardButton('бумага', callback_data='paper'),
            InlineKeyboardButton('ножницы', callback_data='scissors')
    ]

    while True:
        choices = ["rock", "paper", "scissors"]

        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = msg.lower()

        if player == computer:

            update.message.reply_text("Tie!")
        if player == "scissors":
            if computer == "rock":

                update.message.reply_text("You loose!")
            if computer == "paper":

                update.message.reply_text("You win!")
        if player == "paper":
            if computer == "scissors":

                update.message.reply_text("You loose!")
            if computer == "rock":

                update.message.reply_text("You win!")
        if player == "rock":
            if computer == "paper":

                update.message.reply_text("You loose!")
            if computer == "scissors":

                update.message.reply_text("You win!")

        play_again = on_message(update, context).lower()
        if play_again == 'выйти':
            break
