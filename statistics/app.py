import statistics

foo = [2, 4, 3, 6, 8, 99, 100]

# Arithmetic mean (“average”) of data.
mean = statistics.mean(foo)
print(mean)
# 31.714285714285715

# Harmonic mean of data.
harmonic_mean = statistics.harmonic_mean(foo)
print(harmonic_mean)

# Median (middle value) of data.
median = statistics.median(foo)
print(median)
#

# Low median of data.
median_low = statistics.median_low(foo)
print(median_low)
#

# High median of data.
median_high = statistics.median_high(foo)
print(median_high)
#

# Median, or 50th percentile, of grouped data.
median_grouped = statistics.median_grouped(foo)
print(median_grouped)
#

# Mode (most common value) of discrete data.
mode = statistics.mode(foo)
print(mode)
#

pstdev = statistics.pstdev(foo)
print(pstdev)
#

pvariance = statistics.pvariance(foo)
print(pvariance)
#

# Population standard deviation of data.
stdev = statistics.stdev(foo)
print(stdev)
#

variance = statistics.variance(foo)
print(variance)
#


variance = statistics.variance(foo)
print(variance)
# 2148.238095238095
