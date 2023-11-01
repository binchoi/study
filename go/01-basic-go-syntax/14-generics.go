package main

import (
	"fmt"
)

// Without generics, we would have to write a separate function for each type.

func main() {
	intArray := map[string]int64{"a": 1, "b": 2, "c": 3}
	floatArray := map[string]float64{"a": 1.1, "b": 2.2, "c": 3.3}

	fmt.Printf("Non-Generic Sums: %v and %v\n", SumInts(intArray), SumFloats(floatArray))
	fmt.Printf("Generic Sums: %v and %v\n", SumIntsOrFloats(intArray), SumIntsOrFloats(floatArray))
	fmt.Printf("Generic Sums (w/ Constraint): %v and %v\n",
		SumNumbers(intArray),
		SumNumbers(floatArray))
}

func SumInts(m map[string]int64) int64 {
	var s int64
	for _, v := range m {
		s += v
	}
	return s
}

func SumFloats(m map[string]float64) float64 {
	var s float64
	for _, v := range m {
		s += v
	}
	return s
}

// GENERICS

// SumIntsOrFloats illustrates how type parameters can be defined (enclosed in square brackets)
func SumIntsOrFloats[K comparable, V int64 | float64](m map[K]V) V {
	var s V
	for _, v := range m {
		s += v
	}
	return s
}

// Number is a type constraint
type Number interface {
	int64 | float64
}

func SumNumbers[K comparable, V Number](m map[K]V) V {
	var s V
	for _, v := range m {
		s += v
	}
	return s
}

// Extended example

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type FoldTreeInput interface {
	TreeNode | int64 | float64
}

type FoldTreeOutput interface {
	TreeNode | int64 | float64 | []string
}

func foldTree[A FoldTreeInput, B FoldTreeOutput](root *TreeNode, init A) B {

	return init
}
