package main

import (
	"fmt"
	"reflect"
)

func basicPointerPrinciples() {
	// You can get the address of a variable using & (an ampersand), which is
	// Go’s “address of” operator.
	var myInt int
	fmt.Printf("%v [%v] vs  %v [%v]\n",
		myInt, reflect.TypeOf(myInt),
		// The type of a pointer is written with a * symbol, followed by the type
		// of the variable the pointer points to.
		&myInt, reflect.TypeOf(&myInt))

	var myBool bool
	myBoolPointer := &myBool
	fmt.Println("myBoolPointer:", myBoolPointer)

	// You can get the value of the variable a pointer refers to by typing
	// the * operator right before the pointer in your code.
	fmt.Println("myBoolPointer's val:", *myBoolPointer)
}

func changeValAtPointer() {
	// The * operator can also be used to update the value at a pointer
	myInt := 100
	fmt.Println(myInt)

	myIntPointer := &myInt
	*myIntPointer = 10
	fmt.Println(myInt)
	// *myIntPointer accesses the variable at myIntPointer (that is, the
	// myInt variable) and assigns a new value to it.
}

func doubleNumber(num *int) {
	*num *= 2
	// which is short for...
	//*num = 2 * *num
}

func main() {
	basicPointerPrinciples()
	changeValAtPointer()

	myInt := 20
	fmt.Printf("original myInt %3d\n", myInt)
	doubleNumber(&myInt)
	fmt.Printf("updated myInt %3d\n", myInt)

}
