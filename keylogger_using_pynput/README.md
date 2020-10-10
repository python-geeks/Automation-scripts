# Keylogger using pynput module
A python script that records every keystroke made by a computer user and saves it in a text file with timestamp of the key being pressed.

If you want to run the program in background without creating a console window., save the file with the extension .pyw. 
Example : _keylogger.pyw_

## Modules Used

- pynput
- logging

We need to install the pynput module. To install the module type the following into the terminal:
```bash
pip install pynput
```

Recommended: Install the module after creating a virtual environment.

## Execution
- To run the program, type the following command into your terminal 

```bash
python keylogger.py
```

- OR
```bash
python keylogger.pyw
```

The keystrokes are now being logged into the logs.txt file.
To stop recording the keystrokes terminate the program.