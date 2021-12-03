package part1

import "sort"
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

func FindPair(values []int, target int) [2]int {
	result := [2]int{0, 0}
	seen := make(map[int]int)
	for _, value := range values {
		_, valueExists := seen[value]
		if valueExists {
			continue
		}

		seen[value] = 0

		complement := target - value
		_, complementExists := seen[complement]
		if complementExists {
			result[0] = value
			result[1] = complement
			sort.Ints(result[:])
			break
		}
	}
	return result
}

func ComputeAnswer(lines []string, target int) int {
	values := Parse(lines)
	results := FindPair(values, target)
	return results[0] * results[1]
}
