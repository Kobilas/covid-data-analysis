# used to separate United States data from other countries
import csv

dailyreport = '04-08-2020.csv'
dailyreport_us = '04-08-2020_US.csv'

with open(dailyreport_us, 'w+', newline='') as wf, \
     open(dailyreport, 'r') as f:
    reader = csv.reader(f)
    writer = csv.writer(wf)
    writer.writerow(next(reader))
    for row in reader:
        if row[3] == 'US':
            writer.writerow(row)