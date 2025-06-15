import subprocess
import concurrent.futures
import time
import os
import platform
from queue import Queue

def show_banner():
    monster_green = "\033[38;2;255;76;76m"
    reset = "\033[0m"
    banner = r"""

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
             Developed by limmmw.
    """
    print(monster_green + banner + reset)

# Configuration
base_ip = "192.168.100."
ip_range = range(1, 255)
thread_limit = 100
ping_timeout = 2  # timeout per ping (in seconds)
retry_attempts = 2  # ping attempts per IP

active_ips = Queue()

# OS Check
is_windows = platform.system().lower() == "windows"
ping_cmd_base = ['ping', '-n', '1'] if is_windows else ['ping', '-c', '1', '-W', str(ping_timeout)]

def ping(ip):
    for _ in range(retry_attempts):
        try:
            result = subprocess.run(
                ping_cmd_base + [ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            if result.returncode == 0:
                active_ips.put(ip)
                return
        except:
            continue

if __name__ == "__main__":
    show_banner()
    print(f"[i] Start scanning from {base_ip}1 to {base_ip}254 using {thread_limit} threads...\n")

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_limit) as executor:
        futures = [executor.submit(ping, f"{base_ip}{i}") for i in ip_range]
        concurrent.futures.wait(futures)

    YELLOW = "\033[38;2;206;255;0m"
    RESET = "\033[0m"

    print(f"\n{YELLOW}=== Active IP/Device ==={RESET}")
    active_list = list(active_ips.queue)
    for ip in active_list:
        print(f"{YELLOW}[+] Active: {ip}{RESET}")

    print(f"\nTotal Active: {len(active_list)} IP/Device")
    print(f"Scan completed in {round(time.time() - start_time, 2)} seconds.")
