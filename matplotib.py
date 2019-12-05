# This script will create a graph using the matplotlib module
# Robin Cunanan, rtcunanan@student.rtc.edu
# CNA 337 Fall 2019
# Sources: https://data.oecd.org/price/housing-prices.htm

import matplotlib.pyplot as plt

year_x = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
aus_y = [67.0, 69.6, 72.4, 80.9, 79.1, 78.9, 84.1, 91.7, 100.0, 105.5, 114.3, 112.7]
plt.plot(year_x, aus_y, label='Australia')

usa_y = [84.3, 86.4, 87.4, 87.2, 88.7, 91.0, 93.6, 96.5, 100.0, 103.8, 107.7, 111.6]
plt.plot(year_x, usa_y, label='United States')

plt.xlabel('Year')
plt.ylabel('Cost in thousands (USD)')
plt.title(' House Prices by Year')
plt.legend()

plt.show()
