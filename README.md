This is a simple python script which deletes files periodically every 24 hours.

------ Installing ------

Method 1)

1. Open an **Administrator** command prompt in the repository folder.
2. Install the service:
````
python cleanup_service.py --startup auto install
````
3. Create `C:\FileCleanupConfig\config.txt` and write the full path of the
   folder you want cleaned into the file.  If the directory does not exist,
   create it first.
4. The service checks this file every minute and picks up any changes
   automatically.

Method 2)
- Run `install_service.bat` as **Administrator**.
- When prompted, enter the folder you want cleaned and press **Enter**.
- The batch file generates a temporary Python script using that folder path,
  packages it with PyInstaller and installs the resulting executable as a
  service.
- No configuration file is used for this method. To change the folder later,
  rerun the batch file with a new path.
  
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

