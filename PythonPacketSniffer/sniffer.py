from scapy.all import sniff, IP, TCP, UDP
import socket


def get_own_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


MY_IP = get_own_ip()
print(f"[+] Monitoring traffic for host IP: {MY_IP}\n")


def packet_handler(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        if src == MY_IP or dst == MY_IP:

            if TCP in packet:
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                print(f"[TCP] {src}:{sport} -> {dst}:{dport}")

            elif UDP in packet:
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                print(f"[UDP] {src}:{sport} -> {dst}:{dport}")

            else:
                print(f"[IP ] {src} -> {dst}")


try:
    sniff(prn=packet_handler)
except KeyboardInterrupt:
    print("\n[!] Packet sniffing stopped by user.")