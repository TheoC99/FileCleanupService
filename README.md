# FileCleanupService

dependencies:
> pip install pywin32


This is a simple python script which deletes files in a specific folder every 24 hours

----- Configuration steps -------

#1) Go to WinKey > Virus & Threat protection > Scroll to Exlusions > Add or remove exlusions > Add an exlusion > Folder > C:\ScriptPath

2) bash cmd admin at script location
> python cleanup_service.py --startup auto install

--startup auto: Configures the service to start automatically at boot.

3) Start the service:
> python cleanup_service.py start

----Manage the Service ------
> python cleanup_service.py stop
> python cleanup_service.py remove
