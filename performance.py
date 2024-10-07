import psutil
import time


def display_cpu_info():
    # Display CPU count
    print(f"Number of CPUs: {psutil.cpu_count(logical=True)}")

    # CPU utilization per core
    print("CPU usage per core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")

    # Average CPU utilization
    print(f"Average CPU usage: {psutil.cpu_percent(interval=1)}%")

    # CPU frequency information
    cpu_freq = psutil.cpu_freq()
    print(f"Current CPU frequency: {cpu_freq.current:.2f} Mhz")
    print(f"Min CPU frequency: {cpu_freq.min:.2f} Mhz")
    print(f"Max CPU frequency: {cpu_freq.max:.2f} Mhz")

    # CPU load averages (1, 5, 15 minutes)
    load1, load5, load15 = psutil.getloadavg()
    print(f"System Load (1 min): {load1}")
    print(f"System Load (5 min): {load5}")
    print(f"System Load (15 min): {load15}")

    # Total CPU time spent (user, system, idle)
    cpu_times = psutil.cpu_times()
    print(f"CPU times: User: {cpu_times.user} System: {cpu_times.system} Idle: {cpu_times.idle}")


if __name__ == "__main__":
    while True:
        print("\nFetching CPU performance metrics...\n")
        display_cpu_info()
        time.sleep(5)  # Fetch every 5 seconds
