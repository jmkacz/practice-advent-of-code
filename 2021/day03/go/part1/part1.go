package part1

func ComputeAnswer(lines []string) int {
	gamma_rate := 0
	epsilon_rate := 0

	n := len(lines)
	ones := make([]int, len(lines[0]))
	for _, line := range lines {
		for index, bit := range line {
			ones[index] += int(bit - '0')
		}
	}

	for _, value := range ones {
		gamma_rate = gamma_rate * 2
		epsilon_rate = epsilon_rate * 2
		if value*2 >= n {
			gamma_rate += 1
		} else {
			epsilon_rate += 1
		}
	}

	return gamma_rate * epsilon_rate
}
