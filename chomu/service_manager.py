import subprocess
import psutil
from tabulate import tabulate
from .utils import format_memory_kb_to_mb

def get_running_services():
    services = []
    try:
        result = subprocess.run(
            ["systemctl", "list-units", "--type=service", "--state=running", "--no-pager", "--no-legend"],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.strip().split("\n")
        for idx, line in enumerate(lines):
            parts = line.split(None, 4)
            if len(parts) < 5:
                continue
            unit, load, active, sub, description = parts
            pid = get_main_pid(unit)
            mem_kb = get_memory_usage_kb(pid) if pid else 0
            services.append({
                "id": idx,
                "unit": unit,
                "pid": pid if pid else "N/A",
                "mem_kb": mem_kb,
                "status": active,
                "description": description
            })
    except subprocess.CalledProcessError as e:
        print(f"Error fetching services: {e}")
    return services

def get_main_pid(service_name):
    try:
        result = subprocess.run(
            ["systemctl", "show", "-p", "MainPID", "--value", service_name],
            capture_output=True, text=True, check=True
        )
        pid = int(result.stdout.strip())
        return pid if pid > 0 else None
    except (subprocess.CalledProcessError, ValueError):
        return None

def get_memory_usage_kb(pid):
    try:
        process = psutil.Process(pid)
        return int(process.memory_info().rss / 1024)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return 0

def show_service_table(services):
    if not services:
        print("No running services found.")
        return
    table_data = [
        [srv["id"], srv["unit"], srv["pid"], format_memory_kb_to_mb(srv["mem_kb"]), srv["status"], srv["description"]]
        for srv in services
    ]
    print(tabulate(table_data, headers=["ID", "UNIT", "PID", "MEMORY", "STATUS", "DESCRIPTION"], tablefmt="fancy_grid"))

def kill_service(services, service_id):
    try:
        service = next(s for s in services if s["id"] == service_id)
        pid = service["pid"]
        if pid == "N/A":
            print(f"[{service['unit']}] has no PID to kill.")
            return
        psutil.Process(pid).terminate()
        print(f"Killed PID {pid} for service {service['unit']}.")
    except (StopIteration, psutil.NoSuchProcess):
        print("Invalid service ID or process no longer exists.")

def kill_all_services(services):
    for srv in services:
        if isinstance(srv["pid"], int):
            try:
                psutil.Process(srv["pid"]).terminate()
                print(f"Killed PID {srv['pid']} ({srv['unit']})")
            except psutil.NoSuchProcess:
                print(f"PID {srv['pid']} already stopped.")

def stop_service(service_name):
    subprocess.run(["systemctl", "stop", service_name])

def stop_all_services(services):
    for srv in services:
        subprocess.run(["systemctl", "stop", srv["unit"]])

def show_service_details(service_name):
    print(f"\n=== Details for {service_name} ===\n")
    subprocess.run(["systemctl", "status", service_name, "--no-pager"])
    print("\n---- Last 20 logs ----")
    subprocess.run(["journalctl", "-u", service_name, "-n", "20", "--no-pager"])

def show_all_processes(service_name):
    pid = get_main_pid(service_name)
    if not pid:
        print("No running PID for this service.")
        return
    try:
        process = psutil.Process(pid)
        children = process.children(recursive=True)
        all_procs = [process] + children

        table_data = []
        total_mem = 0
        for proc in all_procs:
            mem_kb = int(proc.memory_info().rss / 1024)
            total_mem += mem_kb
            table_data.append([proc.pid, proc.name(), format_memory_kb_to_mb(mem_kb)])

        print(tabulate(table_data, headers=["PID", "Process Name", "Memory"], tablefmt="grid"))
        print(f"\nTotal Memory Used: {format_memory_kb_to_mb(total_mem)}")
    except psutil.NoSuchProcess:
        print("Process no longer exists.")
