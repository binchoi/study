package main

import (
	"bytes"
	"fmt"
)

func sliceIntro() {
	// A slice is a data structure describing a contiguous section of an array stored separately from
	// the slice variable itself. A slice is not an array. A slice describes a piece of an array.

	// note: A byte in Go is simply an unsigned 8-bit integer. That means it has a limit of (0 – 255)
	//       in numerical range. In Go, a byte can represent a character from a string as well.
	var buffer [256]byte // zero value of byte = 0
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

	// There’s one more data item in the slice header which we will discuss shortly.
}

func passingSlicesToFunc() {
	// While a slice contains a pointer, it is itself a value.
	// Under the covers, it is a struct value holding a pointer and a length.
	// It is NOT a pointer to a struct.

	// Hence, when a slice is passed to a function, a COPY of the slice header is given.
	// The ramifications of this is important.
	var buffer [256]byte
	slice := buffer[10:20]
	for i := 0; i < len(slice); i++ {
		slice[i] = byte(i)
	}
	fmt.Println("before", slice) // [0 1 2 3 4 5 6 7 8 9]
	AddOneToEachElement(slice)
	fmt.Println("after", slice) // [1 2 3 4 5 6 7 8 9 10]

	// Even though the slice header is passed by value, the header includes a pointer to elements
	// of an array, so both the original slice header and the copy of the header passed to the
	// function describe the same array.
	fmt.Println("original array", buffer)
}

func AddOneToEachElement(slice []byte) {
	for i := range slice {
		slice[i]++
	}
}

func passingSlicesToFuncTwo() {
	// The argument to the function really is a copy, as this example shows
	slice := make([]byte, 256)
	fmt.Println("Before: len(slice) =", len(slice)) // 256
	newSlice := SubtractOneFromLength(slice)
	fmt.Println("After: len(slice) =", len(slice)) // 256
	// The function is passed a copy of the slice header, not the original.
	fmt.Println("After: len(newSlice) =", len(newSlice)) // 255 b/c slice header specifies length=255
}

func SubtractOneFromLength(slice []byte) []byte {
	slice = slice[:len(slice)-1]
	return slice
}

// Another way to have a function modify the slice header is to pass a POINTER to the slice.

func passingSlicesToFuncThree() {
	slice := make([]byte, 256)
	fmt.Println("Before: len(slice) =", len(slice)) // 256
	PtrSubtractOneFromLength(&slice)
	fmt.Println("After:  len(slice) =", len(slice)) // 255
}

func PtrSubtractOneFromLength(slicePtr *[]byte) {
	slice := *slicePtr
	*slicePtr = slice[0 : len(slice)-1]
}

// NOTE: It is idiomatic to use a pointer receiver for a method that modifies a slice.
// see example in a-slice-pointer-receiver.go

func main() {
	sliceIntro()
	fmt.Println("********* passingSlicesToFunc *********")
	passingSlicesToFunc()
	fmt.Println("********* passingSlicesToFuncTwo *********")
	passingSlicesToFuncTwo()
	fmt.Println("********* passingSlicesToFuncThree *********")
	passingSlicesToFuncThree()

}
