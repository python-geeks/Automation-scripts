# Expense Tracker

## Setting up the database 
- You need to first install the binaries for SQLite database from [here](https://www.sqlite.org/download.html) according to your respective operating system
- To be able to visualize the database properly, download SQLite Studio from [here](https://sqlitestudio.pl/)
- Create a new database and name it 'data.db'
- Run the following command which will automatically define the schema of the database
```
$ python db.py
```

## Running the GUI
- Since Tkinter package is already shipped with Python, no need of extra requirements, if not use the following command :
```
$ pip install tkinter
```
- Finally, run the following command to get going :
```
$ python app.py
```