dist_data = []

def part1():
	count_inc = 0
	for i in range(1, len(dist_data)):
		if (int(dist_data[i]) > int(dist_data[i - 1])):
			count_inc += 1
	return count_inc

def part2():
	count_inc = 0
	window_data = [] # Taking every three inputs and summing them in each element (0 is sum of 0, 1, 2; 1 is sum of 1, 2, 3; etc)
	for i in range(0, len(dist_data) - 2):
		window_data.append(dist_data[i] + dist_data[i + 1] + dist_data[i + 2])

	for i in range(1, len(window_data)):
		if (window_data[i] > window_data[i - 1]):
			count_inc += 1
	return count_inc

if __name__ == "__main__":
	with open("day1_input", "r") as file:
		dist_data = file.read().split("\n")

	for i in range(len(dist_data)):
		dist_data[i] = int(dist_data[i])

	print(part1())
	print(part2())

