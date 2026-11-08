from netmiko import ConnectHandler
from getpass import getpass

ip = input("Device IP: ")
username = input("Username: ")
password = getpass("Password: ")

device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": username,
    "password": password,
}

conn = ConnectHandler(**device)
output = conn.send_command("show version")
print(output)
conn.disconnect()
