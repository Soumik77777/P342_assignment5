import math
import csv
from library_week5 import *

f = lambda x: math.log (x) - math.sin (x)

x= input("Input initial guess:")

ans, list_x= NewtonRaphson(f, float(x), 10**(-10), 10**(-6))

error = list_error(list_x)

with open('1a_nr_datafile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Sl. No.", "value of x", "Abs_error"])
    for i in range(len(list_x)):
        writer.writerow([i+1, list_x[i], error[i]])

print("The solution of the equation is, x=", ans)



'''
Input initial guess:1.5
The solution of the equation is, x= 2.219107148913746
'''
