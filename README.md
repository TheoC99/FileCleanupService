This service deletes every file and subfolder from a fixed temporary directory
once every 24 hours.  The folder is chosen automatically: if
`D:\TempStorage` exists it will be cleaned, otherwise `C:\TempStorage` is used.

------ Installing ------

Installation (run from an elevated command prompt):
````
python cleanup_service.py --startup auto install
````
  
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

