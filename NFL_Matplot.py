import matplotlib.pyplot as plt # Modules needed
import csv

# Creates empty list
seahawks_y = []
sf_y = []
rams_y = []
cardinals_y = []
years_x = []

def SF():
    line_count = 0
    with open('49ers_Data.csv','r') as SF: # Open CSV file
        plots = csv.reader(SF, delimiter=',') # Reads csv
        for row in plots: # Reads each line
            if line_count == 0: # Skips the first row
                line_count+= 1
            else:
                line_count+= 1
                years_x.append(int(row[1])) # Adds data from years column to years_x
                sf_y.append(int(row[0])) # Adds data from PAT column to sf_y

def ram():
    line_count = 0
    with open('Rams_Data.csv','r') as ram:
        plots = csv.reader(ram, delimiter=',')
        for row in plots:
            if line_count == 0:
                line_count+= 1
            else:
                line_count+= 1
                rams_y.append(int(row[0]))

def seahawks():
    line_count = 0
    with open('Seahawks_Data.csv','r') as seahawks:
        plots = csv.reader(seahawks, delimiter=',')
        for row in plots:
            if line_count == 0:
                line_count+= 1
            else:
                line_count+= 1
                seahawks_y.append(int(row[0]))

def cardinals():
    line_count = 0
    with open('Cardinals_Data.csv','r') as cardinals:
        plots = csv.reader(cardinals, delimiter=',')
        for row in plots:
            if line_count == 0:
                line_count+= 1
            else:
                line_count+= 1
                cardinals_y.append(int(row[0]))

# Call out the functions
SF()
ram()
seahawks()
cardinals()

# Plot out data from lists
plt.plot(years_x,sf_y, label='49ers')
plt.plot(years_x,rams_y, label='Rams')
plt.plot(years_x,seahawks_y, label='Seahawks')
plt.plot(years_x,cardinals_y, label='Cardinals')

# Design graph
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.title('NFL Extra-Point Kick Accuracy')
plt.legend()
plt.show()

