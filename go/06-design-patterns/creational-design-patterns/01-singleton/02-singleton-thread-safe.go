package main

import (
	"fmt"
	"sync"
)

type singleThreadSafe struct {
	value int
}

var lock = &sync.Mutex{}

var singleThreadSafeInstance *singleThreadSafe

func getThreadSafeInstance(value int) *singleThreadSafe {
	if singleThreadSafeInstance == nil {
		lock.Lock()
		defer lock.Unlock()
		if singleThreadSafeInstance == nil {
			fmt.Println("Creating single instance now.")
			singleThreadSafeInstance = &singleThreadSafe{value}
		} else {
			fmt.Println("Single instance already exists.")
		}
	} else {
		fmt.Println("Single instance already exists.")
	}
	return singleThreadSafeInstance
}

func main() {
	for i := 0; i < 30; i++ {
		go getThreadSafeInstance(i)
	}
	fmt.Scanln()
}
