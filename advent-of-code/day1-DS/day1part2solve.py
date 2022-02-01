from itertools import count
from math import dist


dist_data = []
window_data = [] # Taking every three inputs and summing them in each element (0 is sum of 0, 1, 2; 1 is sum of 1, 2, 3; etc)
count_inc = 0
with open("day1_input", "r") as file:
	dist_data = file.read().split("\n")

for i in range(len(dist_data)):
	dist_data[i] = int(dist_data[i])

for i in range(0, len(dist_data) - 2):
	window_data.append(dist_data[i] + dist_data[i + 1] + dist_data[i + 2])

for i in range(1, len(window_data)):
	if (window_data[i] > window_data[i - 1]):
		count_inc += 1
print(count_inc)