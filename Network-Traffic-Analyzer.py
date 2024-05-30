from scapy.all import *
import threading
import msvcrt
import os

os.system('cls')
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("  _   _      _                      _        _______         __  __ _      ")
print(" | \ | |    | |                    | |      |__   __|       / _|/ _(_)     ")
print(" |  \| | ___| |___      _____  _ __| | ________| |_ __ __ _| |_| |_ _  ___ ")
print(" | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /______| | '__/ _` |  _|  _| |/ __|")
print(" | |\  |  __/ |_ \ V  V / (_) | |  |   <       | | | | (_| | | | | | | (__ ")
print(" |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\      |_|_|  \__,_|_| |_| |_|\___|")
print("")
print("                          Press: ESC to Stop                               ")
                                                                           
                                                                           


# Öffnen Sie die Datei zu Beginn des Programms im Schreibmodus, um sie zu leeren
with open('network_traffic.txt', 'w') as f:
    pass

def packet_callback(packet):
    # Öffnen Sie die Datei im Anhängemodus, um Pakete hinzuzufügen
    with open('network_traffic.txt', 'a') as f:
        f.write(str(packet) + '\n')

def stop_sniffing(packet):
    return stop_sniff

stop_sniff = False

def keyboard_listener():
    global stop_sniff
    while True:
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            if ord(key_stroke) == 27:  # ESC key
                stop_sniff = True
                break

keyboard_thread = threading.Thread(target=keyboard_listener, daemon=True)
keyboard_thread.start()

sniff(prn=packet_callback, stop_filter=stop_sniffing, store=0)
