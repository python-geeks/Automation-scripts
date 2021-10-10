### A simple implementation of a CLI tool to work with caeser ciphers. The default implementation is ROT-13, but can be adjusted for any offset. Works on files and string arguments passed via CLI.
***
PS E:\Ceaser Cipher> py .\CeaserCipher.py -help
usage: CeaserCipher.py [-h] [-d] [-o OFFSET] (-f FILE | -s STRING)
CeaserCipher.py: error: argument -h/--help: ignored explicit argument 'elp'

PS E:\Ceaser Cipher> py .\CeaserCipher.py -s "hello st0rm"
uryyb fg0ez

PS E:\Ceaser Cipher> py .\CeaserCipher.py -d  -s "uryyb fg0ez"  
hello st0rm
