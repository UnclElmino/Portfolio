# Automated System Diagnostics Tool

A simple Bash script that monitors system health, CPU/memory usage, disk space, and logs potential issues.

## Features
- **Cross-platform** (Linux)
- **Monitors CPU & Memory Usage**
- **Checks Disk Space Usage**
- **Displays system health information**
- **Detects potential issues and suggests solutions**

## Prerequisites
This script requires root privileges to run.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/system-diagnostics-tool.git
   cd system-diagnostics-tool
   ```

2. Make the script executable:
   ```bash
   chmod +x diagnosis-tool.sh
   ```

3. Run the script as root:
   ```bash
   sudo ./diagnosis-tool.sh
   ```

## Example Output
```
================ SYSTEM INFORMATION ================
   Static hostname: yourhostname
         Icon name: computer-vm
           Chassis: vm
        Machine ID: xxxxxxxx
           Boot ID: xxxxxxxx
  Operating System: Ubuntu 20.04.1 LTS
            Kernel: Linux 5.4.0-42-generic
      Architecture: x86-64

================ CPU INFORMATION ======================
   Architecture:        x86_64
   CPU op-mode(s):      32-bit, 64-bit
   Byte Order:          Little Endian
   Model name:          Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz
   CPU MHz:             3600.000

================ MEMORY USAGE =========================
              total        used        free      shared  buff/cache   available
   Mem:           15G        2.1G         11G        1.2M        1.8G         12G
   Swap:         2.0G          0B        2.0G

================ DISK USAGE ===========================
   Filesystem      Size  Used Avail Use% Mounted on
   /dev/sda1        50G   20G   28G  42% /

================ NETWORK CONFIGURATION =================
   2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
       link/ether 08:00:27:53:8b:dc brd ff:ff:ff:ff:ff:ff
       inet 192.168.1.10/24 brd 192.168.1.255 scope global dynamic enp0s3
          valid_lft 86396sec preferred_lft 86396sec

================ ACTIVE CONNECTIONS ====================
   Netid State      Recv-Q Send-Q Local Address:Port Peer Address:Port Process
   tcp   LISTEN     0      128    0.0.0.0:22        0.0.0.0:*     -

================ RUNNING SERVICES ======================
   UNIT                    LOAD   ACTIVE SUB     DESCRIPTION
   ssh.service             loaded active running OpenBSD Secure Shell server
   systemd-journald.service loaded active running Journal Service

================ RECENT LOGIN ATTEMPTS =================
   user    pts/0        192.168.1.5     Mon Mar  9 14:30   still logged in

================ LISTENING PORTS =======================
   Netid State      Recv-Q Send-Q Local Address:Port Peer Address:Port
   tcp   LISTEN     0      128    0.0.0.0:22        0.0.0.0:*

================ SYSTEM UPDATES STATUS =================
   Listing... Done
   systemd/bionic-updates 237-3ubuntu10.42 amd64 [upgradable from: 237-3ubuntu10.41]

================ MALICIOUS FILE SCAN ===================
   Scanning for malicious files... No malicious files found.

================ DIAGNOSIS COMPLETE =====================
```