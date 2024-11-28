import random
import string
from mcpi.minecraft import Minecraft
import time
import threading

def generate_random_name(length=16):
    """Генерирует случайное имя заданной длины."""
    letters = string.ascii_letters  # Буквы латинского алфавита
    return ''.join(random.choice(letters) for i in range(length))

def create_bot(host, port):
    """Создает бота и подключается к серверу Minecraft."""
    bot_id = generate_random_name()  # Генерация случайного имени
    mc = Minecraft.create(address=host, port=port)
    
    # Приветствие бота
    mc.postToChat(f"Bot {bot_id} has joined the server!")

    # Здесь можно добавить взаимодействие с сервером
    while True:
        time.sleep(5)  # Задержка для предотвращения избыточных запросов

# Настройки сервера
server_host = 'Topper1199191-PwlR.aternos.me'  # Укажите адрес сервера
server_port = 49773          # Укажите порт сервера

# Создание нескольких ботов
number_of_bots = 100  # Укажите количество ботов

for _ in range(number_of_bots):
    threading.Thread(target=create_bot, args=(server_host, server_port)).start()
