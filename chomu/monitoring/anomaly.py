import psutil
import time
import threading
from collections import defaultdict

class AnomalyDetector:
    def __init__(self, interval=5, mem_threshold_mb=200, cpu_threshold=80):
        self.interval = interval
        self.mem_threshold_mb = mem_threshold_mb
        self.cpu_threshold = cpu_threshold
        self.running = False
        self.anomalies = defaultdict(list)

    def monitor_service(self, pid, service_name):
        try:
            proc = psutil.Process(pid)
            while self.running:
                mem_mb = proc.memory_info().rss / 1024 / 1024
                cpu = proc.cpu_percent(interval=1)
                if mem_mb > self.mem_threshold_mb:
                    self.anomalies[service_name].append(f"High memory: {mem_mb:.1f} MB")
                if cpu > self.cpu_threshold:
                    self.anomalies[service_name].append(f"High CPU: {cpu:.1f}%")
                time.sleep(self.interval)
        except psutil.NoSuchProcess:
            pass

    def start(self, service_pid_map):
        self.running = True
        self.threads = []
        for service, pid in service_pid_map.items():
            t = threading.Thread(target=self.monitor_service, args=(pid, service))
            t.daemon = True
            t.start()
            self.threads.append(t)

    def stop(self):
        self.running = False
        for t in self.threads:
            t.join()

    def get_anomalies(self):
        return dict(self.anomalies)
