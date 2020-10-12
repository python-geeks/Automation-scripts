# filemover

This script was written with python 3.9

To use this script you will just need to run it and follow the on screen instructions in the console.

Basics of what will happen
- You will be asked "What directory would you like to move?". In which you will need to enter the FULL path to your desired folder.
- Next, you will be asked "Where would you like to transfer the contents?". Same as before, you will need to provide a full path to your desired folder, but if it does not exist the script will ask if you want it created.
- Once both directories are established, the code will run continuously (until exited) moving any files from the 1st folder to the 2nd provided. It will check every 30 seconds if there are any new files to move. Side Note: it will skip any folders it finds in the 1st folder provided.