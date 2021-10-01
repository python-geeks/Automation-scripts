# Browser Notification Sender

This python program will send sends browser notifications to other linked devices from your device using .

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following dependencies.

```bash
pip install notify2
pip install notify-run
pip install tkinter
```
Now we have to register a channel for it.
To create simply type 

```bash
notify-run register
```
in your CLI , you will be getting something like below.

<img width="616" alt="68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6e6f746966792d72756e2f6e6f746966792e72756e2f6d61737465722f70795f636c69656e742f73637265656e73686f74732f72656769737465722e706e67" src="https://user-images.githubusercontent.com/60290431/130251692-be8f8567-43f2-4792-bc17-01b82100827f.png">

Now open the link which you got in any device you want to link and click "Subscribe on this device" (see below). that's it!
![12](https://user-images.githubusercontent.com/60290431/130252214-b80581a6-2782-4daa-a143-9c0633648385.png)


For more info go to https://pypi.org/project/notify-run/

## Usage
Now to use this application simply execute  "main.py",
a GUI will open where you can type your message and this message will be prompt as a browser notification to all linked devices.

![Annotation 2021-08-20 202439](https://user-images.githubusercontent.com/60290431/130252428-dabdf8f5-dcfa-4fc1-9aa2-1cd96d04cf17.jpg)


## License
[MIT](https://choosealicense.com/licenses/mit/)
