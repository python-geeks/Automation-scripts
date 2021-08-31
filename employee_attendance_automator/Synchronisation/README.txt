Make sure to have template.xlsx where localserver is hosted(whichever directory).
Make sure to have Emp.xlsx for device1, Emp2.xlsx for device2.These get overwritten every time.
Also month files like(2021-01-01,201-01-16,2021-02-01,2021-02-16.........) will get overwritten on client side.
Finally Synced(merged) files with same month name will over write the existing month file in /images/excel/month.xlsx file on both devices.
Synchronisation is thus maintained.
This synchronisation program is scheduled to run everyday a 11:00 and 17:00 also local server is sccheduled to run at same time , 
i have also maintained sync such that there will be no conflict in sending or revcieving files.
localserver should be always runing, but the recieving turns on at schedules times.
after sending both files from client the merging starts. else it will not.
So use this olny when you are using two or more devices.
