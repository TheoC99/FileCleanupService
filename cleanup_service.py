import os
import time
import shutil
import win32serviceutil
import win32service
import win32event

CONFIG_FILE = r"C:\FileCleanupConfig\config.txt"  # Path to config file

class FileCleanupService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FileCleanupService"
    _svc_display_name_ = "File Cleanup Service"
    _svc_description_ = "A service that deletes all files and folders from a specified directory every 24 hours."

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True
        self.folder_to_clean = self.get_folder_path()
        self.last_modified = os.path.getmtime(CONFIG_FILE) if os.path.exists(CONFIG_FILE) else 0

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.running = False

    def SvcDoRun(self):
        interval_seconds = 24 * 60 * 60  # 24 hours in seconds
        config_check_interval = 60  # Check for config updates every 60 seconds

        while self.running:
            # Check if config.txt has been updated
            if self.is_config_updated():
                self.folder_to_clean = self.get_folder_path()

            if self.folder_to_clean:
                self.delete_files_and_folders(self.folder_to_clean)

            # Sleep in shorter intervals to detect config changes
            for _ in range(interval_seconds // config_check_interval):
                if not self.running:
                    break
                time.sleep(config_check_interval)

    def is_config_updated(self):
        """ Check if config.txt has been modified since last check. """
        if os.path.exists(CONFIG_FILE):
            modified_time = os.path.getmtime(CONFIG_FILE)
            if modified_time > self.last_modified:
                self.last_modified = modified_time
                return True
        return False

    @staticmethod
    def get_folder_path():
        """ Reads the folder path from the config file. """
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                folder_path = f.readline().strip()
                if os.path.exists(folder_path):
                    return folder_path
        return None  # Return None if invalid or missing

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
