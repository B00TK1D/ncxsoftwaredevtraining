from math import ceil, floor

def median(arr):
	return arr[len(arr) // 2]

def mean(arr):
	return sum(arr) / len(arr)

def part1(crab_pos):
	total = 0
	mid = median(crab_pos)
	for pos in crab_pos:
		total += abs(pos - mid)
	print(total)

def part2(crab_pos):
	total = [0, 0]
	mean_rtn = mean(crab_pos)
	mid = [floor(mean_rtn), ceil(mean_rtn)]
	for pos in crab_pos:
		for i in range(2):
			if pos == mid[i]: continue
			dist = abs(pos - mid[i])
			total[i] += ((dist ** 2) + dist) // 2
	print(min(total))

if __name__ == "__main__":
	crab_pos = sorted([int(var) for var in open("day7_input").read().split(",")])
	part1(crab_pos)
	part2(crab_pos)