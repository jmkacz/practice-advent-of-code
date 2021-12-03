package part2

import "advent"
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

func FindTriple(values []int, target int) [3]int {
	distinct_values := advent.NewIntSet2(values)
	result := [3]int{0, 0, 0}

	for firstValue, _ := range distinct_values {
		for secondValue, _ := range distinct_values {
			if firstValue == secondValue {
				continue
			}
			thirdValue := target - firstValue - secondValue
			if (thirdValue != firstValue) && (thirdValue != secondValue) && (distinct_values.Has(thirdValue)) {
				result[0] = firstValue
				result[1] = secondValue
				result[2] = thirdValue
				sort.Ints(result[:])
				return result
			}
		}
	}
	return result
}

func ComputeAnswer(lines []string, target int) int {
	values := Parse(lines)
	results := FindTriple(values, target)
	return results[0] * results[1] * results[2]
}
