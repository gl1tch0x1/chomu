# Chomu - Linux Service Manager

A command-line tool to view, manage, and control running services on Linux.

## Features
- List all running services with PID, memory usage, and status.
- View detailed information and logs of a service.
- Kill service PIDs or all services.
- Stop/deactivate services using systemctl.
- Inspect all processes spawned by a service.

## Installation
```bash
git clone https://github.com/gl1tch0x1/chomu.git
cd chomu
chmod +x install.sh
./install.sh
```

## Usage
Run the tool:
```bash
sudo chomu
```
## Example commands inside the tool:

* s 1   # Show details of service with ID 1
* p 2   # Show all processes of service with ID 2
* k 3   # Kill service with ID 3
* K     # Kill all services
* t 4   # Stop service with ID 4
* T     # Stop all services
* r     # Refresh list
* q     # Quit

## Sample output:

```bash
╒════╤══════════════════════════════╤════════╤══════════╤══════════╤═══════════════════════════╕
│ ID │ UNIT                         │ PID    │ MEMORY   │ STATUS   │ DESCRIPTION               │
╞════╪══════════════════════════════╪════════╪══════════╪══════════╪═══════════════════════════╡
│ 0  │ ssh.service                   │ 1245   │ 12.4 MB  │ active   │ OpenSSH server daemon      │
│ 1  │ cron.service                  │ 678    │ 2.3 MB   │ active   │ Regular background program │
╘════╧══════════════════════════════╧════════╧══════════╧══════════╧═══════════════════════════╛
```

