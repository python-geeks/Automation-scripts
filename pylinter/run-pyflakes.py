import sys
import subprocess

from .utils import collect_sources


def ignore(p):
    """ Ignore hidden and test files """
    parts = p.splitall()
    if any(x.startswith(".") for x in parts):
        return True
    if 'test' in parts:
        return True
    return False


def run_pyflakes():
    cmd = ["pyflakes"]
    cmd.extend(collect_sources(ignore_func=ignore))
    return subprocess.call(cmd)


if __name__ == "__main__":
    rc = run_pyflakes()
    sys.exit(rc)
