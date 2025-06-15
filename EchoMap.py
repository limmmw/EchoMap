import subprocess
import concurrent.futures
import time
import os

def show_banner():
    monster_green = "\033[1;92m"
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
timeout_seconds = 20

active_ips = []

def ping(ip):
    try:
        result = subprocess.run(
            ['ping', '-c', '1', '-W', '1', ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            active_ips.append(ip)
    except:
        pass

if __name__ == "__main__":
    show_banner()
    print(f"[i] start to ping from {base_ip}1 - {base_ip}254 in {timeout_seconds} seconds...\n")

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_limit) as executor:
        futures = []
        for i in ip_range:
            ip = f"{base_ip}{i}"
            futures.append(executor.submit(ping, ip))

        concurrent.futures.wait(futures, timeout=timeout_seconds)

    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"\n{YELLOW}=== Active IP/Device ==={RESET}")
    for ip in active_ips:
        print(f"{YELLOW}[+]Active {ip} {RESET}")

    print(f"\n{YELLOW}Total Active: {len(active_ips)} IP{RESET}")