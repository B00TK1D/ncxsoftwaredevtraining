def part1(dataIn):
	horiz_pos = 0
	depth = 0
	for data in dataIn:
		match data[0]:
			case "forward":
				horiz_pos += int(data[1])
			case "up":
				depth -= int(data[1])
			case "down":
				depth += int(data[1])
	print(horiz_pos * depth)
	return

def part2(dataIn):
	horiz_pos = 0
	depth = 0
	aim = 0
	for data in dataIn:
		match data[0]:
			case "forward":
				horiz_pos += int(data[1])
				depth += int(data[1]) * aim
			case "up":
				aim -= int(data[1])
			case "down":
				aim += int(data[1])
	print(horiz_pos * depth)
	return

if __name__ == "__main__":
	dataIn = [line for line in open("day2_input").read().splitlines()]
	for i in range(len(dataIn)): dataIn[i] = dataIn[i].split(" ")
	part1(dataIn)
	part2(dataIn)