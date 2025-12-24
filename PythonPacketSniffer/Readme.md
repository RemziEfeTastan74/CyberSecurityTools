Simple Packet Sniffer (Python)

A lightweight and educational network packet sniffer built with Python & Scapy.
This project captures TCP and UDP traffic related only to the user’s own machine and displays basic packet information in real time.

⚠️ This tool is developed for educational and ethical purposes only.

 Features:

Automatically detects your own local IP address

Captures incoming and outgoing traffic

Supports:

✅ TCP packets

✅ UDP packets

Displays:

Source IP & Port

Destination IP & Port

Filters packets so only traffic related to your system is shown

Simple, clean, and beginner-friendly code structure

 How It Works

The script first determines your local IP address.

It listens to network traffic using Scapy’s sniff() function.

Only packets where the source or destination matches your IP are processed.

Packet details are printed based on protocol type (TCP / UDP).

🛠 Requirements

Python 3.x

Scapy

Npcap (Windows users)

Install dependencies:
pip install scapy

 Usage

Run the script with administrator privileges:

python packet_sniffer.py


You will see real-time packet output like:

[TCP] 192.168.1.10:52344 -> 142.250.184.14:443
[UDP] 192.168.1.10:60637 -> 8.8.8.8:53

 Educational Purpose

This project was created to:

Learn how packet sniffing works

Understand TCP/UDP traffic structure

Practice Python networking concepts

Build a foundation for cybersecurity tools

 Disclaimer

This tool must not be used on networks you do not own or have permission to monitor.
The author is not responsible for misuse.

 Author

Efe Taştan
Python & Cybersecurity Enthusiast

🔗 LinkedIn: https://www.linkedin.com/in/remzi-efe-tastan/