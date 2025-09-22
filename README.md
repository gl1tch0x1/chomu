
# Chomu - Linux Service Manager

Chomu is a powerful and user-friendly command-line tool for Linux that allows you to view, manage, and control running system services interactively. It provides a clear overview of all running services, lets you inspect details, manage processes, and perform service actions with ease.

---

## Features

- **List Running Services:**
	- Displays all running services with ID, unit name, PID, memory usage, status (color-coded), and description.
- **Service Details:**
	- View detailed information and the last 20 logs for any running service.
- **Process Inspection:**
	- List all processes spawned by a service, including memory usage.
- **Kill Services:**
	- Terminate the main PID of a service or all running services at once.
- **Stop Services:**
	- Stop/deactivate a specific service or all running services using `systemctl`.
- **Interactive CLI:**
	- Menu-driven interface for easy navigation and command execution.
- **Root Check:**
	- Ensures the tool is run with root privileges for safe operation.
- **Auto-Updater:**
	- Use `updater.sh` to check for and install the latest version from GitHub.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/gl1tch0x1/chomu.git
cd chomu
```

### 2. Run the Installer
```bash
chmod +x install.sh
./install.sh
```
This will:
- Check for Python 3 and required tools
- Create a virtual environment
- Install all dependencies (`psutil`, `tabulate`, `termcolor`)
- Install Chomu globally as a CLI tool

---

## Usage

### Start the Tool
```bash
sudo chomu
```

### Interactive Commands (inside Chomu)
| Command      | Description                                 |
|--------------|---------------------------------------------|
| `s <ID>`     | Show details of a service                   |
| `p <ID>`     | Show all processes of a service             |
| `k <ID>`     | Kill a service's main PID                   |
| `K`          | Kill all services                           |
| `t <ID>`     | Stop/deactivate a service                   |
| `T`          | Stop all services                           |
| `r`          | Refresh the list                            |
| `q`          | Quit the tool                               |

---

## Example Output

```
╒════╤══════════════════════════════╤════════╤══════════╤══════════╤═══════════════════════════╕
│ ID │ UNIT                         │ PID    │ MEMORY   │ STATUS   │ DESCRIPTION               │
╞════╪══════════════════════════════╪════════╪══════════╪══════════╪═══════════════════════════╡
│ 0  │ ssh.service                  │ 1245   │ 12.4 MB  │ active   │ OpenSSH server daemon      │
│ 1  │ cron.service                 │ 678    │ 2.3 MB   │ active   │ Regular background program │
╘════╧══════════════════════════════╧════════╧══════════╧══════════╧═══════════════════════════╛
```

---

## Updating Chomu

To check for updates and upgrade to the latest version:
```bash
chmod +x updater.sh
./updater.sh
```

---

## Uninstallation

To uninstall Chomu:
```bash
sudo pip uninstall chomu
```
Or remove the installed files from `/usr/local/bin/chomu` and the Python site-packages directory.

---

## Requirements
- Python 3.8+
- Linux system with `systemctl` and `journalctl`
- `psutil`, `tabulate`, `termcolor` (installed automatically)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
- Cyb3rspl0it (gl1tch0x1)

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue or submit a PR on GitHub.

---

## Disclaimer

Chomu is provided as-is, without warranty. Use at your own risk. Always review actions before killing or stopping system services.

