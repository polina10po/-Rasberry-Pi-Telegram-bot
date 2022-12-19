import time
import datetime
import telepot
from telepot.loop import MessageLoop
import cv2

now = datetime.datetime.now()
cap = cv2.VideoCapture(0)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == '/hi':
        bot.sendMessage(chat_id, "HI")
    elif command == '/date':
        bot.sendMessage(chat_id, "Date:" + str(now.day) + "." + str(now.month) + "." + str(now.year))
    elif command == '/time':
        bot.sendMessage(chat_id, "Time:" + str(now.hour) + ":" + str(now.minute))
    elif command == '/file':
        bot.sendDocument(chat_id, document = open('/home/orangepi/bot.py'))
    elif command == '/image':
        ret, frame = cap.read()
        cv2.imwrite("photo.jpg", frame)
        bot.sendPhoto(chat_id, open('/home/orangepi/photo.jpg'))

bot = telepot.Bot('5790505945:AAGf0gTk8LD3k4IXhdQog5YQezat2YyTFZQ')
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)



