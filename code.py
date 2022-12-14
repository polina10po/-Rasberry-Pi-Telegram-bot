import time
import datetime
import telepot
from telepot.loop import MessageLoop
from picamera import PiCamera

now = datetime.datetime.now()

def handle(msg):
  chat_id = msg['chat']['id']
  command = msg['text']
  
  print('Received:')
  print(command)
  
  if command == '/hi':
    bot.sendMessage(chat_id, str("Hi!"))
  elif command == '/time':
    bot.sendMessage(chat_id, str("Time:") + str(now.hour) + str(":") + str(now.minute))
  elif command == '/date':
    bot.sendMessage(chat_id, str("Date:") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
  elif command == '/image':
    camera = PiCamera();   
    camera.start_preview()   
    camera.capture('/home/img.jpg',resize=(640,480))   
    time.sleep(2)   
    camera.stop_preview()   
    camera.close()   
    Seding picture   
    bot.sendPhoto(chat_id, open('/home/img.jpg', 'rb'))
    bot.sendMessage(chat_id, str("Time:") + str(now.hour) + str(":") + str(now.minute))  
  elif command == '/file':
    bot.sendMessage(chat_id, document = open('/home/telegram.txt'))
    
bot = telepot.Bot('5790505945:AAGf0gTk8LD3k4IXhdQog5YQezat2YyTFZQ')
print(bot.getMe())

MassegeLoop(bot, handle).run_as_thread()
print('Listening...')

while 1:
  time.sleep(10)