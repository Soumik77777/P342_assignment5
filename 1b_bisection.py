import math
import csv
from library_week5 import *

f = lambda x: -x - math.cos (x)

a= float(input("Enter lower limit(a):"))
b= float(input("Enter upper limit(b):"))

if f(a) == 0:
    print("The exact solution is, x=", a)
elif f(b) == 0:
    print("The exact solution is, x=", b)
else:
    c, list_c = bisection(f, a, b)

    error = list_error(list_c)

    with open('1b_bisec_datafile.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Sl. No.", "value of c", "Abs_error"])
        for i in range(len(list_c)):
            writer.writerow([i + 1, list_c[i], error[i]])


'''
Enter lower limit(a):1.5
Enter upper limit(b):2.5
Modified lower limit= -0.875
Modified upper limit= 2.5
The solution of the equation is, x= -0.7390852272510529
'''