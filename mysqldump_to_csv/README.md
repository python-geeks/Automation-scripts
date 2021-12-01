### Purpose ###
This tool is really helpful to convert mysqldump files to csv, so these dump files are easily readable.

### How does it work ###
You pass in a mysqldump file and a target directory where the csv will be stored in. Then a file will be created for each table and the corrolated values. An example is provided, to mysampledatabase.sql is the dump file and borders.csv is the produced csv file.

### How to use ###
To used this script all you need is the python script, a mysqldump file, and a directory where you would want the csv files saved in. The following command is to show how to run the script:
            'python mysql_dump_to_csv.py mysqlsampledatabase.sql output_directory'

Add you directory in the place of "output_directory"

### Author ###
Abdulaziz alharqan


### References ###
mysqldump file: http://smiffy.de/mondial/mysql-mondial.dmp