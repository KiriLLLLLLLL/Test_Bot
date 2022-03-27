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
def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def game_command(update: Update, context: CallbackContext):
    item = [
        [
            InlineKeyboardButton("камень", callback_data='rock'),
            InlineKeyboardButton("бумага", callback_data='paper'),
            InlineKeyboardButton("ножницы", callback_data='scissors')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(item)
    update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    player = update.callback_query
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    if player.data == computer:
        player.edit_message_text(f"You: {player.data}, Bot: {computer}  Tie!")
    if player.data == "scissors":
        if computer == "rock":
            player.edit_message_text(f"You: {player.data}, Bot: {computer}  You loose!")
        if computer == "paper":
            player.edit_message_text(f"You: {player.data}, Bot: {computer}  You win!")
    if player.data == "paper":
        if computer == "scissors":
            player.edit_message_text(f"You: {player.data}, Bot: {computer}  You loose!")
        if computer == "rock":
            player.edit_message_text(f"You: {player.data}, Bot: {computer}  You win!")
    if player.data == "rock":
        if computer == "paper":
            player.edit_message_text(f"You: {player.data}, Bot: {computer}  You loose!")
        if computer == "scissors":
            player.edit_message_text(f"You: {player.data}, Bot: {computer}  You win!")



