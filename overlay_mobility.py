#%%
# collects data from JHU time_series_covid19_confirmed_US into a list
# list is 40 elements long representing the x-axis of Google Mobility graph from 02/16 to 03/26
import csv

covid_timed_data = 'time_series_covid19_confirmed_US.csv'
# list containing data from 02/16 (column 36) to 03/26 (column 75), aligned with the x axis of Google mobility graphs
covid_cases = [0] * 40 # 75 - 36, the number of days worth of data we are extracting
with open(covid_timed_data, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[6] == 'New Jersey':
            for i in range(36, 76):
                covid_cases[i - 36] += int(row[i])
#%%
# overlays Google mobility graph with regression line and scatterplot of covid cases from JHU
# serves to help visualize the flattening of the curve as more people social distance over time
import matplotlib.pyplot as plt

img = plt.imread('mobility_nj_recreation.png')
imgplot = plt.imshow(img, origin='upper', extent=[0, 10000, 10000, 0])
plt.scatter(range(0, 40000, 1000), covid_cases)
plt.show()

#ax.plot(range(41), covid_cases, '-', linewidth=2, color='firebrick')