# FileCleanupService

**Purpose**  
A lightweight scheduler that periodically deletes files older than _N_ days from a target directory—ideal for log rotation, temp-folder pruning, and automated disk-space management.

---

## Features

- Deletes files older than configurable threshold  
- “Dry-run” mode for safe preview  
- Detailed logging (console & file)  
- Configurable via CLI flags or JSON/YAML config  
- Cross-platform: Windows service & Unix cron compatibility  

---

## 🛠️ Prerequisites

- Python ≥ 3.8  
- Dependencies: listed in `requirements.txt`  

---

## ⚙️ Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/TheoC99/FileCleanupService.git
   cd FileCleanupService
2. python cleanup_service.py --startup auto install
