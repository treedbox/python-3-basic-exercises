from matplotlib import pyplot as plt

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x2 = [1, 2, 9, 3]
y2 = [7, 5, 8, 2]

plt.grid(True, color='#FF0000')
plt.style.use('dark_background')
plt.plot(x, y, '#FFDD00', linewidth=5, label='Line 1')  # 3 hexcolor don't work #fd0, #f00
plt.plot(x2, y2, label='Line 2')
plt.legend()
plt.title('Foo Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

print(plt.style.available)
"""
['seaborn-notebook', 'seaborn-dark-palette', 'ggplot', 'fast', 'bmh',
'seaborn-muted', 'grayscale', 'dark_background', 'seaborn-pastel',
'seaborn-dark', 'seaborn-paper', '_classic_test', 'seaborn-deep',
'fivethirtyeight', 'Solarize_Light2', 'seaborn-talk', 'seaborn-bright',
'seaborn-poster', 'seaborn-colorblind', 'seaborn-darkgrid', 'classic',
'seaborn', 'seaborn-white', 'tableau-colorblind10', 'seaborn-whitegrid',
'seaborn-ticks']
"""
