#%%
# collects data from JHU time_series_covid19_confirmed_US into a list
# list is 40 elements long representing the x-axis of Google Mobility graph from 02/16 to 03/26
import csv

covid_timed_data = 'time_series_covid19_confirmed_US.csv'
# list containing data from 03/30 (column 80) to 04/05 (column 86), aligned with the x axis of Google mobility graphs
covid_cases = [0] * 7 # 86-80, the number of days worth of data we are extracting
with open(covid_timed_data, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[6] == 'New Jersey':
            for i in range(79, 86):
                covid_cases[i - 79] += int(row[i])
print(covid_cases)

#%%
mobility_data = 'mobility_reports.csv'
# Google mobility reports currently contain two data points
# 03/29 and 04/05
mobility = [] # the number of Google mobility data points..
rowcount = -1
with open(mobility_data, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "United States" and row[1] == "New Jersey":
            rowcount += 1
            mobility.append(row[3:9])
mobility = [[int(float(percent)*100) for percent in date] for date in mobility]
print(mobility)

# %%
# ordering of mobility percentage values:
# Retail & Recreation, Grocery & Pharmacy, Parks, Transit Stations, Workplaces, Residential
#     30 31  1  2  3  4  5
day = [0,                6]
day2 = [i for i in range(7)]
pct = [mobility[0][0], mobility[1][0]]

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * b ** x

fig = plt.figure()
axl = fig.add_subplot(111)
slope, intercept, r_value, p_value, std_err = linregress(day, pct)
popt, pcov = curve_fit(func, day2, covid_cases)
X_plot = np.linspace(0, 6)
Y_plot = slope*X_plot+intercept
axl.plot(X_plot, Y_plot, color='r')
axl.scatter(day, pct, label='% mobility', color='r')
axr = axl.twinx()
axr.plot(day2, func(day2, *popt), color='b')
axr.scatter(day2, covid_cases, label='covid cases', color='b')
plt.title('Recreational Mobility in NJ')
plt.xlabel('Day')
axl.set_ylabel('Mobility Percentage', color='r')
axr.set_ylabel('COVID-19 Cases', color='b')
for tl in axr.get_yticklabels():
    tl.set_color('b')
#plt.legend()
plt.show()


# %%
