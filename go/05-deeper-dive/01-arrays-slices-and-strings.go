package main

import (
	"bytes"
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

func sliceIntro() {
	// A slice is a data structure describing a contiguous section of an array stored separately from
	// the slice variable itself. A slice is not an array. A slice describes a piece of an array.

	var buffer [256]byte
	var slice []byte = buffer[100:150]

	// type: []byte (read as, slice of byte)
	fmt.Printf("slice: %T\n", slice)

	// idiomatic way to initialize slice
	var sliceIdiomatic = buffer[100:150]
	sliceIdiomaticTwo := buffer[100:150]
	fmt.Printf("sliceIdiomatic: %T\n", sliceIdiomatic)
	fmt.Printf("sliceIdiomaticTwo: %T\n", sliceIdiomaticTwo)

	// For now, think of a slice as a little data structure with two elements: a length and a pointer
	// to an element of an array. For instance, it could be built like this behind the scenes:
	type sliceHeader struct {
		Length        int
		ZerothElement *byte
	}

	customSlice := sliceHeader{
		Length:        50,
		ZerothElement: &buffer[100],
	}
	fmt.Printf("customSlice: %T", customSlice)

	// we can slice a slice
	slice2 := slice[5:10]
	fmt.Printf("slice2: %T | %v\n", slice2, slice2)

	// We can also reslice, which is slicing a slice AND storing the result back in the
	// original slice structure.
	slice = slice[5:10]
	fmt.Printf("slice: %T | %v\n", slice, slice)
	// because slice2 points to the underlying array rather than slice, it is unaffected
	fmt.Printf("slice2: %T | %v\n", slice2, slice2)

	// You’ll often hear experienced Go programmers talk about the “slice header” because that
	// really is what’s stored in a slice variable. For instance, when you call the following,
	// the header is what gets passed to the function:
	slashPos := bytes.IndexRune(slice, '/')
	fmt.Printf("slashPos: %v\n", slashPos)

	// The slice argument that is passed to the IndexRune function is, in fact, a “slice header”.

	// There’s one more data item in the slice header which we will get to shortly.
}

func passingSlicesToFunc() {
	// It’s important to understand that even though a slice contains a pointer, it is itself
	// a value. Under the covers, it is a struct value holding a pointer and a length. It is
	// NOT a pointer to a struct.

	// Hence, when a slice is passed to a function, a COPY of the slice header is given.
	// The ramifications of this is important.
	
}

func main() {
	theFoundation()
	sliceIntro()
}
