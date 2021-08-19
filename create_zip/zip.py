import os
import zipfile
import argparse


def cli_parse():
    cli = argparse.ArgumentParser(prog='zip creator',
                                  description='Basic automation script for \
                                  creating zip file from a folder')
    cli.add_argument("folder", metavar='Folder',
                     type=str, help="Path to folder")
    cli.add_argument("-o", "--output", type=str, help="Output file path")
    return cli.parse_args()


args = cli_parse()
folder = args.folder
output = args.output


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        print(root, dirs, files, path)
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


# print(output)
if not output:
    output = os.path.basename(folder)

if not output.lower().endswith('.zip'):
    output += ".zip"

zipf = zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED)
zipdir(folder, zipf)
zipf.close()

print("File created", output)
