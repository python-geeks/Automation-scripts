import ast
import csv
import os
import sys
import re

# This will hold the table name as key, and columns as values.
mainDict = {}


def createStatement(line):
    return line.startswith('CREATE TABLE')


# To detect fields, aka column names
def fieldDef(line):
    return line.strip().startswith('`')


def insertStatement(line):
    return line.startswith('INSERT INTO')


def getCleanedValue(line):
    value = None
    result = re.search(r'\`([^\`]*)\`', line)
    if result:
        value = result.groups()[0]
        print(value)
    return value


def getValueTuple(line):
    values = line.partition(' VALUES ')[-1].strip().replace('NULL', "''")
    # To exclude the ;
    if values[-1] == ';':
        values = values[:-1]

    return ast.literal_eval(values)


def writeFile(outputDirectory, tableName, schema, values):
    # File name that the current table will be assigned to
    fileName = os.path.join(outputDirectory, '%s.csv' % (tableName,))
    with open(fileName, 'w') as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=schema)
        writer.writeheader()
        for value in values:
            writer.writerow(dict(zip(schema, value)))


def parseFile(fileName, outputDirectory):
    tableName = None

    with open(fileName, 'r') as readFile:
        for line in readFile:
            if createStatement(line):
                tableName = getCleanedValue(line)
                mainDict[tableName] = []
            elif tableName and fieldDef(line):
                fieldName = getCleanedValue(line)
                mainDict[tableName].append(fieldName)
            elif insertStatement(line):
                tableName = getCleanedValue(line)
                currentTable = mainDict[tableName]
                values = getValueTuple(line)
                writeFile(outputDirectory, tableName, currentTable, values)


if __name__ == '__main__':
    parseFile(sys.argv[1], sys.argv[2])
