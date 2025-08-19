# network-scanner
# usage
pip install -r requirements.txt
clone the repository with git clone https://github.com/fixit-py/network-scanner.git

change into the directory with cd MAC-CHANGER2.0

give the file permission to run as an executable with chmod +x network_scanner.py

run python network_scanner.py -r or --range  "full ip range with CIDR notation" while using python2

run python3 network_scanner.py -r or --range  "full ip range with CIDR notation" while using python3

replace the "full ip range with CIDR notation" with the name of your ip range
# ABOUT
This python program scans your local network for all devices connected to the network compatible with both python 2 and python 3 specify the interface name using the -r or --range from the bash terminal or cmd. this script works on both linux, MAC and windows as long as all the required external libaries are downloaded and imported 
# module
scapy , optparse(argparse)
