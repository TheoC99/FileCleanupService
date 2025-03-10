This is a simple python script which deletes files periodically every 24 hours.

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

