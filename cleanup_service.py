import os
import time
import win32serviceutil
import win32service
import win32event

class FileCleanupService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FileCleanupService"
    _svc_display_name_ = "File Cleanup Service"
    _svc_description_ = "A service that deletes files from a specific folder every 24 hours."

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.running = False

    def SvcDoRun(self):
        folder_to_clean = r"D:\TempStorage"  # Replace with your folder path
        interval_seconds = 24 * 60 * 60  # 24 hours in seconds

        while self.running:
            self.delete_files_in_folder(folder_to_clean)
            time.sleep(interval_seconds)

    @staticmethod
    def delete_files_in_folder(folder_path):
        """
        Deletes all files in the specified folder.
        """
        try:
            if not os.path.exists(folder_path):
                return

            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            for file in files:
                try:
                    os.remove(os.path.join(folder_path, file))
                except Exception:
                    pass  # Suppress exceptions during file deletion
        except Exception:
            pass  # Suppress exceptions during folder access


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(FileCleanupService)
