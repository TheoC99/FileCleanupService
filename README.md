dependencies:
> pip install pywin32


This is a simple python script which deletes files in a specific folder every 24 hours

To configure:
1) bash cmd admin at script location
> python cleanup_service.py --startup auto install

--startup auto: Configures the service to start automatically at boot.

2) Start the service:
python cleanup_service.py start

----Manage the Service ------
> python cleanup_service.py stop
> python cleanup_service.py remove


Update:
Make sure it also deletes folders and its containing files

To Delete:
cmd bash:
> sc delete FileCleanupService
Verify Deletion run bash:
>sc query FileCleanupService
