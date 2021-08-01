import telebot # importamos la libreria de telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['info','hola']) #definimos el comando
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "Envia 1 o Celsius par ver Formula Grados Celsius a Grados Farenheit \n Envia 2 o Farenheit para ver Formula Grados Farenheit a Grados Celsius.")
    print("Mandaron 1")

@bot.message_handler(commands=['1','Celsius']) 
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "(0 °C × 9/5) + 32 = 32 °F")
    print("Mandaron 1")

@bot.message_handler(commands=['2','Farenheit'])
def nombre(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "(32 °F − 32) × 5/9 = 0 °C")
    print("Mandaron 2")

bot.polling()