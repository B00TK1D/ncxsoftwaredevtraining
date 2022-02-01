from itertools import count
from math import dist


dist_data = 0
count_inc = 0
with open("day1_input", "r") as file:
	dist_data = file.read().split("\n")

for i in range(1, len(dist_data)):
	if (int(dist_data[i]) > int(dist_data[i - 1])):
		count_inc += 1
print(count_inc)