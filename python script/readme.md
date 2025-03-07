# Automated System Diagnostics Tool

A simple Python script that monitors system health, CPU/memory usage, disk space, and logs potential issues.

## Features
- ✅ **Cross-platform** (Windows & Linux)
- 📊 **Monitors CPU & Memory Usage**
- 💾 **Checks Disk Space Usage**
- 📝 **Logs system health with timestamps**
- 🔍 **Detects potential issues and suggests solutions**

## Prerequisites
This script requires Python and the `psutil` library.

### Install Dependencies
```bash
pip install psutil
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/system-diagnostics-tool.git
   cd system-diagnostics-tool
   ```

2. Run the script:
   ```bash
   python diagnosis-tool.py
   ```

3. View results in the console and check logs in `system_diagnostics.log`

## Example Output
```
🔹 Timestamp:
   2025-03-06 14:30:15.123456

🔹 System Info:
   OS: Windows
   OS Version: 10.0.19045
   Processor: Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz
   Uptime (seconds): 345600

🔹 CPU & Memory:
   CPU Usage (%): 12.3
   Memory Usage (%): 45.7

🔹 Disk Info:
   Total Disk (GB): 500
   Used Disk (GB): 250
   Free Disk (GB): 250
   Usage (%): 50.0
```

## Logging
- The script logs all system diagnostics in `system_diagnostics.log`
- Example log entry:
  ```json
  {
      "Timestamp": "2025-03-06 14:30:15.123456",
      "System Info": {"OS": "Windows", "Processor": "Intel Core i7"},
      "CPU & Memory": {"CPU Usage (%)": 85.0, "Memory Usage (%)": 90.2},
      "Disk Info": {"Usage (%)": 95.0}
  }
  ```

## Future Improvements
- 📩 **Email alerts for high CPU/memory usage**
- 📡 **Remote monitoring support**
- 📊 **Dashboard with real-time metrics**

## Contributing
Feel free to fork and submit pull requests!

## License
MIT License. See `LICENSE` file for details.

