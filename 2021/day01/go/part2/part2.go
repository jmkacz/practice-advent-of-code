package part2

import "strconv"

func Parse(lines []string) []int {
	var values []int
	for _, line := range lines {
		value, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}
		values = append(values, value)
	}
	return values
}

func ComputeAnswer(lines []string) int {
	result := 0
	depths := Parse(lines)
	for index := 3; index < len(depths); index++ {
		if depths[index] > depths[index-3] {
			result += 1
		}
	}
	return result
}
