import argparse
from getpass import getpass
import aes_tool


parser = argparse.ArgumentParser(description="Aes \
 encryption and decryption command")

parser.add_argument("--text", help=argparse.SUPPRESS)
parser.add_argument(
    "--operation",
    "-op",
    choices=["0", "1"],
    help="0 for encryption and 1 for decryption",
)
args = parser.parse_args()
password = getpass("Enter password : ")

if args.operation == "0":
    print(aes_tool.encrypt(args.text, password))

elif args.operation == "1":
    print(aes_tool.decrypt(args.text, password))
