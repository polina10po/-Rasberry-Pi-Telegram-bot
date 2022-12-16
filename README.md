# Rasberry-Pi-Telegram-bot 

Raspberry Pi — это одноплатный компьютер, построенный на ARM-архитектуре и обладающий небольшой ценой и скромными габаритами. У него есть процессор, ОЗУ, видеоускоритель, а некоторые вариации обладают множеством полноценных разъёмов, включая USB, Ethernet и microHDMI. Иными словами, он полностью готов к работе из коробки. Микрокомпьютер разрабатывается британской компанией Raspberry Pi Foundation. Изначально разработанный для обучения, Raspberry Pi обрёл широкое распространение среди энтузиастов.

**Цель работы** - создать телеграмм бот для обмена данными между Rasberry Pi и мобильным телефоном

___

### Ход работы

Сначала необходимо создать Telegram бот. Зайдем в телеграмм и зарегистрируем нового бота в BotFather `/newbot` и получим токен доступа

**Устанавливаем Telegram на Rasberry Pi**

```
sudo apt-get install python-pip
sudo pip install telepot
```

Подключаем библиотеку telepot для управления телеграмм ботом. Библиотеки time и datetime нужны для считывания текущего времени в Rasberry Pi. 

```
import time, datetime
import telepot
```

Далее создадим функцию `handle`, которая будет отвечать за выполнение поступающих запросов из Telegram.
Сначала будем записывать идентификатор чата `chat_id = msg['chat']['id']` и сам текст сообщения `command = msg['text']`. Текст принятого сообщения также выводится в терминале Rasberry Pi `print('Received:')` `print(command)`.

Далее функция будет сравнивать текст принятого сообщения с заранее определенными командами.
Если бот получает команду '/hi', то мы будем отвечать на него "Hi!"

```
if command == '/hi':
bot.sendMessage(chat_id, str("Hi!")
```

Если бот получает команду '/date', то мы получает текущую дату на Rasberry Pi

```
elif command == '/date
bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year)
```

Если бот получает команду '/time', то мы получает текущее время на Rasberry Pi

```
elif command == '/time'
bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str("/") + str(now.minute)
```

Если бот получает команду '/file', то мы файл, хранящийся на Rasberry Pi

```
elif command == '/file'
bot.sendMessage(chat_id, document = open('/home/telegram.txt'))
```

Если бот получает команду '/image', то мы фотографию, которую мы сделали на камере Rasberry Pi

```
elif command == '/image'
camera = PiCamera()
camera.start_preview()
camera.capture('/home/img.jpg', resize=(640,480))
time.sleep(2)
camera.stop_preview()
camera.close()
bot.sendMessage(chat_id, open('/home/img.jpg'))
```

Далее передадим написанный скрипт Telegram боту, через полученный токен

`bot = telepot.Bot('5790505945:AAGf0gTk8LD3k4IXhdQog5YQezat2YyTFZQ')`

___

**Проверка работы Telegram бота**

___

### Заключение

В ходе выполнения работы был создан Telegram бот, через который мы можем удаленно подключиться к Rasberry Pi и получать изображение с камеры, файлы, текущую дату и время.



