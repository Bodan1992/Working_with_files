import csv

with open('resources/username.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)