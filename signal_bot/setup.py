from setuptools import setup
from signalbot.metadata import version, author, authoremail

setup(
    name='SignalBot',
    version=version,
    description='Interactive bot for the Signal messenger platform',
    packages=['signalbot'],
    author=author,
    author_email=authoremail,
    license='MIT',
    install_requires=['pytest', 'pytest-html', 'pytest-cov', 'pytest-dotenv', 'docker', 'haikunator', 'emoji', 'urllib3']
)