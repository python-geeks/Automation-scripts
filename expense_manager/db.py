import sqlite3
import datetime
now = datetime.datetime.utcnow()

CREATE_GROCERIES = "CREATE TABLE IF NOT EXISTS groceries (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_HOUSEHOLD = "CREATE TABLE IF NOT EXISTS household (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_ENTERTAINMENT = "CREATE TABLE IF NOT EXISTS entertainment (id INTEGER PRIMARY KEY,good TEXT, \
                                                                  price INTEGER, date DATE);"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"

INSERT_GROCERIES = "INSERT INTO groceries (good, price, date) VALUES(?,?,?);"
INSERT_HOUSEHOLD = "INSERT INTO household (good, price, date) VALUES(?,?,?);"
INSERT_ENTERTAINMENT = "INSERT INTO entertainment (good, price, date) VALUES(?,?,?);"
INSERT_OTHER = "INSERT INTO other (good, price, date) VALUES(?,?,?);"


SELECT_ALL1 = "SELECT * FROM groceries;"
SELECT_ALL2 = "SELECT * FROM household;"
SELECT_ALL3 = "SELECT * FROM entertainment;"
SELECT_ALL4 = "SELECT * FROM other;"

SELECT_GROCERIES = "SELECT * FROM groceries WHERE good = ? AND price = ?;"
SELECT_HOUSEHOLD = "SELECT * FROM household WHERE good = ? AND price = ?;"
SELECT_ENTERTAINMENT = "SELECT * FROM entertainment WHERE good = ? AND price = ?;"
SELECT_OTHER = "SELECT * FROM other WHERE good = ? AND price = ?;"

DELETE_GROCERIES = "DELETE FROM groceries WHERE good = ? AND price = ?;"
DELETE_HOUSEHOLD = "DELETE FROM household WHERE good = ? AND price = ?;"
DELETE_ENTERTAINMENT = "DELETE FROM entertainment WHERE good = ? AND price = ?;"
DELETE_OTHER = "DELETE FROM other WHERE good = ? AND price = ?;"

# create for every table


def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_OTHER)

# INSERT VALUES


def insert_groceries(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_GROCERIES, (good, price, date))
        conn.commit()


def insert_household(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_HOUSEHOLD, (good, price, date))
        conn.commit()
        c.close()


def insert_entertrainment(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_ENTERTAINMENT, (good, price, date))
        conn.commit()
        c.close()


def insert_other(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_OTHER, (good, price, date))
        conn.commit()
        c.close()

# SELECT_ALL


def select_all_groceries():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


def select_all_household():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL2)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


def select_all_entertrainment():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL3)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


def select_all_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

# SELECT SPECIFIC


def select_grocery(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_GROCERIES, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


def select_household(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_HOUSEHOLD, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


def select_entertainment(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ENTERTAINMENT, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


def select_other(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_OTHER, (good, price))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


# DELETE VALUE
def delete_grocery(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_GROCERIES, (good, price))
        conn.commit()
        c.close()


def delete_household(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_HOUSEHOLD, (good, price))
        conn.commit()
        c.close()


def delete_entertainment(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ENTERTAINMENT, (good, price))
        conn.commit()
        c.close()


def delete_other(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_OTHER, (good, price))
        conn.commit()
        c.close()
