# **Hardware and System Information using Python** :snake:  :computer:

[![python 3](https://img.shields.io/badge/python-3.8-blue)](https://python.org)

 Sometimes while working you want to know about the CPU usgae of your computer or how many memory is your computer consuming and other various reasons where you need to know about your hardware and system. 

 **Python** has a awesome library [*psutil*](https://github.com/giampaolo/psutil) which displays information on processes and system like CPU, memory, disks, etc.
 

### Before you import psutil you need to install it:

  ```python 
 pip3 install psutil
 ```
 

### We also need to import additional modules for date and system information:

```python
import psutil
import platform
from datetime import datetime
```
