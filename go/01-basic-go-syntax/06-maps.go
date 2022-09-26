package main

import (
	"fmt"
	"hash/fnv"
)

func hash(s string) uint32 {
	h := fnv.New32a()
	h.Write([]byte(s))
	return h.Sum32()
}

func basicMapUsage() {
	// declare map
	var myMap map[string]int
	// actually create a map
	myMap = make(map[string]int)

	// alternatively
	myMap2 := make(map[string]int)

	myMap["potato"] = 7
	myMap2["gold"] = 1

	fmt.Println(myMap["potato"])
	fmt.Println(myMap2["gold"])
}

func usingMapLiterals() {
	myMap := map[string]string{"a": "apple", "b": "book", "c": "cheese"}

	fmt.Println(myMap["a"])
	fmt.Println(myMap["b"])
	fmt.Println(myMap["c"])
}

func mapValuesHaveZeroValue() {
	// zero value for values is that of the value's data type
	// for int values -> 0
	var myMap map[string]int
	fmt.Println(myMap["I've not been assigned"])

	// for bool values -> false
	var myMap2 map[string]bool
	fmt.Println(myMap2["I've not been assigned"])

	// for string values -> ""
	var myMap3 map[string]string
	fmt.Println(myMap3["I've not been assigned"])
}

func mapHasZeroValue() {
	var myMap map[string]int

	fmt.Printf("%#v [%T] LEN: %v\n", myMap, myMap, len(myMap))

	if myMap == nil {
		fmt.Println("zero value of map is nil")
	}
}

func tellingZeroValuesApartFromRealZeros() {
	scores := map[string]int{} // could have used make()

	scores["alpha"] = 70
	// ok=true indicates that they key was found
	val, ok := scores["alpha"]
	fmt.Println(val, ok)

	val, ok = scores["beta"]
	fmt.Println(val, ok)
}

func usingMapsAsSets() {
	mySet := make(map[int]bool)
	mySet[5] = false
	mySet[9] = true
	// ok=true indicates that they key was found
	_, ok := mySet[6]
	fmt.Println(ok)

	_, ok = mySet[5]
	fmt.Println(ok)
}

func updatingMaps() {
	myMap := make(map[int]int)
	myMap[5] = 0

	if val, ok := myMap[5]; ok {
		fmt.Println(val)
	}

	// one way
	myMap[5] = 10
	if val, ok := myMap[5]; ok {
		fmt.Println(val)
	}

	// another way
	myMap[5]++
	if val, ok := myMap[5]; ok {
		fmt.Println(val)
	}
}

func deletingKeyValues() {
	myMap := make(map[int]int)
	myMap[5] = 0

	if _, ok := myMap[5]; ok {
		fmt.Println("it exists")
	}

	delete(myMap, 5)
	if _, ok := myMap[5]; !ok {
		fmt.Println("it doesn't exist anymore")
	}
}

func traverseKVsUsingForRangeLoops() {
	scores := map[string]int{}
	scores["alpha"] = 70
	scores["beta"] = 80
	scores["delta"] = 90
	scores["gamma"] = 100

	// ordering is not guaranteed
	for k, v := range scores {
		fmt.Printf("student %5s scored %3d\n", k, v)
	}
}

func main() {
	basicMapUsage()
	usingMapLiterals()
	mapValuesHaveZeroValue()
	mapHasZeroValue()
	tellingZeroValuesApartFromRealZeros()

	usingMapsAsSets()
	updatingMaps()
	deletingKeyValues()

	traverseKVsUsingForRangeLoops()
}
