package main

import (
	"fmt"
	"sync"
)

var once sync.Once

type singleton struct {
	value int
}

var singletonInstance *singleton

func getSingletonInstance(value int) *singleton {
	if singletonInstance == nil {
		once.Do(
			func() {
				fmt.Println("Creating single instance now.")
				singletonInstance = &singleton{value}
			})
	} else {
		fmt.Println("Singleton instance already created.")
	}
	fmt.Printf("Returning %v\n", singletonInstance)
	return singletonInstance
}

func main() {
	for i := 0; i < 30; i++ {
		go getSingletonInstance(i)
	}

	fmt.Scanln()
}
