# Script to monitor CPU and RAM usage

import psutil

cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent


print(f"Consommation CPU: {cpu_usage} %")
print(f"Consommation RAM: {ram_usage} %")
# AUtres métriques peuvent être ajoutées ici
# Par exemple, utilisation du disque, réseau, etc.
disk_usage = psutil.disk_usage('/').percent
print(f"Consommation Disque: {disk_usage} %")
network_stats = psutil.net_io_counters()
print(f"Octets envoyés: {network_stats.bytes_sent}")
print(f"Octets reçus: {network_stats.bytes_recv}")
