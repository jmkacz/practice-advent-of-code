package part2

import "strconv"

func GetRating(lines []string, value int) string {
	var char byte
	for index := 0; index < len(lines[0]); index++ {
		n := len(lines)
		ones := 0
		for _, line := range lines {
			ones += int(line[index] - '0')
			if ones*2 >= n {
				char = byte('0' + rune(value))
			} else {
				char = byte('0' + rune(1-value))
			}
		}
		filtered := make([]string, 0)
		for _, line := range lines {
			if line[index] == char {
				filtered = append(filtered, line)
			}
		}
		lines = filtered
		if len(lines) == 1 {
			break
		}
	}
	if len(lines) != 1 {
		panic("did not find solution")
	}
	return lines[0]
}

func ComputeAnswer(lines []string) int {
	oxygen_generator_rating, err := strconv.ParseInt(GetRating(lines, 1), 2, 32)
	if err != nil {
		panic(err)
	}
	co2_scrubber_rating, err := strconv.ParseInt(GetRating(lines, 0), 2, 32)
	if err != nil {
		panic(err)
	}
	return int(oxygen_generator_rating) * int(co2_scrubber_rating)
}
