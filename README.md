This is a simple python script which deletes files periodically every 24 hours.

Install required Python packages with:
```
pip install -r requirements.txt
```

------ Installing ------

Method 1)

Bash cmd admin at script location:
````
python cleanup_service.py --startup auto install
````

Method 2) 
- Run install_service.bat as administrator
- When Promted enter the target temporary folder and hit enter
- Script creates `C:\FileCleanupConfig\config.txt`
- config.txt get read every 5 minutes.
- If any changes have been made, the target folder changes.
  
---- Managing the Service ------

````
 python cleanup_service.py start
````
````
 python cleanup_service.py stop
````
````
 python cleanup_service.py remove
````

---- Kill the Service Process ----
1) Open Command Prompt as Administrator.
2) Find the service's Process ID (PID) by running:
````
sc queryex FileCleanupService
````
Look for the PID in the output, like this:
````
SERVICE_NAME: FileCleanupService
STATE              : 3  STOP_PENDING
PID               : 1234  <---- This is the process ID
````
3) Kill the process using:
````
taskkill /F /PID 1234
````
(Replace 1234 with the actual PID from Step 2.)

4) Verify the service is now stopped:
````
sc query FileCleanupService
````
---- Delete the Service -----

5) Once the service is fully stopped, remove it with:
````
sc delete FileCleanupService
````
Then restart your computer to finalize the removal.
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

## Prerequisites

- Python ≥ 3.8  
- Dependencies: listed in `requirements.txt`  

---

##  Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/TheoC99/FileCleanupService.git
   cd FileCleanupService

2. By default create a folder called "TempStorage" in either C:/ or D:/ drive.
3. python cleanup_service.py --startup auto install
    ```bash
    python cleanup_service.py --startup auto install
4. Restart Computer
