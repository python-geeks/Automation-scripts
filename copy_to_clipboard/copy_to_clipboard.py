import os
import sys
import platform
import subprocess

# Seeing if the file exists
if os.path.exists(sys.argv[1]):
    f = open(sys.argv[1], "r")
    f_contents = f.read()
    f.close()
else:
    print("Usage: copy2clip <file_name>")
    exit(1)

whatos = platform.system()

if whatos == "Darwin":
    subprocess.run("pbcopy", universal_newlines=True, input=f_contents)
    print("success: copied to clipboard")
elif whatos == "Windows":
    subprocess.run("clip", universal_newlines=True, input=f_contents)
    print("success: copied to clipboard")
else:
    print("failed: clipboard not supported")
