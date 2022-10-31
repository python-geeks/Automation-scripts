import tarfile
import os


def list_tar(archive, verbosity):
    """List a TAR archive with the tarfile Python module."""
    try:
        with tarfile.open(archive) as tfile:
            tfile.list(verbose=verbosity > 1)
    except Exception as err:
        msg = "error listing %s: %s" % (archive, err)
        print(msg)
    return None


test_tar = list_tar


def extract_tar(archive, outdir):
    """Extract a TAR archive with the tarfile Python module."""
    try:
        with tarfile.open(archive) as tfile:
            tfile.extractall(path=outdir)
    except Exception as err:
        msg = "error extracting %s: %s" % (archive, err)
        print(msg)
    return None


def create_tar(archive, folder_name, compression=None):
    """Create a TAR archive with the tarfile Python module."""
    mode = "w:"
    if compression is not None:
        mode = get_tar_mode(compression)
    try:
        with tarfile.open(archive, mode) as tfile:
            for filename in os.listdir(folder_name):
                tfile.add(folder_name + filename, arcname=filename)
    except Exception as err:
        msg = "error creating %s: %s" % (archive, err)
        print(msg)
    return None


def get_tar_mode(compression):
    """Determine tarfile open mode according to the given compression."""
    if compression == 'gzip':
        return 'w:gz'
    if compression == 'bzip2':
        return 'w:bz2'
    if compression == 'lzma':
        return 'w:xz'
    if compression:
        msg = 'pytarfile does not support %s for tar compression'
        print(msg)
    # no compression
    return 'w'
