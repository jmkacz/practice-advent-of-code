package part2

import "bufio"
import "log"
import "os"
import "testing"

func TestComputeAnswerSample(t *testing.T) {
	lines := []string{}
	actual := ComputeAnswer(lines)
	expected := 0
	if actual != expected {
		t.Errorf("Test failed, expected: '%d', got: '%d'", expected, actual)
	}
}

func getLines(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func TestComputeAnswerFull(t *testing.T) {
	lines := getLines("../../data/input.dat")
	actual := ComputeAnswer(lines)
	expected := 0
	if actual != expected {
		t.Errorf("Test failed, expected: '%d', got: '%d'", expected, actual)
	}
}
