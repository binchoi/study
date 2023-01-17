package main

import (
	"fmt"
)

// The concept of an array is one of the most common features of procedural programming languages.
// Despite its seemingly simple logic, there are many questions that must be answered when adding
// them to a language. For instance,
// 1. fixed-size or variable-size?
// 2. is the size part of the type?
// 3. what do multidimensional arrays look like?
// 4. does the empty array have meaning?

// The answers to these questions shape the role of arrays in the design of the language.

// For Go, the keystone that fits everything together is the concept of slices. Slices, which built
// on fixed-size arrays, gives a flexible, extensible data structure.

// New Go programmers stumble over the way slices work. Let's clear up the confusion today by
// Investigating arrays, slices, strings, and the mechanics of 'append'

// ARRAYS
func theFoundation() {
	//`Arrays are not often seen in Go programs because the size of an array is part of its type,
	// which limits its expressive power.

	// to declare...
	var buffer [256]byte
	// the type of buffer includes its size
	fmt.Printf("buffer: %T\n", buffer)
	buffer[0] = 123

	// Hence, bigBugger has a distinct type
	var bigBuffer [512]byte
	fmt.Printf("bigBuffer: %T\n", bigBuffer)

	// len returns the number of elements of an array, slice, and some other data types
	fmt.Printf("len of buffer: %v | len of bigBuffer: %v\n", len(buffer), len(bigBuffer))

	// Arrays have their place—they are a good representation of a transformation matrix for
	// instance—but their most common purpose in Go is to hold storage for a slice.
}

func main() {
	theFoundation()
}
