from netmiko import ConnectHandler
from datetime import datetime
import os

os.makedirs("backups", exist_ok=True)
today = datetime.now().strftime("%Y-%m-%d")

# line 1 is the username, line 2 is the password
with open("credentials.txt") as f:
    lines = f.read().splitlines()
username = lines[0]
password = lines[1]

# one IP per line
with open("devices.txt") as f:
    ips = f.read().splitlines()

for ip in ips:
    ip = ip.strip()
    if ip == "":
        continue

    try:
        conn = ConnectHandler(
            device_type="cisco_ios",
            host=ip,
            username=username,
            password=password,
        )

        # the prompt looks like SW1#, so remove the # to get the name
        hostname = conn.find_prompt().strip("#>")
        config = conn.send_command("show running-config")

        file_name = "backups/" + hostname + "_" + today + ".cfg"
        with open(file_name, "w") as backup_file:
            backup_file.write(config)

        conn.disconnect()
        print("OK     " + hostname + " (" + ip + ")")

    except Exception as e:
        # if one switch is down, carry on with the next one
        print("FAILED " + ip + ": " + str(e))
