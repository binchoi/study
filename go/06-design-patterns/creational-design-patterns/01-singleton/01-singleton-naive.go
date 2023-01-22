package main

import "fmt"

type single struct {
	value int
}

var singleInstance *single

func getInstance(value int) *single {
	if singleInstance == nil {
		fmt.Println("Creating single instance now.")
		singleInstance = &single{value}
	} else {
		fmt.Println("Single instance already exists.")
	}
	return singleInstance
}

func main() {
	s1 := getInstance(1)
	s2 := getInstance(2)
	fmt.Printf("%v, %v", s1, s2)
}
