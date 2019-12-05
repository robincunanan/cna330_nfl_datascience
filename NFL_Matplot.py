import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='First line!')

plt.xlabel('Years')
plt.ylabel('Percentage')
plt.title('NFL Extra-Point Accuracy \nstart year- end year')
plt.legend()
plt.show()
