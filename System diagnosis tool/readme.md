# System Diagnosis Tool

## Overview
The System Diagnosis Tool is designed to collect and display key system information for diagnostic purposes. It includes scripts written in Python and Bash to provide comprehensive system diagnostics, helping to identify potential issues and ensure system health.

## Scripts

### `diagnosis-tool.py`
This Python script performs the following tasks:
- **System Information**: Retrieves basic system information such as OS, OS version, processor, machine type, and system uptime.
- **CPU and Memory Check**: Monitors CPU and memory usage, identifying high usage issues.
- **Disk Check**: Checks disk space usage and identifies low disk space issues.
- **Malicious File Scan**: Scans a specified directory for malicious files using a simple YARA rule.
- **Log Generation**: Generates and saves a log file containing system information, CPU and memory usage, disk information, and results of the malicious file scan.

### `diagnosis-tool.sh`
This Bash script performs the following tasks:
- **System Information**: Displays system information using `hostnamectl`.
- **CPU Information**: Displays CPU model name, architecture, and CPU MHz.
- **Memory Usage**: Displays memory usage using `free -h`.
- **Disk Usage**: Displays disk usage using `df -h`.
- **Network Configuration**: Displays network configuration using `ip a`.
- **Active Connections**: Displays active network connections using `ss -tunlp`.
- **Running Services**: Lists running services using `systemctl`.
- **Recent Login Attempts**: Displays the last 5 login attempts using `last`.
- **Listening Ports**: Displays listening ports using `ss -tuln`.
- **System Updates Status**: Checks for available system updates using `apt` or `yum`.
- **Malicious File Scan**: Scans the system for potentially malicious files and lists them if found.

## Author
Emilio Shakhawat