package main

import "fmt"

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

func main() {
	w := "string-variable"
	x := 10
	y := true
	z := 3.14

	fmt.Printf("w = %v [%T] | %q | %s | %#v \n", w, w, w, w, w)
	fmt.Printf("x = %v [%T] | %d | %o | %O | %b | %x | %#v\n", x, x, x, x, x, x, x, x)
	fmt.Printf("y = %v [%T] | %#v\n", y, y, y)
	fmt.Printf("z = %v [%T] | %f | %e | %g | %#v\n", z, z, z, z, z, z)
}
