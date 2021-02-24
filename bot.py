#!/usr/bin/env python
import os
import telebot 
import logging
from telebot import types
from replies import *
from decouple import config



TOKEN = config("TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML") # You can set parse_mode by default. HTML or MARKDOWN

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



@bot.message_handler(commands=['start'])
def send_welcome(m):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row(question1,question2 )
    user_markup.row(question3)
    user_markup.row(question4)
    user_markup.row(question5)
    user_markup.row(question6)
    user_markup.row(question7)
    user_markup.row(question8)
    user_markup.row(question9)
    user_markup.row(question10)
    user_markup.row(question11)
    user_markup.row(question12)
    cid = m.chat.id
    line1 = 'Hello, I\'m Adigun 🤖! Press any button below to interact with me. You will love using me to get Blockchain information.'
    msg = line1
    bot.send_message(cid, msg, reply_markup=user_markup)


# main menu
@bot.message_handler(commands=['menu'])
@bot.message_handler(regexp="menu")
def main_menu(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(question1, question2)
    user_markup.row(question3, question4)
    user_markup.row(question5, question6)
    user_markup.row(question7, question8)
    user_markup.row(question9, question10)
    user_markup.row(question11, question12)
    cid = m.chat.id
    user_msg = 'Welcome to the main menu.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)


# help details
@bot.message_handler(regexp="Help")
def command_help(m):
    cid = m.chat.id
    help_text = "Alexandra 🤖: Send my creator *@Josylad* a private message if you need help with anything."
    bot.send_message(cid, help_text, parse_mode='Markdown')


@bot.message_handler(regexp='^What is Blockchain$')
def send_answer(m):
    user_msg = answer1
    bot.reply_to(m, user_msg)

#fixing this regex part was serious work, but it works now!
@bot.message_handler(regexp='^What is blockchain software$')
def send_answer(m):
    user_msg = answer2
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What Is A Private Blockchain$')
def send_answer(m):
    user_msg = answer3
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What Is A Smart Contract$')
def send_answer(m):
    user_msg = answer4
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What is Mining$')
def send_answer(m):
    user_msg = answer5
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^How does a blockchain work$')
def send_answer(m):
    user_msg = answer6
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What is a blockchain application$')
def send_answer(m):
    user_msg = answer7
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What are the benefits of blockchain technology$')
def send_answer(m):
    user_msg = answer8
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What is the blockchain revolution$')
def send_answer(m):
    user_msg = answer9
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What is decentralized finance$')
def send_answer(m):
    user_msg = answer10
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What is a block in a blockchain$')
def send_answer(m):
    user_msg = answer11
    bot.reply_to(m, user_msg)

@bot.message_handler(regexp='^What is a blockchain wallet$')
def send_answer(m):
    user_msg = answer12
    bot.reply_to(m, user_msg)

# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# - interval: True/False (default False) - The interval between polling requests
#           Note: Editing this parameter harms the bot's response time
# - timeout: integer (default 20) - Timeout in seconds for long polling.

bot.polling()