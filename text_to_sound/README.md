# Converting Text to Speech By Python 

This script involves implementation of Google text to speech API which is deployed on Deep Learning Algorithm Wavenet . The API is used for a better usability and simple architecture of the script , so that everyone can use it . It involves playsound (for audio files) . The steps how to use the script as well the visuals are shown below : 

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## Install Dependencies manually: 

```
python run requirements.txt (will install all dependienies in your local operating system)
```
There will be some command issues regarding Anaconda usgae it is cited below : 
```
If using anaconda , then follow the steps : 
Step 1 : Open Anaconda Power Shell 
Step 2 : pip install gTTS
Step 3 : pip install playsound
```
If you want to use Anaconda as a virtual environment then : 
```
1.) Step 1 : Open Anaconda Cmd prompt 
2.) Step 2 : conda create --name pip_env
3.) Step 3 : conda activate pip_env
4.) Step 4 : conda install pip
5.) Step 5 : Now you can use above commands
```
Visuals of the code bases and the interface is there in the Assets folder , 
Simply Run the script and the interface will open , and start converting your text to speech.
