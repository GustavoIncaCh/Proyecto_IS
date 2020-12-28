import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('coverage_test.txt', delimiter=',', unpack=True)
x2, y2 = np.loadtxt('coverage_pynguin.txt', delimiter=',', unpack=True)
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

#lb1='Manual test'+(sum2/225)

plt.plot(x,y, label='Manual test = 89.74%')
plt.plot(x2,y2, label='Automatic Pynguin = 97.00%')



plt.xlabel('Test')
plt.ylabel('Cobertura (porcentaje %)')
plt.title('Cobertura de codigo\nAutomatizada vs Manual')
plt.legend()
plt.show()
