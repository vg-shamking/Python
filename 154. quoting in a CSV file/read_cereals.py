import csv

csv_filename = 'cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # all digits remain float type
    for row in reader:
        print(row)
