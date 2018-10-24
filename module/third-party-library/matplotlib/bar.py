from matplotlib import pyplot as plt

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x2 = [1, 2, 9, 3]
y2 = [7, 5, 8, 2]

plt.grid(True, color='red')
plt.bar(x, y, color='#ffdd00', label='Line 1', align='center')  # 3 hexcolor don't work #fd0, #f00
plt.bar(x2, y2, label='Line 2', align='center')
plt.legend()
plt.title('Foo Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
