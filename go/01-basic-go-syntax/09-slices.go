package main

import "fmt"

func basicSliceUsage() {
	// unlike arrays, declaring slices doesn't automatically create the slice
	var myIntArr []int
	var myStrArr []string

	// you must create it with the built-in make function
	myIntArr = make([]int, 5)
	myStrArr = make([]string, 5)

	// initially filled with zero values of the assigned type
	fmt.Println(myIntArr)
	fmt.Println(myStrArr)

	myIntArr[0] = 8
	myIntArr[3] = 7
	fmt.Println(myIntArr)

	myStrArr[0] = "first string"
	fmt.Println(myStrArr)
}

func sliceLiteralsInitializeWithValues() {
	myIntArr := []int{1, 2, 3}
	myStrArr := []string{"a", "b", "c", "d", "e"}

	fmt.Println(myIntArr)
	fmt.Println(myStrArr)
}

func useMakeToSlice() {
	myIntArr := make([]int, 10)
	fmt.Printf("%#v LEN: %v\n", myIntArr, len(myIntArr))
}

func checkOutSliceLen() {
	myIntArr := []int{1, 2, 3}
	myStrArr := []string{"a", "b", "c", "d", "e"}

	fmt.Printf("%v [%T] LEN: %v\n", myIntArr, myIntArr, len(myIntArr))
	fmt.Printf("%v [%T] LEN: %v\n", myStrArr, myIntArr, len(myStrArr))
}

func sliceIsFromArray() {
	myIntArr := [3]int{1, 2, 3}
	myIntSlice := myIntArr[:]

	fmt.Printf("%v [%T] LEN: %v\n", myIntArr, myIntArr, len(myIntArr))
	fmt.Printf("%v [%T] LEN: %v\n", myIntSlice, myIntSlice, len(myIntSlice))
}

func sliceAndArrayRelationship() {
	myStrArr := []string{"a", "b", "c", "d", "e"}
	myStrSlice := myStrArr[:3]

	fmt.Println("init")
	fmt.Println(myStrArr)
	fmt.Println(myStrSlice)

	// change element in arr and change is reflected in the slice
	fmt.Println("change arr element")
	myStrArr[1] = "X"
	fmt.Println(myStrArr)
	fmt.Println(myStrSlice)

	// change element in slice and change is reflected in the arr
	fmt.Println("change slice element")
	myStrSlice[2] = "Y"
	fmt.Println(myStrArr)
	fmt.Println(myStrSlice)
}

func sliceCanAppend() {
	myStrArr := []string{"a", "b", "c", "d", "e"}
	myStrSlice := myStrArr[:3]

	fmt.Println(myStrSlice)

	// append(slice, elems)
	// If it has sufficient capacity, the destination is resliced to accommodate the new elements.
	// If it does not, a new underlying array will be allocated. Append returns the updated slice

	myStrSlice = append(myStrSlice, "x")
	myStrSlice = append(myStrSlice, "y")
	myStrSlice = append(myStrSlice, "z")
	myStrSlice = append(myStrSlice, "1")
	myStrSlice = append(myStrSlice, "2")
	myStrSlice = append(myStrSlice, "3")
	fmt.Println(myStrSlice)

	// append is a variadic functions (i.e. it can call as many arguments as needed)
	myStrSlice2 := make([]string, 0)
	myStrSlice2 = append(myStrSlice2, "a", "b", "c", "d", "e")
	fmt.Println(myStrSlice2)
}

func sliceHasZeroValue() {
	var mySlice []int

	fmt.Printf("%#v [%T] LEN: %v\n", mySlice, mySlice, len(mySlice))

	if mySlice == nil {
		fmt.Println("zero value of slice is nil")
	}
}

func main() {
	basicSliceUsage()
	sliceLiteralsInitializeWithValues()
	checkOutSliceLen()
	sliceIsFromArray()

	sliceAndArrayRelationship()
	sliceCanAppend()

	sliceHasZeroValue()

	useMakeToSlice()
}
