package main

import (
	"fmt"
	"math/rand"
	"time"
)

// A buffered channel can be used like a semaphore, for instance to limit throughput.

// Semaphores are a type of synchronization primitive. It is a variable or abstract data type used to
// control access to a common resource by multiple threads and avoid critical section problems in a
// concurrent system such as a multitasking operating system

// METHOD 1

const MaxOutstanding = 5

var sem = make(chan int, MaxOutstanding)

type Request struct {
	id int
}

func process(r *Request) {
	fmt.Println("| process started. id", r.id)
	time.Sleep(time.Duration(rand.Intn(5)) * time.Second)
	fmt.Println("| processing finished. id", r.id)
}

func Serve(queue chan *Request) {
	for req := range queue {
		fmt.Printf("req %d waiting for a seat...\n", req.id)
		sem <- 1
		fmt.Printf("req %d found a seat!\n", req.id)
		// Shadow the loop variable locally and make the Request input unique to each goroutine.
		go func(req *Request) {
			process(req)
			<-sem
		}(req)
	}
	fmt.Println("All queue items have been popped.") // never reached!
}

// ServeAlternativeImpl is an alternative serve method (same under the hood) - METHOD 1 [alt.]
func ServeAlternativeImpl(queue chan *Request) {
	for req := range queue {
		// Create new instance of req for the goroutine. This is legal and idiomatic in Go.
		req := req
		sem <- 1
		go func() {
			process(req)
			<-sem
		}()
	}
}

// METHOD 2
// Another approach that manages resources well is to start a fixed number of handle goroutines all
// reading from the request channel. The number of goroutines limits the number of simultaneous calls
// to process. This Serve function also accepts a channel on which it will be told to exit; after
// launching the goroutines it blocks receiving from that channel.

func handle(queue chan *Request) {
	for req := range queue {
		process(req)
	}
}

func ServeWithFixedGoroutines(queue chan *Request, quit chan bool) {
	// Start handlers (fixed number)
	for i := 0; i < MaxOutstanding; i++ {
		go handle(queue)
	}
	<-quit
}

func main() {
	// METHOD 1
	var reqChan chan *Request
	reqChan = make(chan *Request, 10)
	go func() {
		for i := 0; i < 10; i++ {
			reqChan <- &Request{i}
		}
	}()
	go Serve(reqChan) // returns `fatal error: all goroutines are asleep` when Serve() run by main goroutine
	//go ServeAlternativeImpl(reqChan) // this implementation works too!

	time.Sleep(5 * time.Second)

	fmt.Println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

	// METHOD 2
	reqChan2 := make(chan *Request, 10)
	quitChan := make(chan bool)
	go func() {
		for i := 0; i < 10; i++ {
			reqChan2 <- &Request{i}
		}
	}()
	go ServeWithFixedGoroutines(reqChan2, quitChan)
	time.Sleep(5 * time.Second)
	quitChan <- true
	fmt.Println("ServeWithFixedGoroutines told to quit/finish execution")

}
