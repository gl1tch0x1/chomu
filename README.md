

# Chomu - Linux Service Manager

<p align="center">
	<img src="https://img.shields.io/badge/Chomu-Production%20Ready-brightgreen" alt="Chomu Production Ready"/>
</p>

---

## 📖 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [CLI Commands](#cli-commands)
- [Example Output](#example-output)
- [Updating Chomu](#updating-chomu)
- [Uninstallation](#uninstallation)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

---

Chomu is a powerful and user-friendly command-line tool for Linux that allows you to view, manage, and control running system services interactively. It provides a clear overview of all running services, lets you inspect details, manage processes, and perform service actions with ease.

---



## 🚀 Features

- **List Running Services:**
	- Displays all running services with ID, unit name, PID, memory usage, status (color-coded), and description.
- **Service Details:**
	- View detailed information and the last 20 logs for any running service.
- **Process Inspection:**
	- List all processes spawned by a service, including memory usage.
- **Kill/Stop Services:**
	- Terminate or stop any service or all running services at once.
- **Interactive CLI:**
	- Menu-driven interface for easy navigation and command execution.
- **Root Check:**
	- Ensures the tool is run with root privileges for safe operation.
- **Auto-Updater:**
	- Use `updater.sh` to check for and install the latest version from GitHub.


### 🔒 Advanced Cybersecurity & Monitoring Features

- **Anomaly Detection:**
	- Detects abnormal CPU/memory usage or unexpected service restarts.
- **Service Hardening Recommendations:**
	- Warns about insecure configurations (e.g., SSH root login enabled).
- **Real-Time Monitoring & Alerts:**
	- Live updates and notifications for service state/resource changes.
- **Audit Logging:**
	- Logs all actions (service stops, kills, etc.) with timestamps and user info.
- **Threat Intelligence Integration:**
	- Checks running services/processes against threat intelligence feeds.
- **Automated Incident Response:**
	- User-defined rules for auto-restart/kill and a panic button for emergencies.
- **Service Integrity Checking:**
	- Verifies service binaries/configs against known-good hashes.
- **Role-Based Access Control (RBAC):**
	- User authentication for sensitive actions.
- **Network Connections View:**
	- Shows active network connections for each service/process.
- **SIEM/SOAR Integration:**
	- Export logs/events to SIEM platforms (Splunk, ELK, etc.).
- **Whitelisting/Blacklisting:**
	- Define allowed/blocked services and enforce policies.
- **Scheduled Security Scans:**
	- Integrate with tools like Lynis and display scan results in the CLI.

---

---


## ⚡ Quick Start

1. **Clone and Install:**
	```bash
	git clone https://github.com/gl1tch0x1/chomu.git
	cd chomu
	chmod +x install.sh
	./install.sh
	```
2. **Run the Tool:**
	```bash
	sudo chomu
	```
3. **Update Anytime:**
	```bash
	chmod +x updater.sh
	./updater.sh
	```

---

## 🛠️ Installation

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
- Install all dependencies (`psutil`, `tabulate`, `termcolor`, and more)
- Install Chomu globally as a CLI tool

---


## 🖥️ Usage


### Start the Tool
```bash
sudo chomu
```

---

## 💡 CLI Commands

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

---


## 📊 Example Output

```
╒════╤══════════════════════════════╤════════╤══════════╤══════════╤═══════════════════════════╕
│ ID │ UNIT                         │ PID    │ MEMORY   │ STATUS   │ DESCRIPTION               │
╞════╪══════════════════════════════╪════════╪══════════╪══════════╪═══════════════════════════╡
│ 0  │ ssh.service                  │ 1245   │ 12.4 MB  │ active   │ OpenSSH server daemon      │
│ 1  │ cron.service                 │ 678    │ 2.3 MB   │ active   │ Regular background program │
╘════╧══════════════════════════════╧════════╧══════════╧══════════╧═══════════════════════════╛
```

---


## 🔄 Updating Chomu

To check for updates and upgrade to the latest version:
```bash
chmod +x updater.sh
./updater.sh
```

---


## 🗑️ Uninstallation

To uninstall Chomu:
```bash
sudo pip uninstall chomu
```
Or remove the installed files from `/usr/local/bin/chomu` and the Python site-packages directory.

---


## ⚙️ Requirements
- Python 3.8+
- Linux system with `systemctl` and `journalctl`
- `psutil`, `tabulate`, `termcolor`, `requests`, `PyYAML` (installed automatically)
- (Optional for advanced features) `lynis`, access to threat intelligence APIs, SIEM/SOAR endpoints

---


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


## 👤 Author
- Cyb3rspl0it (gl1tch0x1)

---



## 🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue or submit a PR on GitHub.
If you want to add new security modules, see the `chomu/security/` and `chomu/monitoring/` directories for examples.

---


## ⚠️ Disclaimer


Chomu is provided as-is, without warranty. Use at your own risk. Always review actions before killing or stopping system services.

---

## 📚 Full Documentation

For complete documentation, usage examples, and advanced configuration, please see the [Chomu Wiki](https://github.com/gl1tch0x1/chomu/wiki) or open the `docs/` folder (if available). You can also click the Table of Contents above to jump to any section.

