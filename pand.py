import csv

header = ['Name', 'Phone']
data = ['David', +2347014465861]

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    writer.writerow(data)

