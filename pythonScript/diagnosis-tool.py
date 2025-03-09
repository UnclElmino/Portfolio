import psutil
import platform
import datetime

import yara
import os
import time

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

def scan_for_malicious_files(directory):
    """Scan for malicious files in the given directory."""
    # Define a simple YARA rule for demonstration purposes
    rules = yara.compile(source="""
    rule dummy_malware_rule {
        strings:
            $a = "malicious_string"
        condition:
            $a
    }
    """)

    malicious_files = []
    files_scanned = 0

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                matches = rules.match(file_path)
                if matches:
                    malicious_files.append(file_path)
            except Exception as e:
                print(f"Error scanning file {file_path}: {e}")

            files_scanned += 1
            print(f"Scanning files{'.' * (files_scanned % 3 + 1)}", end='\r')
            time.sleep(0.1)  # Simulate scanning delay

    print("\nScan complete.")
    if malicious_files:
        return malicious_files
    else:
        return ["No malicious files found"]

def generate_log():
    """Generate and save system diagnostics log."""
    system_info = get_system_info()
    cpu_memory = check_cpu_memory()
    disk_info = check_disk()
    malicious_files = scan_for_malicious_files("d:\\Work\\Projects\\System Diagnostic tool")
    
    log_data = {
        "Timestamp": str(datetime.datetime.now()),
        "System Info": system_info,
        "CPU & Memory": cpu_memory,
        "Disk Info": disk_info,
        "Malicious Files": malicious_files,
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

