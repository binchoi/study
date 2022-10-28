package main

import "fmt"

// Go defined types most often use structs as their underlying types, but they can also be based on
// ints, strings, booleans, or any other type

// Here is an example of an appropriate use case

type Liters float64

func (g Gallons) ToLiters() Liters {
	return Liters(g * 3.785)
}

type Gallons float64

func main() {
	var CarFuel Liters
	var TruckFuel Gallons
	CarFuel = Liters(40.0)
	TruckFuel = Gallons(20.0)

	fmt.Println(CarFuel, TruckFuel)
	// cannot assign Gallons to CarFuel and Liters to TruckFuel

	CarFuel = 10.0 // however, this is possible!
	fmt.Println(CarFuel, TruckFuel)

	l := Gallons(40.0).ToLiters()
	fmt.Println("40 Gallons converted to Liters:", l)

	// A defined type supports all the same operations as its underlying type.
	fmt.Println(Gallons(1) == Gallons(1))
	// fmt.Println(Gallons(1)==Liters(1)) // notice the error
	fmt.Println(Liters(7) * Liters(8))
	fmt.Println(Liters(7) < Liters(8))

}
