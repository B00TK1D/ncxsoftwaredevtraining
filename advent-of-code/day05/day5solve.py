raw_data = []
start_coords = []
end_coords = []
vent_grid = []
SIZE = 1000

def set_straight_vent(alongX, sel, start, end):
	global vent_grid
	if (start > end):
		tmp = start
		start = end
		end = tmp

	if (alongX):
		for y in range(start, end + 1):
			vent_grid[y][sel] += 1
	else:
		for x in range(start, end + 1):
			vent_grid[sel][x] += 1
	return

def set_diagonal_vent(start, end):
	global vent_grid
	if (start[0] > end[0]):
		tmp = start
		start = end
		end = tmp

	if (start[1] < end[1]):
		for shift in range(end[0] - start[0] + 1):
			vent_grid[start[1] + shift][start[0] + shift] += 1
	else:
		for shift in range(end[0] - start[0] + 1):
			vent_grid[start[1] - shift][start[0] + shift] += 1
	return

def check_interects():
	intersects = 0
	for row in vent_grid:
		for cell in row:
			if (cell >= 2):
				intersects += 1
	return intersects

def part1():
	for i in range(len(start_coords)):
		if (start_coords[i][0] == end_coords[i][0]):
			set_straight_vent(True, start_coords[i][0], start_coords[i][1], end_coords[i][1])
		elif (start_coords[i][1] == end_coords[i][1]):
			set_straight_vent(False, start_coords[i][1], start_coords[i][0], end_coords[i][0])
		else:
			print("*** Failed coord check ***")
			print("i    : " + str(i))
			print("start: " + str(start_coords[i][0]) + " " + str(start_coords[i][1]))
			print("end  : " + str(end_coords[i][0]) + " " + str(end_coords[i][1]) + "\n")
	return

def part2():
	for i in range(len(start_coords)):
		if (start_coords[i][0] == end_coords[i][0]):
			set_straight_vent(True, start_coords[i][0], start_coords[i][1], end_coords[i][1])
		elif (start_coords[i][1] == end_coords[i][1]):
			set_straight_vent(False, start_coords[i][1], start_coords[i][0], end_coords[i][0])
		else:
			set_diagonal_vent(start_coords[i], end_coords[i])
	return

if __name__ == "__main__":
	with open("day5_input", "r") as file:
		raw_data = file.read().splitlines()
	
	for i in range(len(raw_data)):
		tmp = raw_data[i].split(" -> ")
		start_coords.append(tmp[0].split(","))
		end_coords.append(tmp[1].split(","))

	start_coords = [[int(j) for j in i] for i in start_coords]
	end_coords = [[int(j) for j in i] for i in end_coords]

	for y in range(SIZE):
		vent_grid.append([])
		for x in range(SIZE):
			vent_grid[y].append(0)

	# part1()
	part2()
	print(check_interects())