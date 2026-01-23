import psutil

cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
memory_usage = memory_info.percent

print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
