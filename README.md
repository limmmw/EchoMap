# Parallel Network Ping Scanner
This Python script is designed to **map active devices on a local network** using parallel pinging. It performs a **fast and concurrent ICMP scan** over a specified IP range and stops after a fixed timeout (10 seconds by default). Only devices that respond to ping within that time window are shown.

---

## 📌 Features
- Parallel ping scanning using multithreading
- Stops automatically after 10 seconds
- Displays a list of responsive IP addresses
- Shows the total number of active hosts
- Customizable IP base and range

## 🧠 Purpose
This tool helps identify **which devices are currently active** on your local network using **ICMP echo requests (ping)**. It's useful for:
- Network diagnostics
- Mapping connected clients
- Detecting unauthorized users
- Lightweight host discovery

## 🚀 Requirements
- Python 3.x
- Linux (or WSL/macOS) with `ping` command available

## ⚙️ Configuration
You can adjust the target IP range and subnet directly in the script:

1. Edit
   ```python
   base_ip = "192.168.100."       # Change to match your local network
   ip_range = range(1, 255)       # Range of host addresses
   timeout_seconds = 10           # How long the scan runs

## ▶️ Usage

2. Download:
   ```python
   git clone https://github.com/limmmw/continuous-ping.git
   cd EchoMap

3. run:
   ```python
   echomap.py

4. Example Output:
   ```python

   ▓█████  ▄████▄   ██░ ██  ▒█████   ███▄ ▄███▓ ▄▄▄       ██▓███ 
   ▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒
   ▒███   ▒▓█    ▄ ▒██▀▀██░▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒
   ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒
   ░▒████▒▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░
   ░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░
    ░ ░  ░  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░▒ ░     
      ░   ░         ░  ░░ ░░ ░ ░ ▒  ░      ░     ░   ▒   ░░       
      ░  ░░ ░       ░  ░  ░    ░ ░         ░         ░  ░         
          ░                                                       
             Developed by limmmw

   [i] start to ping from 192.168.100.1 - 192.168.100.254 in 10 seconds...
   === IP Aktif ===
   192.168.100.1 active
   192.168.100.5 active
   192.168.100.23 active
   Total Active: 3 IP

5. if you want to run the program anywhere, make this configuration:
   ```python
   sudo nano /usr/bin/EchoMap.sh
   ## write down this scripting program
   sudo python3 /yourpath/EchoMap/EchoMap.py
   ## save and you can run the program anywhere with:
   sudo bash EchoMap.sh

## 📁 Output
The program prints only the IP addresses that responded within the timeout window, along with the total count.

## 🛠️ Notes
- Some devices may not respond to ping due to firewalls or OS settings (e.g., Windows with ICMP blocked).
- The scan is limited to 10 seconds to keep it lightweight and avoid triggering alerts on monitored networks.