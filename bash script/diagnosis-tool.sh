#!/bin/bash

# System Diagnosis Tool
# Author: Emilio Shakhawat
# Description: This tool collects and displays key system information for diagnosis.

# Check if script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root."
    exit 1
fi

# Display System Information
echo "================ SYSTEM INFORMATION ================"
hostnamectl

echo "================ CPU INFORMATION ======================"
lscpu | grep 'Model name\|Architecture\|CPU MHz'

echo "================ MEMORY USAGE ========================="
free -h

echo "================ DISK USAGE ==========================="
df -h

echo "================ NETWORK CONFIGURATION ================="
ip a | grep -A 5 "^[0-9]"

echo "================ ACTIVE CONNECTIONS ===================="
ss -tunlp

echo "================ RUNNING SERVICES ======================"
systemctl list-units --type=service --state=running

echo "================ RECENT LOGIN ATTEMPTS ================="
last -n 5

echo "================ LISTENING PORTS ======================="
ss -tuln

echo "================ SYSTEM UPDATES STATUS ================="
apt list --upgradable 2>/dev/null || yum check-update 2>/dev/null

echo "================ MALICIOUS FILE SCAN ==================="
echo -n "Scanning for malicious files..."
FOUND_FILES=$(find / -type f \( -name "*.sh" -o -name "*.py" -o -name "*.exe" \) -size +1M 2>/dev/null | pv -l -s $(find / -type f \( -name "*.sh" -o -name "*.py" -o -name "*.exe" \) -size +1M 2>/dev/null | wc -l))
if [ -z "$FOUND_FILES" ]; then
    echo " No malicious files found."
else
    echo "\nPotentially malicious files found:" 
    echo "$FOUND_FILES"
fi

echo "================ DIAGNOSIS COMPLETE ====================="
