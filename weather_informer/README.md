# Weather

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

Cli used to gather weather information. It is a basic wrapper around [wttr.in](http://wttr.in/)'s http interface.

```shell
user@computer:~$ python3 weather.py
Venice, Italy

      \   /     Sunny
       .-.      10 °C          
    ― (   ) ―   ↖ 0 km/h       
       `-’      10 km          
      /   \     0.0 mm         
```

Use the ```--help``` option to learn all the options available.

### Dependencies
* [Requests](https://requests.readthedocs.io/)
* [Click](https://click.palletsprojects.com/)
