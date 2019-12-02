from numpy import loadtxt


def get_list():
	original_list = loadtxt('input.txt', delimiter=',', dtype=int).tolist()
	return original_list


# part 1
def part_1(noun=12, verb=2):
	input_list = get_list()
	input_list[1] = noun
	input_list[2] = verb
	index = 0

	while len(input_list) > index + 3:

		position0 = input_list[index]
		position1 = input_list[index + 1]
		position2 = input_list[index + 2]
		position3 = input_list[index + 3]

		if position0 == 1:
			value = input_list[position1] + input_list[position2]
			input_list[position3] = value

		if position0 == 2:
			value = input_list[position1] * input_list[position2]
			input_list[position3] = value

		index += 4
	return int(input_list[0])


part1_output = part_1()
print("Solution to part 1: ", part1_output)


def part_2(search):
	for noun in range(search):
		for verb in range(search):
			output = part_1(noun, verb)

			if output == 19690720:
				return 100 * noun + verb


# part 2
part2_output = part_2(100)
print("Solution to part 2: ", part2_output)
