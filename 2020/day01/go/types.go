// Borrowed from https://www.davidkaya.com/sets-in-golang/
// Borrowed from https://codetree.dev/golang-implementing-sets/

package advent

type IntSet map[int]struct{}

var exists = struct{}{}

func NewIntSet() IntSet {
	s := IntSet{}
	return s
}

func NewIntSet2(values []int) IntSet {
	s := NewIntSet()

	for _, value := range values {
		s.Add(value)
	}

	return s
}

func (s IntSet) Add(val int) {
	s[val] = exists
}

func (s IntSet) Remove(val int) {
	delete(s, val)
}

func (s IntSet) Has(val int) bool {
	_, ok := s[val]
	return ok
}
