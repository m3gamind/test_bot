import logging
import telegram
from telegram.ext import Filters
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

def start(bot, update):
	update.message.reply_text("Hi, Bugs are bugging you? Fret not, I'm here to help!")

	user = telegram.User(id=562767140, first_name="", is_bot=False)
	user.send_message("Hey There!")


def MsgHandle(bot, update):
	print("User :", update.message.text)

	reply = "Maybe I'm running on a docker container inside an Operating System on a virtual machine inside Microsoft Azure Cloud inside another Virtual Environment on top a of a Hypervisor on some Operating System on a server infrastructure located somewhere around the world! Maybe... Just Maybe..."

	print("BugBugger:", reply)
	update.message.reply_text(reply)


def getkey():
	f = open("telegram-key.txt", "r")
	key = str(f.readline()).strip()
	f.close()
	print(key)
	return key

def main():
	# Create Updater object and attach dispatcher to it
	key = getkey()
	updater = Updater(key)
	dispatcher = updater.dispatcher
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)
	print("Bot started")

	# Add command handler to dispatcher 
	dispatcher.add_handler(CommandHandler('start',start))

	# on noncommand i.e message - echo the message on Telegram
	dispatcher.add_handler(MessageHandler(Filters.text, MsgHandle))

	# Start the bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C
	updater.idle()


if __name__ == '__main__':
	main()