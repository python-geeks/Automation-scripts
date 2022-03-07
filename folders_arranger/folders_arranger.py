import shutil
import os
import string


class ArrangeScripts:
    def __init__(self, path_to_folder):
        self.folders = ['a_e', 'f_j', 'k_o', 'p_t', 'u_z']
        self.folder_mapping = {}
        for alphabet in list(string.ascii_lowercase):
            if alphabet in list('abcde'):
                self.folder_mapping[alphabet] = 'a_e'
            elif alphabet in list('fghij'):
                self.folder_mapping[alphabet] = 'f_j'
            elif alphabet in list('klmno'):
                self.folder_mapping[alphabet] = 'k_o'
            elif alphabet in list('pqrst'):
                self.folder_mapping[alphabet] = 'p_t'
            elif alphabet in list('uvwxyz'):
                self.folder_mapping[alphabet] = 'u_z'

        self.path_to_folder = path_to_folder

    def create_folders(self):
        for folder in self.folders:
            new_folder = os.path.join(self.path_to_folder, folder)
            if not os.path.isdir(new_folder):
                os.mkdir(new_folder)

    def organize_folder(self):
        self.create_folders()
        for a_folder in os.listdir(self.path_to_folder):
            if a_folder in self.folders:
                continue

            source_path = os.path.join(self.path_to_folder, a_folder)

            first_char = a_folder.lower()[0]
            destination_path = os.path.join(self.path_to_folder, self.folder_mapping[first_char])
            shutil.move(source_path, destination_path, copy_function=shutil.copytree)


def process_folders():
    # get folder path
    user_input = input('Enter path to folder which needs to be organized: ')
    arrange = ArrangeScripts(user_input)
    arrange.organize_folder()


if __name__ == "__main__":
    try:
        process_folders()
    except Exception as e:
        print(e.__class__, "occurred.")
