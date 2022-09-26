package main

import "fmt"

func basicArrayUsage() {
	var myIntArr [10]int
	var myStrArr [5]string

	// initially filled with zero values of the assigned type
	fmt.Println(myIntArr)
	fmt.Println(myStrArr)

	myIntArr[0] = 8
	myIntArr[6] = 7
	fmt.Println(myIntArr)

	myStrArr[0] = "first string"
	fmt.Println(myStrArr)
}

func arrayLiteralsInitializeWithValues() {
	myIntArr := [3]int{1, 2, 3}
	myStrArr := [5]string{"a", "b", "c", "d", "e"}

	fmt.Println(myIntArr)
	fmt.Println(myStrArr)
}

func checkOutArrLen() {
	myIntArr := [3]int{1, 2, 3}
	myStrArr := [5]string{"a", "b", "c", "d", "e"}

	fmt.Printf("%v LEN: %v\n", myIntArr, len(myIntArr))
	fmt.Printf("%v LEN: %v\n", myStrArr, len(myStrArr))
}

func main() {
	basicArrayUsage()
	arrayLiteralsInitializeWithValues()
	checkOutArrLen()
}
