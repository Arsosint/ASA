import random
import string
import time
from mineflayer import Bot

def random_name(length=10):
    letters = string.ascii_lowercase  # Используем только маленькие буквы
    return ''.join(random.choice(letters) for _ in range(length))

def create_bot(server_address, version):
    bot = Bot(random_name(), version=version)
    
    @bot.event
    def on_spawn():
        while True:
            bot.chat("привет")
            bot.jump()
            time.sleep(0.1) 

    bot.connect(server_address)

def main():
    server_address = input("Выберите адрес сервера: ")
    version = input("Выберите версию Minecraft (например, '1.16.4'): ")
    num_bots = int(input("Выберите количество ботов: "))

    for _ in range(num_bots):
        create_bot(server_address, version)

if __name__ == "__main__":
    main()
