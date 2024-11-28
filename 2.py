import random
import string
import time
from mineflayer import Bot

def random_name(length=10):
    letters = string.ascii_lowercase  # Используем только маленькие буквы
    return ''.join(random.choice(letters) for _ in range(length))

def create_bot(server_address, port, version):
    bot = Bot(random_name(), version=version)
    
    @bot.event
    def on_spawn():
        while True:
            bot.chat("привет")
            bot.jump()
            time.sleep(0.5)  # Задержка, чтобы избежать спама

    bot.connect(server_address, port)

def main():
    server_address = input("Выберите адрес сервера: ")
    port = int(input("Введите порт сервера: "))
    version = input("Выберите версию Minecraft (например, '1.16.4'): ")
    num_bots = int(input("Выберите количество ботов: "))

    for _ in range(num_bots):
        create_bot(server_address, port, version)

if __name__ == "__main__":
    main()
