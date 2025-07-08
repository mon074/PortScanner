#port scanner phase2: Speed (multithreading is used for increasing the scanning speed)

import socket
import threading


target = input("Enter the target IP or a website: ")
startport = int(input("Enter start port: "))
endport = int(input("Enter end port: "))


def scan_port(portn):
    soc = socket.socket()
    result = soc.connect_ex((target,portn))
    if result == 0:
        print(f"port {portn} is open")

threads = []
for port in range(startport,(endport+1)):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print("Scanning completed ✅")
    


