import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('coverage_pynguin.txt', delimiter=',', unpack=True)
x2, y2 = np.loadtxt('coverage_h2.txt', delimiter=',', unpack=True)
x3, y3 = np.loadtxt('coverage_h3.txt', delimiter=',', unpack=True)

sum=0
for i in y:
    sum=sum+i
print(sum)
print(sum/225)


sum2=0
for i in y2:
    sum2=sum2+i
print(sum2)
print(sum2/225)

sum3=0
for i in y3:
    sum3=sum3+i
print(sum3)
print(sum3/225)


#lb1='Manual test'+(sum2/225)

plt.plot(x,y, label='Coverage.py = 97.00%')
plt.plot(x2,y2, label='Pytest --cov = 96.02%')
plt.plot(x3,y3, label='SonarPython = 96.68%')



plt.xlabel('Test')
plt.ylabel('Cobertura (porcentaje %)')
plt.title('Cobertura de codigo\nComparacion de Herramientas')
plt.legend()
plt.show()
