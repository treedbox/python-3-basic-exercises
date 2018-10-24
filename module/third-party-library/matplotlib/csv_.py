from matplotlib import pyplot as plt
import numpy as np
from os.path import abspath, join, dirname

file1 = 'file.csv'
file2 = 'file2.csv'
dir = abspath(dirname(__file__))
absFilePathFile1 = abspath(join(dirname(__file__), file1))
absFilePathFile2 = abspath(join(dirname(__file__), file2))

x, y = np.loadtxt(absFilePathFile1, unpack=True, delimiter=',')
x2, y2 = np.loadtxt(absFilePathFile2, unpack=True, delimiter='*')  # any delimiter
plt.grid(True, color='red')
plt.bar(x, y, color='#ffdd00', label='Line 1', align='center')  # 3 hexcolor don't work #fd0, #f00
plt.bar(x2, y2, label='Line 2', align='center')
plt.legend()
plt.title('Foo Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
