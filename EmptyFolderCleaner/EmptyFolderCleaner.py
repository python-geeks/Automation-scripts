import os


def get_subdirectories(path):
    """
    Return a list containing the absolute path of the direct subdirectories in the provided path. Doesn't walk the
    directory tree.
    :param path: the path to check
    :return: a list with the direct subdirectories names
    """
    return [os.path.join(path, o) for o in os.listdir(path)
            if os.path.isdir(os.path.join(path, o))]


def clean_empty_folders(path, removeRoot=True, verbose=False):
    """
    Recursively remove empty folders and subdirectories.
    :param path: the initial (root) path
    :param removeRoot: if True (default), also removes the root path if all subdirectories are empty
    :param verbose: if True, prints progress
    :return: True if 'path' was removed, false otherwise. Note that, if removeRoot=False, this function will always
    return False
    """
    if not os.path.isdir(path):
        if verbose:
            print(path, "is not a directory. Abort.")
        return False

    subdirectories = get_subdirectories(path)
    for subdirectory in subdirectories:
        clean_empty_folders(subdirectory, removeRoot=True, verbose=verbose)

    # After removing subdirectories, check if folder is empty
    if not os.listdir(path) and removeRoot:
        os.rmdir(path)
        if verbose:
            print(path, "removed")
        return True

    return False


if __name__ == '__main__':
    selected_path = input("Write the desired path: ")
    remove_root = None
    while remove_root is None:
        remove_root_input = input("Also remove root folder (Y/N)? ").lower()
        if remove_root_input == "y":
            remove_root = True
            break
        elif remove_root_input == "n":
            remove_root = False
            break
        print(f"Invalid input '{remove_root_input}', please try again.")
    clean_empty_folders(selected_path, removeRoot=remove_root, verbose=True)
    print("Done!")
