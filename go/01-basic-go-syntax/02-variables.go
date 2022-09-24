package main

import "fmt"

func playingWithTypes() {
	w := "string-variable"
	x := 1
	y := true
	z := 3.14

	fmt.Printf("w = %v [%T]\n", w, w)
	fmt.Printf("x = %v [%T]\n", x, x)
	fmt.Printf("y = %v [%T]\n", y, y)
	fmt.Printf("z = %v [%T]\n", z, z)
}

func assigningVariables() {
	// 1. declare, then assign
	var w string
	w = "string-variable"

	// 2. declare and assign simultaneously [type inferred]
	x := 1

	fmt.Printf("w = %v [%T]\n", w, w)
	fmt.Printf("x = %v [%T]\n", x, x)
}

func playingWithConstants() {
	const x string = "I'm an unchangeable constant"
	fmt.Printf("x = %v [%T]\n", x, x)

	// uncomment line below to see compile error
	// x = "Some other string"
}

func runesAreCharacters() {
	runes := []rune("Hello World")
	fmt.Printf("raw rune array: %v", runes)

	for i := 0; i < len(runes); i++ {
		fmt.Printf("%vth rune: %v | char format: %c\n", i, runes[i], runes[i])
	}

	for i, r := range runes {
		fmt.Printf("%vth rune: %v | char format: %c\n", i, r, r)
	}
}

func main() {
	playingWithTypes()
	assigningVariables()
	playingWithConstants()
	runesAreCharacters()
}
