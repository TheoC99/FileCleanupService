@echo off
REM Display an example folder path to the user
echo Example folder path: C:\Temp\MyFolder
echo.
REM Prompt user for the folder path
set /p folder_path="Enter the folder path to clean (e.g., C:\Temp\MyFolder): "

REM Create a temporary Python script with the user-defined folder path
echo import os > temp_script.py
echo folder_to_clean = "%folder_path%" >> temp_script.py
echo import time >> temp_script.py
echo import win32serviceutil >> temp_script.py
echo import win32service >> temp_script.py
echo import win32event >> temp_script.py
echo class FileCleanupService(win32serviceutil.ServiceFramework): >> temp_script.py
echo     _svc_name_ = "FileCleanupService" >> temp_script.py
echo     _svc_display_name_ = "File Cleanup Service" >> temp_script.py
echo     _svc_description_ = "A service that deletes files from a specified folder every 24 hours." >> temp_script.py
echo     def __init__(self, args): >> temp_script.py
echo         super().__init__(args) >> temp_script.py
echo         self.stop_event = win32event.CreateEvent(None, 0, 0, None) >> temp_script.py
echo         self.running = True >> temp_script.py
echo     def SvcStop(self): >> temp_script.py
echo         self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) >> temp_script.py
echo         win32event.SetEvent(self.stop_event) >> temp_script.py
echo         self.running = False >> temp_script.py
echo     def SvcDoRun(self): >> temp_script.py
echo         folder_to_clean = "%folder_path%" >> temp_script.py
echo         interval_seconds = 24 * 60 * 60  >> temp_script.py
echo         while self.running: >> temp_script.py
echo             self.delete_files_in_folder(folder_to_clean) >> temp_script.py
echo             time.sleep(interval_seconds) >> temp_script.py
echo     @staticmethod >> temp_script.py
echo     def delete_files_in_folder(folder_path): >> temp_script.py
echo         try: >> temp_script.py
echo             if not os.path.exists(folder_path): >> temp_script.py
echo                 return >> temp_script.py
echo             files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))] >> temp_script.py
echo             for file in files: >> temp_script.py
echo                 try: >> temp_script.py
echo                     os.remove(os.path.join(folder_path, file)) >> temp_script.py
echo                 except Exception: >> temp_script.py
echo                     pass  >> temp_script.py
echo         except Exception: >> temp_script.py
echo             pass >> temp_script.py
echo if __name__ == "__main__": >> temp_script.py
echo     win32serviceutil.HandleCommandLine(FileCleanupService) >> temp_script.py

REM Run PyInstaller to generate the executable
echo Creating the executable using PyInstaller...
pyinstaller --onefile --noconsole temp_script.py

REM Install the service
echo Installing the service...
python dist\temp_script.exe install --startup auto

REM Start the service
echo Starting the service...
python dist\temp_script.exe start

REM Clean up the temporary script
del temp_script.py

echo Service installed and started successfully!
pause
