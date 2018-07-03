import telebot
import pyowm

from pyowm import exceptions as pyex

bot = telebot.TeleBot('') # token here
owm = pyowm.OWM('a3b32fc0e56e8a8b54b4949c18b4b27c')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row('/start', '/stop')
    user_markup.row('/weather')

    bot.send_message(message.from_user.id, 'Greetings user...',
                     reply_markup=user_markup)

@bot.message_handler(commands=['weather'])
def handle_weather(message):
    bot.send_message(message.from_user.id,  'Enter your city in the form (City - London,uk)')
    pyex.not_found_error.NotFoundError(print('Such wasnt found'))

@bot.message_handler(content_types=['text'])
def handle_messages(message):
    try:
        weather_array = message.text.split(',')

        if weather_array[0][:4] == 'City':
            bot.send_message(message.from_user.id, get_weather(message.text[7:]))
    except Exception as e:
        try:
            e.__str__(bot.send_message(message.from_user.id, 'There is no city with this name'))
        except TypeError as e:
            e.__str__
        else:
            bot.send_message(message.from_user.id, 'Bot is not ready yet')

    log(message)



@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()

    bot.send_message(message.from_user.id, 'Thanks for using my bot!',
                     reply_markup=hide_markup)

def get_weather(city_name):
   observation = owm.weather_at_place(city_name)
   w = observation.get_weather()

   weather_array = str(w).split(', ')
   return weather_array[1][7:-1]

def log(message):
    from datetime import datetime

    print(datetime.now(), "\n")
    print("Message from {0} {1}. (id = {2})\n\n".format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        message.from_user.id))

    print('Text of the message: {0}'.format(message.text))
    print('Location of the user: {0}'.format(message.location))

bot.polling(none_stop=True, interval=0)