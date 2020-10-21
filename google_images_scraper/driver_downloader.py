import os


def driver_download():
    commands = [
        "wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz",
        "tar xzf geckodriver-v0.25.0-linux64.tar.gz",
        "sudo mv geckodriver /usr/bin/geckodriver",
        "rm geckodriver-v0.25.0-linux64.tar.gz",
    ]
    for command in commands:
        os.system(command)


if __name__ == "__main__":
    driver_download()
