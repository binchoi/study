package main

import "fmt"

func basicStructVariable() {
	var house struct {
		numOfWindows     int
		numOfDoors       int
		colorOfRoof      string
		isLocatedInKorea bool
	}

	fmt.Printf("This is an example of a struct variable: %#v\n", house)

	house.numOfWindows = 3
	house.numOfDoors = 4
	house.colorOfRoof = "red"
	house.isLocatedInKorea = true

	fmt.Printf("This is an example of a struct variable: %#v\n", house)
	fmt.Printf("The number of windows: %d\n", house.numOfWindows)
}

func exploringTypes() {
	// Type definitions allow you to create types of your own.
	// They let you create a new defined type that’s based on an underlying type

	type house struct {
		numOfWindows     int
		numOfDoors       int
		colorOfRoof      string
		isLocatedInKorea bool
	}

	type car struct {
		name     string
		topSpeed float64
	}

	var myFriendsHouse house
	myFriendsHouse.numOfDoors = 5
	myFriendsHouse.numOfWindows = 2
	myFriendsHouse.colorOfRoof = "yellow"
	myFriendsHouse.isLocatedInKorea = false

	fmt.Printf("My friend's house: %#v\n", myFriendsHouse)

	var porsche car
	porsche.name = "Porsche 911"
	porsche.topSpeed = 323

	fmt.Printf("Check out my ride: %#v\n", porsche)
}

type saleItem struct {
	name          string
	percentOff    float64
	originalPrice float64
}

func reduceOriginalPrice(item saleItem) {
	item.originalPrice = item.originalPrice * 0.9
}

func tryingToModifyStructUsingAFunction() {
	var item saleItem
	item.originalPrice = 100
	fmt.Println(item)

	reduceOriginalPrice(item)

	fmt.Println(item)
	// No Change!

	// Go is a “pass-by-value” language.
	// This means that function parameters receive a copy of the arguments the function was called with.
}

func reduceOriginalPricePointer(item *saleItem) {
	item.originalPrice = item.originalPrice * 0.9
}

func actuallyModifyStructUsingAFunction() {
	var item saleItem
	item.originalPrice = 100
	fmt.Println(item)

	reduceOriginalPricePointer(&item)

	fmt.Println("Wow! It changed this time to", item)
}

func main() {
	basicStructVariable()
	exploringTypes()
	tryingToModifyStructUsingAFunction()
	actuallyModifyStructUsingAFunction()
}
