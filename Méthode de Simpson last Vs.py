import numpy as np
import matplotlib.pyplot as plt

try:
    a = float(input("Enter the lower limit of integration \n"))
    b = float(input("Enter the upper limit of integration \n"))
    n = int(input("enter the number of points for your calculation \n"))
except ValueError:
    print('Please enter a valid value')

if n % 2 == 0:
    npair = n
else:
    npair = n+1

#Initialization of the function
pas = 0.000001
z = np.arange(a, b+pas, pas)
t= 1/(1+z**2)
integralereel=np.pi/4

#Initialization of the function with discretization
h = (b-a)/(npair)
x = np.arange(a, b+h, h)
y = 1/(1+x**2)

#calculation of the integral
sompair = 0
somimpair = 0
for i in range(1, npair):
    if i % 2 == 0:
        sompair += y[i]
    else:
        somimpair += y[i]

integrale = (h/3)*(y[0]+y[npair]+2*sompair+4*somimpair)

#calculation of the error
derive4 = (24*(5*(z**4)-10*(z**2)+1))/((1+z**2)**5)
positive =np.abs(derive4)
maximum =np.max(positive)
erreur=((b-a)*(h**4)*maximum)/180

#Plotting of the fourth derivative
plt.subplot(1,2,1)
plt.plot(z,derive4)
plt.title('fourth derivative')

#plotting of function
plt.subplot(1,2,2)
plt.plot(z, t)
plt.plot(x, y, "o")
plt.title('$1/(1+x^2)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

#simpson curve parabola
for i in range(0, npair-1, 2):
    xparabol = x[i:i+3]
    yparabol = y[i:i+3]
    xcontinu=np.arange(xparabol[0],xparabol[2]+pas,pas) #plotting of a continuous parabola
    coeff = np.polyfit(xparabol, yparabol, 2)
    parabol = coeff[0]*(xcontinu**2) + coeff[1]*xcontinu + coeff[2]
    plt.plot(xcontinu, parabol, "r")

plt.show()

print(f"the integral of this function from {a} to {b} is {integrale} \n The interpolation error is less than {erreur}")
print(f"The absolute error obtained is {integrale-integralereel}")