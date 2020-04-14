#%%
# collects data from JHU time_series_covid19_confirmed_US into a list
# list is 40 elements long representing the x-axis of Google Mobility graph from 02/16 to 03/26
import csv

covid_timed_data = 'time_series_covid19_confirmed_US.csv'
# list containing data from 02/16 (column 36) to 04/05 (column 84), aligned with the x axis of Google mobility graphs
covid_cases = [0] * 49 # 84 - 36, the number of days worth of data we are extracting
with open(covid_timed_data, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[6] == 'New Jersey':
            for i in range(36, 85):
                covid_cases[i - 36] += int(row[i])
print(covid_cases)

#%%
mobility_data = 'mobility_reports.csv'
# Google mobility reports currently contain two data points
# 03/29 and 04/05
mobility_data = [[]] * 2 # the number of Google mobility data points..
rowcount = 0
with open(mobility_data, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "United States" and row[1] == "New Jersey":
            for i in range(5):
                mobility_data[rowcount].append(row[i + 3])