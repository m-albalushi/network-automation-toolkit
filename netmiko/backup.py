from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import os

os.makedirs("backups", exist_ok=True)
today = datetime.now().strftime("%Y-%m-%d")

username = input("Username: ")
password = getpass("Password: ")

with open("devices.txt") as f:
    ips = [line.strip() for line in f if line.strip()]

ok, failed = 0, 0
for ip in ips:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }
    try:
        conn = ConnectHandler(**device)
        hostname = conn.find_prompt().strip("#>")
        config = conn.send_command("show running-config")
        filename = f"backups/{hostname}_{today}.cfg"
        with open(filename, "w") as out:
            out.write(config)
        conn.disconnect()
        print(f"OK     {ip} -> {filename}")
        ok += 1
    except Exception as e:
        print(f"FAILED {ip}: {e}")
        failed += 1

print(f"\nDone: {ok} OK, {failed} failed")
