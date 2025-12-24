#Check the CPU, Disk & RAM usage of the system

import psutil

cpu_threshold = 75  # CPU usage threshold percentage
disk_threshold = 80  # Disk usage threshold percentage
ram_threshold = 80  # RAM usage threshold percentage

def check_system_health():
    #Check CPU usage
    current_cpu = psutil.cpu_percent(interval=1)
    if current_cpu > cpu_threshold:
        print(f"-------------------------------------\nWarning: CPU usage is high at {current_cpu}%\n-------------------------------------")
    else:
        print(f"-------------------------------------\nCPU usage is normal at {current_cpu}%\n-------------------------------------")
    #Check Disk usage
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > disk_threshold:
        print(f"Warning: Disk usage is high at {disk_usage.percent}%\n-------------------------------------")
    else:
        print(f"Disk usage is normal at {disk_usage.percent}%\n-------------------------------------")
    #Check RAM usage
    ram_usage = psutil.virtual_memory()
    if ram_usage.percent > ram_threshold:
        print(f"Warning: RAM usage is high at {ram_usage.percent}%\n-------------------------------------")
    else:
        print(f"RAM usage is normal at {ram_usage.percent}%\n-------------------------------------")

check_system_health()