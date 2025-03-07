import psutil
import platform
import datetime

def get_system_info():
    """Retrieve basic system information."""
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "Machine": platform.machine(),
        "Uptime (seconds)": round(datetime.datetime.now().timestamp() - psutil.boot_time(), 2),
    }
    return system_info

def check_cpu_memory():
    """Check CPU and memory usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    issues = []
    if cpu_usage > 80:
        issues.append(f"⚠️ High CPU Usage: {cpu_usage}%")
    if memory.percent > 80:
        issues.append(f"⚠️ High Memory Usage: {memory.percent}%")
    
    return {
        "CPU Usage (%)": cpu_usage,
        "Memory Usage (%)": memory.percent,
        "Issues": issues
    }

def check_disk():
    """Check disk space usage."""
    disk = psutil.disk_usage('/')
    issues = []
    if disk.percent > 90:
        issues.append(f"⚠️ Low Disk Space: {disk.percent}% used")

    return {
        "Total Disk (GB)": round(disk.total / (1024**3), 2),
        "Used Disk (GB)": round(disk.used / (1024**3), 2),
        "Free Disk (GB)": round(disk.free / (1024**3), 2),
        "Usage (%)": disk.percent,
        "Issues": issues
    }

def generate_log():
    """Generate and save system diagnostics log."""
    system_info = get_system_info()
    cpu_memory = check_cpu_memory()
    disk_info = check_disk()
    
    log_data = {
        "Timestamp": str(datetime.datetime.now()),
        "System Info": system_info,
        "CPU & Memory": cpu_memory,
        "Disk Info": disk_info,
    }
    
    # Save log
    with open("system_diagnostics.log", "a") as log_file:
        log_file.write(str(log_data) + "\n\n")

    return log_data

if __name__ == "__main__":
    log_result = generate_log()
    
    # Display results
    for section, details in log_result.items():
        print(f"\n🔹 {section}:")
    
        if isinstance(details, dict):  # ✅ Check if details is a dictionary
            for key, value in details.items():
                print(f"   {key}: {value}")
        else:  # ✅ If it's a string (like Timestamp), print directly
            print(f"   {details}")

