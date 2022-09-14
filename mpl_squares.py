#import tkinter as tk

from shutil import which
import matplotlib
import matplotlib.pyplot as plt

# tKinter backend
matplotlib.use('tkAgg')

# data
squares = [1,2,9,16,25]
input_values = [1, 2, 3, 4, 5] 
#x_values = [1, 2, 3, 4, 5]
x_values = range(1, 1001)
#y_values = [1, 4, 9, 16, 25]
y_values = [x**2 for x in x_values]


# Canvas
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots()


#ax.scatter(2,4,s=200)
#ax.scatter(x_values, y_values, c='red', s=1)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=1)
#ax.plot(input_values, squares, linewidth = 2)
#ax.plot(squares)
#ax.plot(squares, linewidth = 3)


ax.set_title("Square Numbers", fontsize = 24 )
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis='both', which='major', labelsize = 14)
ax.axis([0, 1100, 0, 1100000])

plt.show()
#plt.savefig("squares.png")
