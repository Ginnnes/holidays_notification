import telebot
import time
bot = telebot.TeleBot('5651115064:AAEybYXX_mIHx9GcCRWgVAOrbH8j_GQ42G8')
CHANNEL_NAME = '@hihihirus'
f = open('c:/Users/alex/Documents/data/prz.txt', 'r', encoding='UTF-8')
przs = f.read().split("*")
f.close()
for prz in przs:
    bot.send_message(CHANNEL_NAME, prz)
    time.sleep(3)