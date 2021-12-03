package advent

import "reflect"
import "sort"
import "testing"

func TestNewIntSet(t *testing.T) {
	s := NewIntSet()
	actual := len(s)
	expected := 0
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestAdd(t *testing.T) {
	s := NewIntSet()
	s.Add(1)
	actual := len(s)
	expected := 1
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestAddDuplicate(t *testing.T) {
	s := NewIntSet()
	s.Add(1)
	s.Add(1)
	actual := len(s)
	expected := 1
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestRemove(t *testing.T) {
	s := NewIntSet()
	s.Add(1)
	s.Remove(1)
	actual := len(s)
	expected := 0
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestRemoveNonExistant(t *testing.T) {
	s := NewIntSet()
	s.Add(1)
	s.Remove(2)
	actual := len(s)
	expected := 1
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestHas(t *testing.T) {
	s := NewIntSet()
	s.Add(1)
	actual := s.Has(1)
	expected := true
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestHasNonExistant(t *testing.T) {
	s := NewIntSet()
	s.Add(1)
	actual := s.Has(2)
	expected := false
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestRange(t *testing.T) {
	s := NewIntSet()
	s.Add(1)
	s.Add(2)
	var actual []int
	for val, _ := range s {
		actual = append(actual, val)
	}
	sort.Ints(actual)
	expected := []int{1, 2}
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}
}

func TestNewIntSet2WithSlice(t *testing.T) {
	s := NewIntSet2([]int{1, 1, 2, 2, 3, 3})
	actual := len(s)
	expected := 3
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}

}

func TestNewIntSet2WithArray(t *testing.T) {
	i := [6]int{1, 1, 2, 2, 3, 3}
	s := NewIntSet2(i[:])
	actual := len(s)
	expected := 3
	if actual != expected {
		t.Errorf("Test failed, expected: '%#v', got: '%#v'", expected, actual)
	}

}
