# Cisco Switch Configuration Backup Using Netmiko

This project uses Python and Netmiko to automate configuration backups of Cisco IOS switches.

The script connects to multiple switches using SSH, retrieves their running configurations, and saves each configuration into a separate file on the local machine.

## Requirements

- Ubuntu Linux
- Python 3
- Netmiko
- SSH access to Cisco switches
- Cisco IOS devices

## Project Structure

```text
netmiko/
├── backup.py
├── requirements.txt
├── devices.example.txt
├── credentials.example.txt
├── README.md
└── .gitignore
```

## Setup

### 1. Create a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure credentials

Create a file named `credentials.txt`:

```text
YOUR_USERNAME
YOUR_PASSWORD
```

Line 1 contains the SSH username.

Line 2 contains the SSH password.

### 4. Add switch IP addresses

Create a file named `devices.txt`:

```text
192.0.2.10
192.0.2.11
```

Add one switch IP address per line. Replace these example addresses with your own device IPs.

## Run the Script

```bash
python backup.py
```

The script will:

1. Create the backups folder if it doesn't exist.
2. Read the SSH credentials.
3. Read the switch IP addresses.
4. Connect to each switch using Netmiko.
5. Retrieve the running configuration.
6. Save the configuration using the switch hostname and current date.
7. Display successful or failed connections.

## Generated Output

After running the script:

```text
backups/
├── SW1_2026-11-14.cfg
└── SW2_2026-11-14.cfg
```

Each `.cfg` file contains the running configuration of its respective switch.
