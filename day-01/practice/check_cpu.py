#current cpu usage 
import psutil
def check_cpu_threshold():
    cpu_threshold = 75  # set CPU usage threshold percentage
    current_cpu = psutil.cpu_percent(interval=1)

    if current_cpu > cpu_threshold:
        print(f"Warning: CPU Alert Email sent! Current CPU usage is {current_cpu}%")
    else:
        print(f"CPU usage is normal at {current_cpu}%")

check_cpu_threshold()