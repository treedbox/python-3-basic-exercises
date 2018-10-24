# list two-dimensional
# list inside the list
foo = [[5, 6], [6, 7], [7, 2], [8, 4]]
print(foo)
# [[5, 6], [6, 7], [7, 2], [8, 4]]


# list multi-dimensional
# list inside the list inside the list
bar = [[5, 6], [6, 7], [7, [2, 6]], [[8, 5], 4]]


print(bar)
# [[5, 6], [6, 7], [7, [2, 6]], [[8, 5], 4]]

print(bar[0])
# [5, 6]

print(bar[0][1])
# 6

print(bar[3][0][0])
# 8
