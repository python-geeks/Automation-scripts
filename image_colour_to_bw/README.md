# Script to convert coloured images to black and white

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## How to use:
1. Make the directory structure as shown below:
<br>.
<br>├── colour_to_bw.py
<br>└── image.png

2. Call the function giving two arguments, the path to the original image and the path for your output image
<br> example :-
<br>```colour_to_bw("./image.png","./")```

3. The output of the script will be stored as "final_image.png". The directory structure would look similar to this if you execute the code in step 2.
<br>.
<br>├── colour_to_bw.py
<br>├── final_image.png
<br>└── ptr_mail.apng
