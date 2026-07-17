# engine.py
import math
import random
import threading
import time

class MetricsEngine:
    def __init__(self):
        self.tick = 0
        self.lock = threading.Lock()
        self.metrics = {
            "cores": [0.0, 0.0, 0.0, 0.0],
            "ram": 0.0,
            "network_in": 0.0,
            "network_out": 0.0,
            "uptime": 0
        }
        self.start_time = time.time()
        self.active = False

    def start(self):
        self.active = True
        self.thread = threading.Thread(target=self._telemetry_loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.active = False

    def _telemetry_loop(self):
        while self.active:
            with self.lock:
                self.tick += 1
                # Complex wave oscillation formulas to mirror raw CPU workloads
                c1 = abs(math.sin(self.tick * 0.12)) * 50 + random.randint(5, 15)
                c2 = abs(math.cos(self.tick * 0.08)) * 60 + random.randint(5, 20)
                c3 = (math.sin(self.tick * 0.04) * math.cos(self.tick * 0.15) + 1) * 45 + 5
                c4 = random.randint(88, 99) if self.tick % 25 == 0 else abs(math.sin(self.tick * 0.06)) * 35 + 10
                
                self.metrics["cores"] = [c1, c2, c3, c4]
                self.metrics["ram"] = 54.2 + math.sin(self.tick * 0.015) * 4.8
                self.metrics["network_in"] = abs(math.sin(self.tick * 0.3)) * 340 + random.randint(10, 50)
                self.metrics["network_out"] = abs(math.cos(self.tick * 0.2)) * 120 + random.randint(5, 30)
                self.metrics["uptime"] = int(time.time() - self.start_time)
                
            time.sleep(0.15)

    def get_latest_snapshots(self):
        with self.lock:
            return self.metrics.copy()
