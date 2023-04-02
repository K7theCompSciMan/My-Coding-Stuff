import csv
with open("CSVDemo.csv", 'r') as file:
    csvreader = csv.reader(file)


    for row in csvreader:
        print(row)