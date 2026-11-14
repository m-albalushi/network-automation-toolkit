# Cisco Switch Backup and Information Collection

## Project Overview

This project uses Ansible to automate configuration backups and information collection from Cisco IOS switches.

The playbook connects to multiple switches using SSH, backs up their running configurations, collects hardware information, executes show commands, and saves the results on the Ubuntu Ansible controller.

## Requirements

- Ubuntu Linux (Ansible Controller)
- Ansible installed
- Cisco IOS Ansible collection
- SSH connectivity to Cisco switches
- Cisco switches configured for SSH access

## Project Structure

```text
Ansible_Project/
├── Switches.yml
├── inventory.example.ini
├── README.md
└── .gitignore
```

## What the Playbook Does

1. **Backup Configuration:** Backs up the running configuration of each switch into the `backups` folder.
2. **Gather Hardware Facts:** Collects hardware information using the Cisco IOS facts module.
3. **Run Show Commands:** Executes commands such as `show version`, `show inventory`, `show interfaces status`, `show vlan brief`, and `show cdp neighbors`.
4. **Check Switch Stack:** Attempts to run `show switch`. Unsupported commands are ignored so the playbook can continue.
5. **Create Information Folder:** Ensures the `info` folder exists on the Ubuntu controller.
6. **Save Information:** Combines command outputs and saves them into separate text files for each switch.

## How to Run

1. Clone the repository.
2. Configure your own inventory with your switch IP addresses and SSH credentials.
3. Run the playbook:

```bash
ansible-playbook Switches.yml
```


## Generated Output

After running the playbook, the following folders and files are generated automatically:

```text
backups/
├── SW1.cfg
└── SW2.cfg

info/
├── SW1.txt
└── SW2.txt
```

- `.cfg` files contain running configuration backups.
- `.txt` files contain collected switch command outputs.


## Purpose

The goal of this project is to reduce manual network administration tasks, simplify configuration backups, and make Cisco switch information easier to collect and review.
