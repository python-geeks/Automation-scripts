import os
import sys
import hashlib
import pandas as pd


# get list of all files in a dir
def file_list(folder):
    path = os.path.abspath(folder)
    files = [entry.path for entry in os.scandir(path) if entry.is_file()]
    print(f'[+] Found {len(files)} files in {folder}. ')

    return files


# Calculate the hash for any given file
def get_hash(filename):
    block_size = 65536

    with open(filename, 'rb') as f:
        m = hashlib.sha256()
        block = f.read(block_size)
        while len(block) > 0:
            m.update(block)
            block = f.read(block_size)
        digest = m.hexdigest()

    return digest

# create hashtable


def hashtable(files):
    if not isinstance(files, list):
        files = [files]
    else:
        pass

    hash_identifier = []
    for f in files:
        try:
            hash_identifier.extend([get_hash(f)])
        except OSError:
            hash_identifier.extend(['Hash could not be generated.'])

    return hash_identifier


# crawl through a directory and return the hashes of each file as a pd
# dataframe.
def create_hashtable(folder):
    files = file_list(folder)

    df = pd.DataFrame(columns=['file', 'hash'])
    df['file'] = files
    df['hash'] = hashtable(files)
    print('[+] Generated all hashes.')

    return df


# get duplicates
def list_duplicates(folder):
    duplicates_files = create_hashtable(folder)
    duplicates_files = duplicates_files[duplicates_files['hash'].duplicated(
        keep=False)]
    duplicates_files.sort_values(by='hash', inplace=True)
    duplicates_files = duplicates_files.drop_duplicates(
        subset='hash', keep='first')
    print(f'[+] Found {len(duplicates_files)} duplicates.\n')
    print(duplicates_files)

    return duplicates_files


# list_duplicates('C:/Users/ramij/Desktop/secret')

if __name__ == '__main__':
    folder = str(input('Folder full path (eg: C:/Users/bob/Desktop): '))
    if not os.path.exists(folder):
        print('Folder does not exist.')
        sys.exit(1)
    else:
        pass

    duplicates = list_duplicates(folder)
    delete = input('\n[!] Do you want to delete the duplicates (y/n):')
    print('\n')
    if delete.lower() == 'y':
        duplicates = duplicates['file'].tolist()
        for f in duplicates:
            os.remove(f)
            print(f'Deleted {f}')
    else:
        print('[X] Exiting...')
