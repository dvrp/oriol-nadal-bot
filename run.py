# -*- coding: UTF-8 -*-
from telegram.ext import Updater
API_KEY = '481044208:AAGT44fpd-FJ1pSDIYZEp26egqW9D8OHPjA'
updater = Updater(token=API_KEY)
dispatcher = updater.dispatcher

# Logging

import logging
logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Start Command
def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Hola, sóc l'Oriol Nadal, i no sóc un bot. #PNEB")

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, BaseFilter
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

### Nazi Filter
class NaziFilter(BaseFilter):
	def filter(self, message):
		return ('Heil' in message.text or 'heil' in message.text)
# Init
nazi_filter = NaziFilter()

def heil(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Hitler!')

heil_handler = MessageHandler(nazi_filter, heil)
dispatcher.add_handler(heil_handler)

### Patricia Filter
class PatriciaFilter(BaseFilter):
	def filter(self, message):
		return ('Patri' in message.text or 'patri' in message.text or 'patricia' in message.text or 'Patri' in message.text)
# Init
patricia_filter = PatriciaFilter()

def patricia_func(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='La profe que no està bona dius?')

patricia_handler = MessageHandler(patricia_filter, patricia_func)
dispatcher.add_handler(patricia_handler)
### Run bot

updater.start_polling()
updater.idle()