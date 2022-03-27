import datetime, random, requests
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext
from pprint import pprint
from for_bot_tokens import weather_bot_token

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi - приветствие\n/time - узнать время\n/help - список команд\n/wtr - узнать погоду')

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

def button_game(update: Update, context: CallbackContext):
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

def weather_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'В каком городе Вы хотите узнать погоду?\nВведите название города на английском')

def get_weather(update: Update, context: CallbackContext):
    iqons = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={update.message.text}&appid={weather_bot_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]

        if weather_description in iqons:
            wd = iqons[weather_description]
        else:
            wd = "Не апокалипсис конечно, но лучше сам посмотри!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%d-%m-%Y %H:%M')
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%d-%m-%Y %H:%M')
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        update.message.reply_text(f"***{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}***\n"
              f"В {city} сегодня\nТемпература: {cur_weather}C° {wd}\nВлажность: {humidity}%\n"
              f"Давление: {pressure} мм.рт.ст\nВетер: {wind} м.с\n"
              f"Восход: {sunrise}\nЗакат: {sunset}\n"
              f"Световой день: {length_of_day}\n"
              f"Cпасибо, что воспользовались ботом!!!\n*** Хорошего дня!!! ***"
              )

    except:
        update.message.reply_text("\U00002620 Введите название города на английском! \U00002620")

