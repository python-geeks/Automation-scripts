#!/usr/bin/python
from pathlib import Path
from zipfile import ZipFile

import click


def extract_zip(zip_file: ZipFile, password_file: Path):
    with open(password_file, 'r') as passwords:
        for password in passwords.readlines():
            try:
                zip_file.extractall(pwd=password.strip().encode())
                print(f"Found password: {password}")
                break
            except RuntimeError:
                pass
        else:
            print("Password not found")


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--zip', help='Set path to zip file')
@click.option(
    '--passwords',
    default=Path().cwd() / 'passwords.txt',
    help='Set path to file with passwords',
)
def main(zip, passwords):
    """Simple program that greets NAME for a total of COUNT times."""
    zip_file = ZipFile(zip)
    extract_zip(zip_file, passwords)


if __name__ == '__main__':
    main()
