import os
import hashlib

# prints duplicate files from the list


def show_dup_files(dup_list):
    if len(dup_files) == 0:
        print('no duplicate files found')
        return # noqa 
    print('Duplicate files in the inputted directory : ')
    for file_name in dup_list:
        print(file_name)

# prints out everything inside a given folder


def show_all_files(dest_fold):
    for file_name in os.listdir(dest_fold):
        print(file_name)


# function return hash of file content


def get_digest(file_path):
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def get_file_hashes(file_size, size_dic, root_fold):
    files = list()
    files = [k for k, v in size_dic.items() if v == file_size]
    hash_files = list()
    hash_files = [get_digest(os.path.join(root_fold, name)) for name in files]

    return hash_files


if __name__ == "__main__":
    try:
        dest_folder = input('input the absolute path of a folder : ')
        track_file_size = dict()
        dup_files = list()
        files_list = os.listdir(dest_folder)
        for file_name in files_list:
            if os.path.isdir(os.path.join(dest_folder, file_name)):
                continue

            path = os.path.join(dest_folder, file_name)
            file_size = os.path.getsize(path)
            # searching in the dictionary

            if file_size in track_file_size.values():
                '''if it exists it may be a potential dup file
                to confirm it we will hash content of both and comapare'''# noqa           
                # now there can be more than one files with same size so have

                files_hashed_list = get_file_hashes(file_size, track_file_size, dest_folder)# noqa

                file_hash_2 = get_digest(os.path.join(dest_folder, file_name))

                if file_hash_2 in files_hashed_list:
                    dup_files.append(file_name)
            else:
                track_file_size[file_name] = file_size

    #    show_all_files(dest_folder)
        show_dup_files(dup_files)
    except Exception as err:
        print(err)   # noqa    