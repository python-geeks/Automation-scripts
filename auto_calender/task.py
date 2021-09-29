

import datetime

class Task:
    total_time = 0
    date = datetime.datetime.now()

    def __init__(self, name, start_time, end_time, color):
        self.name=name
        self.start_time=start_time
        self.end_time=end_time
        self.color=color

    def get_time_of_task(self):
        self.total_time = self.end_time - self.start_time
    
    def make_int(self,time):
        arr = []
        for line in time:
            if line.strip(): 
                try:           # line contains eol character(s)
                    n = int(line) 
                    arr.append(n) 
                except Exception as e:
                    pass 
        hour_string = str(arr[0]) + str(arr[1])
        int_hour = int(hour_string)
        return int_hour