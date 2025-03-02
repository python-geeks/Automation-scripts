import os
import argparse
import sys
import datetime
import logging


class DesktopCleaner:

    def __init__(self):
        self._args = self.cli_parse()
        self._desktop_path = self.get_desktop_path()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='Log.log', filemode='w',
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self._files_paths = []

    @staticmethod
    def cli_parse():
        arg_parser = argparse.ArgumentParser(prog='Desktop cleanup',
                                             description='Automation script to clean up old desktop files')
        arg_parser.add_argument("--delete", type=int,
                                required=False,
                                help='Flag to delete the files')

        arg_parser.add_argument("--limit", type=int,
                                required=True,
                                help='No of days to check for')
        return arg_parser.parse_args()

    @staticmethod
    def get_desktop_path():
        _username_path = os.path.expanduser('~')

        if sys.platform == 'win32':
            _username_path += '\\Desktop'
        else:
            _username_path += '/Desktop/New folder'

        return _username_path

    def delete_files(self):
        self.logger.info("Deleting all the files \n")
        for file_path in self._files_paths:
            try:
                os.remove(file_path)
                self.logger.info(f"Deleted file {file_path} successfully\n")
            except FileNotFoundError:
                self.logger.error(f"{file_path} not found\n")
            except PermissionError:
                self.logger.error(f"User does not have permission to delete {file_path}\n")
            except Exception as e:
                self.logger.error(f"Error occurred - {e} for {file_path}\n")

    def scan_desktop(self):

        for dirpath, _, files in os.walk(self._desktop_path):
            self.logger.info("Walking through all files in desktop\n")
            for file in files:
                file_path = str(os.path.join(dirpath, file))
                file_details = os.stat(file_path)

                last_modified = datetime.datetime.fromtimestamp(file_details.st_mtime)
                curr_time = datetime.datetime.now()

                delta_days = curr_time - last_modified
                limit = self._args.limit

                if delta_days.days > limit:
                    self.logger.info(f"{file_path} is exceeding threshold - last modified {delta_days.days} ago\n")
                    self._files_paths.append(file_path)

        if self._args.delete and len(self._files_paths) > 0:
            self.delete_files()
        elif len(self._files_paths) > 0:
            self.logger.info("Delete option not selected - so only logging file names\n")
        else:
            self.logger.info("No files exceeding the limit\n")


if __name__ == '__main__':

    desktop_cleaner = DesktopCleaner()
    desktop_cleaner.scan_desktop()
