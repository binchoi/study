package main

import (
	"fmt"
	"math/rand"
	"time"
)

func classicForLoop() {
	for i := 1; i <= 10; i++ {
		fmt.Println(i)
	}
}

func forLoopAsWhileLoop() {
	i := 1
	for i <= 10 {
		fmt.Println(i)
		i++
	}
}

func infiniteLoop() {
	i := 0
	for {
		i++
		if i >= 100 {
			fmt.Printf("Wow we just reached %v. Let's break out now.\n", i)
			break
		}
	}
}

func ifElse() {
	for i := 1; i <= 10; i++ {
		if i%2 == 1 {
			fmt.Printf("Wow that's pretty odd... ;-) :  %v\n", i)
		} else {
			fmt.Println(i)
		}
	}
}

func ifElseIf() {
	for i := 1; i <= 10; i++ {
		if i%3 == 0 {
			fmt.Printf("Divisible by 3 :  %v\n", i)
		} else if i%3 == 1 {
			fmt.Printf("Remainder is 1 : %v\n", i)
		} else {
			fmt.Printf("Remainder is 2 : %v\n", i)
		}
	}
}

func switchItUp() {
	for cnt := 1; cnt < 11; cnt++ {
		rand.Seed(time.Now().UnixNano())
		i := rand.Intn(100)
		switchItUpHelper(i)
	}
}

func switchItUpHelper(i int) {
	switch i % 3 {
	case 0:
		fmt.Printf("Divisible by 3 : %v\n", i)
	case 1:
		fmt.Printf("Remainder is 1 : %v\n", i)
	case 2:
		fmt.Printf("Remainder is 2 : %v\n", i)
	}
}

func main() {
	fmt.Println("for-loop")
	classicForLoop()
	forLoopAsWhileLoop()
	infiniteLoop()

	fmt.Println("if")
	ifElse()
	ifElseIf()

	fmt.Println("switch")
	switchItUp()
}
