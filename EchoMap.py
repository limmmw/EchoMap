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

# Konfigurasi
base_ip = "192.168.100."
ip_range = range(1, 255)
thread_limit = 100
timeout_seconds = 10

# ANSI colors
YELLOW = "\033[93m"
RESET = "\033[0m"

# Untuk menyimpan IP yang aktif
active_ips = []

# Fungsi ping
def ping(ip):
    try:
        result = subprocess.run(
            ['ping', '-c', '1', '-W', '1', ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            return ip
    except:
        return None

if __name__ == "__main__":
    show_banner()
    print(f"[i] start to ping from {base_ip}1 - {base_ip}254 in {timeout_seconds} seconds...\n")

    # Mulai semua tugas
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_limit) as executor:
        futures = {executor.submit(ping, f"{base_ip}{i}"): f"{base_ip}{i}" for i in ip_range}

        # Tunggu 10 detik penuh
        time.sleep(timeout_seconds)

        # Setelah itu, ambil hanya hasil yang sudah selesai
        for future in futures:
            if future.done():
                result = future.result()
                if result:
                    active_ips.append(result)

    # Tampilkan hasil
    print(f"\n{YELLOW}=== Active IP/Device ==={RESET}")
    for ip in active_ips:
        print(f"{YELLOW}{ip} active{RESET}")

    print(f"\nTotal Active: {len(active_ips)} IP")