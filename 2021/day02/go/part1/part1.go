package part1

import "fmt"
import "strconv"
import "strings"

type Position struct {
	hpos  int
	depth int
}

func ParseLine(line string) (string, int) {
	parts := strings.Split(line, " ")
	dir := parts[0]
	amt, err := strconv.Atoi(parts[1])
	if err != nil {
		panic(err)
	}
	return dir, amt
}

func ComputeAnswer(lines []string) int {
	pos := Position{0, 0}
	for _, line := range lines {
		dir, amt := ParseLine(line)
		switch dir {
		case "forward":
			pos.hpos += amt
		case "down":
			pos.depth += amt
		case "up":
			pos.depth -= amt
		default:
			panic(fmt.Sprintf("Unknown direction: %s", dir))
		}
	}

	if pos.depth < 0 {
		panic(fmt.Sprintf("Invalid depth: %d", pos.depth))
	}

	return pos.hpos * pos.depth
}
