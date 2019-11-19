import csv

with open('uscities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print('\"' + row[1] + ", " + row[2] + '\",')
