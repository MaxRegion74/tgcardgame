import telebot
import random
import time
token = "1746511679:AAHLWHfLgnBiP7O6ZX0UAqQ73Lo2SPDU9nA"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "This is a SOLO BlackJack game. The goal of blackjack is score 21 points.")
    bot.send_message(message.chat.id,"Would you like to start? Press 'y' to start the game")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    random.shuffle(koloda)
    count = 0
    if message.text.lower() == "y":
        while True:
            current = koloda.pop()
            bot.send_message(message.chat.id, f"You have hitted {current} points")
            time.sleep(0.8)
            count += current
            if count > 21:
                bot.send_message(message.chat.id, f"I AM SORRY YOU HAVE LOST THIS GAME WITH A {count} POINTS")
                time.sleep(1)
                bot.send_message(message.chat.id, "Press 'Y' to start again")
                break
            elif count == 21:
                bot.send_message(message.chat.id, f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!! CONGRATS! YOU HAVE WON THIS GAME WITH A {count} POINTS !!!!!!!!!!!!!!!")
                time.sleep(1)
                bot.send_message(message.chat.id, "Press 'Y' to start again")
                break
            else:
                bot.send_message(message.chat.id, f"Now you have got in general {count} points")
                time.sleep(0.8)
    elif message.text.lower() == "n":
        bot.send_message(message.chat.id,f"You have got {count} points and you have ended this game.")
bot.polling(none_stop=True)