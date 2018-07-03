import telebot
import pyowm

bot = telebot.TeleBot() # token here
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
    return

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()

    bot.send_message(message.from_user.id, 'Thanks for using my bot!',
                     reply_markup=hide_markup)

def get_weather(city_name):
   obs = owm.weather_at_place(city_name)    # obs for observation TODO: create better names



bot.polling(none_stop=True, interval=0)