package main

import (
	"fmt"
)

func usePrintln() {
	fmt.Println("basic printing")

	// Println can take multiple args
	fmt.Println("some string", "more string", 1/4, "some boolean:", true)

	// if you don't want sep=" "
	fmt.Print("a", "b", 1/4, "c", true, "\n")
	fmt.Println("a" + "b" + "c")
}

//d - decimal integer
//o - octal integer
//O - octal integer with 0o prefix
//b - binary integer
//x - hexadecimal integer lowercase
//X - hexadecimal integer uppercase
//f - decimal floating point, lowercase
//F - decimal floating point, uppercase
//e - scientific notation (mantissa/exponent), lowercase
//E - scientific notation (mantissa/exponent), uppercase
//g - the shortest representation of %e or %f
//G - the shortest representation of %E or %F
//c - a character represented by the corresponding Unicode code point
//q - a quoted character
//U - Unicode escape sequence
//t - the word true or false
//s - a string
//v - default format
//T - a Go-syntax representation of the type of the value
//p - pointer address
//% - a double %% prints a single %
//#v - Go-syntax representation of the value

func formatVariousTypes() {
	w := "string-variable"
	x := 10
	y := true
	z := 3.14

	// % marks the start of a formatting verb
	fmt.Printf("w = %v [%T] | %q | %s | %#v \n", w, w, w, w, w)
	fmt.Printf("x = %v [%T] | %d | %o | %O | %b | %x | %#v\n", x, x, x, x, x, x, x, x)
	fmt.Printf("y = %v [%T] | %#v\n", y, y, y)
	fmt.Printf("z = %v [%T] | %f | %e | %g | %#v\n", z, z, z, z, z, z)
}

func usePrintf() {
	// specifying decimal precision level
	fmt.Printf("1/3 equals %0.2f\n", 1.0/3.0)
	// specifying minimum width of strings
	fmt.Printf("formatting str | %6s\n", "hello")
	// specifying minimum width of int
	fmt.Printf("formatting int | %6d\n", 1)
	fmt.Printf("formatting int | %6d\n", 21)
	fmt.Printf("formatting int | %6d\n", 212431)
	fmt.Printf("formatting int | %6d\n", 2131)
	fmt.Printf("formatting int | %6d\n", 2133)
	fmt.Printf("formatting int | %6d\n", 21)
}

func useSprintf() {
	var strArr [8]string
	// specifying decimal precision level
	strArr[0] = fmt.Sprintf("1/3 equals %0.2f\n", 1.0/3.0)
	// specifying minimum width of strings
	strArr[1] = fmt.Sprintf("formatting str | %6s\n", "hello")
	// specifying minimum width of int
	strArr[2] = fmt.Sprintf("formatting int | %6d\n", 1)
	strArr[3] = fmt.Sprintf("formatting int | %6d\n", 21)
	strArr[4] = fmt.Sprintf("formatting int | %6d\n", 212431)
	strArr[5] = fmt.Sprintf("formatting int | %6d\n", 2131)
	strArr[6] = fmt.Sprintf("formatting int | %6d\n", 2133)
	strArr[7] = fmt.Sprintf("formatting int | %6d\n", 21)

	for _, strVar := range strArr {
		fmt.Print(strVar)
	}
}

func main() {
	usePrintln()
	formatVariousTypes()
	usePrintf()
	useSprintf()
}
