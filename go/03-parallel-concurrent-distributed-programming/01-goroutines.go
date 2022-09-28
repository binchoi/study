package main

import (
	"fmt"
	"time"
)

// GO'S APPROACH TO CONCURRENCY
// Concurrent programming in many environments is made difficult by the subtleties required to implement
// correct access to shared variables. Go encourages a different approach in which shared values are passed
// around on channels and, in fact, never actively shared by separate threads of execution. Only one goroutine
// has access to the value at any given time. Data races cannot occur, by design. In short:

// Do not communicate by sharing memory; instead, share memory by communicating.

// As a high-level approach, using channels to control access makes it easier to write clear, correct programs.
// If the communication is the synchronizer, there's still no need for other synchronization. Unix pipelines,
// for example, fit this model perfectly. Although Go's approach to concurrency originates in Hoare's
// Communicating Sequential Processes (CSP), it can also be seen as a type-safe generalization of Unix pipes.

// GOROUTINE
// Existing terms — including threads, coroutines, and processes — convey inaccurate connotations and cannot
// precisely capture the essence of goroutines.

// A goroutine has a simple model: it is a function executing concurrently with other goroutines in the same
// address space.

// It is lightweight, costing little more than the allocation of stack space. And the stacks start small,
// so they are cheap, and grow by allocating (and freeing) heap storage as required.

// Goroutines are multiplexed onto multiple OS threads so if one should block, such as while waiting for I/O,
//others continue to run. Their design hides many of the complexities of thread creation and management.

func findSum(arr []int) {
	var sum int
	for _, elem := range arr {
		sum += elem
	}
	fmt.Println(sum)
}

func basicGoroutines(arr []int, someOtherArr []int) {
	go findSum(arr)
	go findSum(someOtherArr)
}

func announceMessage(message string, delay time.Duration) {
	// Prefix a function or method call with the go keyword to run the call in a new goroutine. When the call
	// completes, the goroutine exits, silently.
	// function literals are handy when invoking goroutines.
	go func() {
		time.Sleep(delay)
		fmt.Println("[ANNOUNCEMENT]:", message)
	}() // Note the parentheses - we must call the function!
}

// CHANNELS
// To signal completion of goroutines, we need channels
// examples
// ci := make(chan int)            // unbuffered channel of integers
// cj := make(chan int, 0)         // unbuffered channel of integers
// cs := make(chan *os.File, 100)  // buffered channel of pointers to Files

// Unbuffered channels combine communication with synchronization, guaranteeing that two calculations
// (goroutines) are in a known state.

func useChannelIdioms1() {
	c := make(chan int) // Allocate a channel
	go func() {
		// some operation
		sum := 0
		for i := 0; i < 100; i++ {
			sum += i
		}
		c <- 1 // Send a signal; value does not matter
	}()

	// do something for a while
	time.Sleep(time.Second * 3)

	<-c // Wait for sort to finish; discard sent value.
}

func useChannelIdioms2() {
	c := make(chan int) // Allocate a channel
	sum := 0
	go func(sum *int) {
		for i := 0; i < 100; i++ {
			*sum += i
		}
		c <- 1 // Send a signal; value does not matter
	}(&sum)

	// do something for a while
	time.Sleep(time.Second * 3)

	<-c
	fmt.Println(sum)
}

// Receivers always block until there is data to receive.

// If the channel is unbuffered, the sender blocks until the receiver has received the value.
// If the channel has a buffer...
// AND buffer is not full: the sender blocks only until the value has been copied to the buffer (virtually no block)
// AND buffer is full: the sender waits until some receiver has retrieved a value.

func main() {
	basicGoroutines([]int{1, 2, 3, 4, 5, 6}, []int{10, 20, 30, 40, 50, 60})
	announceMessage("announcement 1", 0)
	time.Sleep(time.Second * 2)
	useChannelIdioms1()
	useChannelIdioms2()

}
