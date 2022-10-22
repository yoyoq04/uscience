import sys
import time
import random
import datetime
import telepot

def handle(msg):
	chat_id = msg["chat"]["id"]
	command = msg["text"]

	#print "Got command: %s" % command 

	if command == "command1":
		bot.sendMessage(chat_id="515182637", text="Hola")
	elif command == "command2":
		bot.sendMessage(chat_id="515182637", text="Waku waku")
	elif command == "sus":
		bot.sendPhoto(chat_id="515182637", photo=("https://i1.sndcdn.com/artworks-VKm5SJSMycnmXUyK-oyxM4Q-t240x240.jpg"))
	elif command == "amongus":
		bot.sendPhoto(chat_id="515182637", photo=("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3hhjBDWF3jAaLhGxaX8azJp83GuRFXs8eiQ&usqp=CAU"))
	elif command == "photo":
		bot.sendPhoto(chat_id="515182637", photo=("https://akcdn.detik.net.id/visual/2022/06/30/anime-spy-x-family-anya-forger_169.jpeg?w=650"))

bot = telepot.Bot("5695185577:AAHXQyWyDCZOsEa32ZKkLInArFSjhx65LaM")
bot.message_loop(handle)

while 1:
	time.sleep(10)