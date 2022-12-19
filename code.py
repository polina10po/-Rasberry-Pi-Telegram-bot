import time
import datetime
import telepot
from telepot.loop import MessageLoop
from picamera import PiCamera

now = datetime.datetime.now()
camera = PiCamera()

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
        camera.start_preview()
        camera.capture('/home/orangepi/img.jpg', resize(640, 480))
        camera.stop_preview()
        camera.close()
        bot.sendPhoto(chat_id, open('/home/orangepi/img.jpg'))

bot = telepot.Bot('5790505945:AAGf0gTk8LD3k4IXhdQog5YQezat2YyTFZQ')
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
