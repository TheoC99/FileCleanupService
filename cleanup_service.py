import os
import time
import shutil
import win32serviceutil
import win32service
import win32event

# Determine which temp directory to clean. If D:\\TempStorage exists it will be
# used, otherwise the fallback path C:\\TempStorage is used.
TEMP_DIR = (
    r"D:\\TempStorage" if os.path.exists(r"D:\\TempStorage") else r"C:\\TempStorage"
)

class FileCleanupService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FileCleanupService"
    _svc_display_name_ = "File Cleanup Service"
    _svc_description_ = "A service that deletes all files and folders from a specified directory every 24 hours."

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.running = False

    def SvcDoRun(self):
        """Main service loop that cleans TEMP_DIR every 24 hours."""
        interval_seconds = 24 * 60 * 60  # 24 hours in seconds
        sleep_interval = 60  # Sleep in 60 second increments to allow fast stop

        while self.running:
            self.delete_files_and_folders(TEMP_DIR)

            for _ in range(interval_seconds // sleep_interval):
                if not self.running:
                    break
                time.sleep(sleep_interval)


    @staticmethod
    def delete_files_and_folders(folder_path):
        """ Deletes all files and subfolders inside the specified folder. """
        try:
            if not os.path.exists(folder_path):
                return

            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)

                try:
                    if os.path.isfile(item_path):
                        os.remove(item_path)  # Delete file
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)  # Delete folder and all its contents
                except Exception:
                    pass  # Suppress errors during deletion

        except Exception:
            pass  # Suppress exceptions during folder access


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(FileCleanupService)
