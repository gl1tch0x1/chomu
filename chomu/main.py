import sys
from chomu.utils.common import check_root, confirm_action, safe_input
from .service_manager import (
    get_running_services,
    show_service_table,
    show_service_details,
    show_all_processes,
    kill_service,
    kill_all_services,
    stop_service,
    stop_all_services
)

def menu():
    services = get_running_services()
    show_service_table(services)

    print("""
Options:
  [s <ID>] Show details of a service
  [p <ID>] Show all processes of a service
  [k <ID>] Kill a service's main PID
  [K] Kill all services
  [t <ID>] Stop/deactivate a service
  [T] Stop all services
  [r] Refresh
  [q] Quit
""")

    choice = safe_input("Enter command: ").strip().split()
    if not choice:
        return

    cmd = choice[0].lower()
    try:
        if cmd == 's' and len(choice) == 2:
            idx = int(choice[1])
            show_service_details(services[idx]["unit"])
        elif cmd == 'p' and len(choice) == 2:
            idx = int(choice[1])
            show_all_processes(services[idx]["unit"])
        elif cmd == 'k' and len(choice) == 2:
            idx = int(choice[1])
            if confirm_action("Kill this service's PID?"):
                kill_service(services, idx)
        elif cmd == 'k' or cmd == 'kall':
            if confirm_action("Kill ALL running service PIDs?"):
                kill_all_services(services)
        elif cmd == 't' and len(choice) == 2:
            idx = int(choice[1])
            if confirm_action(f"Stop {services[idx]['unit']}?"):
                stop_service(services[idx]["unit"])
        elif cmd == 'tall' or cmd == 't' or cmd == 'T':
            if confirm_action("Stop ALL running services?"):
                stop_all_services(services)
        elif cmd == 'r':
            return "refresh"
        elif cmd == 'q':
            sys.exit(0)
        else:
            print("Invalid option.")
    except (ValueError, IndexError):
        print("Invalid service ID.")

def main():
    check_root()
    while True:
        result = menu()
        if result != "refresh":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
