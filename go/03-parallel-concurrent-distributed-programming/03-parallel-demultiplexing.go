package main

import (
	"fmt"
	"time"
)

// CHANNELS OF CHANNELS
// In Go, channels are first-class value that can be allocated and passed around like any other.
// A common use of this property is to implement safe, parallel demultiplexing.

// def: multiplexer is a device that has multiple inputs and single line output
//      demultiplexer is a device that has a single line input and multiple outputs

type RequestB struct {
	args       []int
	f          func([]int) int
	resultChan chan int
}

func sum(arr []int) (s int) {
	for _, elem := range arr {
		s += elem
	}
	return
}

const MaxOutstandingB = 10

func handleB(queue chan *RequestB) {
	for req := range queue {
		// add a slight delay for requests whose arg[0] is even [i.e. those that should sum to an odd value]
		// why? just to add a little spice :-)
		if req.args[0]%2 == 0 {
			time.Sleep(2 * time.Second)
		}
		req.resultChan <- req.f(req.args)
	}
}

func ServeB(queue chan *RequestB) {
	for i := 0; i < MaxOutstandingB; i++ {
		go handleB(queue)
	}
}

func main() {
	clientRequests := make(chan *RequestB, 10)

	reqArr := make([]*RequestB, 10)
	for i := 0; i < 10; i++ {
		request := &RequestB{[]int{i, i + 1, i + 2}, sum, make(chan int)}
		reqArr[i] = request
		// Send request
		clientRequests <- request
	}

	ServeB(clientRequests)

	// Wait for response [choose random request]
	//randInt := rand.Intn(10)
	//fmt.Printf("args: %v | res: %d\n", reqArr[randInt].args, <-reqArr[randInt].resultChan)
	//if randInt < 9 {
	//	fmt.Printf("args: %v | res: %d\n", reqArr[randInt+1].args, <-reqArr[randInt+1].resultChan)
	//}

	for _, req := range reqArr {
		go func(b *RequestB) {
			fmt.Printf("args: %4v | res: %d\n", b.args, <-b.resultChan)
		}(req)
	}

	time.Sleep(5 * time.Second)
}
