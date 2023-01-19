package main

import "fmt"

// AppendToZeroCapacity instantiates a slice of length 0 and capacity 0 and repeatedly
// appends elements to the slice
func AppendToZeroCapacity(n int) []int {
	slice := make([]int, 0)
	for i := 0; i < n; i++ {
		slice = append(slice, i)
	}
	return slice
}

// AppendToNCapacity instantiates a slice of length 0 and capacity n and repeatedly
// appends elements to the slice
func AppendToNCapacity(n int) []int {
	slice := make([]int, 0, n)
	for i := 0; i < n; i++ {
		slice = append(slice, i)
	}
	return slice
}

// FillNLengthSlice instantiates a slice of length n and capacity n and assigns elements
// at index 0 through n-1
func FillNLengthSlice(n int) []int {
	slice := make([]int, n)
	for i := 0; i < n; i++ {
		slice[i] = i
	}
	return slice
}

func main() {
	fmt.Printf("appendToZeroCapacity: %v\n", AppendToZeroCapacity(100))
	fmt.Printf("appendToNCapacity: %v\n", AppendToNCapacity(100))
	fmt.Printf("fillNLengthSlice: %v\n", FillNLengthSlice(100))
}
