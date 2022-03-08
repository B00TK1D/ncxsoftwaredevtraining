def part1(states):
	next_state = states.copy()
	for day in range(80):
		for i in range(1, 9):
			next_state[i - 1] = states[i]
		next_state[6] += states[0]
		next_state[8] = states[0]
		states = next_state.copy()
	return states

def part2(states):
	next_state = states.copy()
	for day in range(256):
		for i in range(1, 9):
			next_state[i - 1] = states[i]
		next_state[6] += states[0]
		next_state[8] = states[0]
		states = next_state.copy()
	return states

if (__name__ == "__main__"):
	total = 0
	lanternfish_pop = [int(fish) for fish in open("day6_input").read().split(",")]
	states = [lanternfish_pop.count(i) for i in range(9)]

	# states = part1(states)
	states = part2(states)
	for state in states:
		total += state
	print(total)