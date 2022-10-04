package main

import (
	"fmt"
	"math/rand"
	"time"
)

// PARALLELIZATION
// Another application of channels and goroutines is to parallelize a calculation across multiple CPU cores.
// If the calculation can be broken into separate pieces that can execute independently, it can be parallelized,
// with a channel to signal when each piece completes.

// Consider the following idealized example: we have an expensive operation to perform on a vector of items
// where the value of the operation on each item is independent.

type Vector []float64

// SPECIFYING NUMBER OF CPU CORES

// Declare as constant
const numCPU = 4

// Alternatively, we could ask the runtime what value is appropriate.
// The following returns the number of hardware CPU cores in the machine.
//var numCPU = runtime.NumCPU()

// As another option, we could ask the runtime for the user-specified number of cores that a Go program
// can run simultaneously. It defaults to the value of runtime.NumCPU but can be overridden by
// setting the similarly named shell environment variable or by calling the function with a positive number.
// var numCPU = runtime.GOMAXPROCS(0) // Calling it with zero just queries the value

func (v Vector) Op(i float64) float64 {
	time.Sleep(1 * time.Second)
	return 10 * i
}

// DoSome applies the operation to v[i], v[i+1], ... v[n-1]
func (v Vector) DoSome(i, n int, u Vector, c chan int) {
	for ; i < n; i++ {
		v[i] += u.Op(v[i])
	}
	c <- 1 // signal that this piece is done
}

// We launch the pieces independently in a loop, one per CPU. They can complete in any order
// but it doesn't matter; we just count the completion signals by draining the channel after
// launching all the goroutines.

func (v Vector) DoAll(u Vector) {
	// buffering is optional but sensible
	c := make(chan int, numCPU)
	for i := 0; i < numCPU; i++ {
		go v.DoSome(i*len(v)/numCPU, (i+1)*len(v)/numCPU, u, c)
	}
	// Drain the channel
	for i := 0; i < numCPU; i++ {
		<-c // wait for one task to complete
	}
	// All done
}

func (v Vector) DoAllSequential(u Vector) {
	for i := 0; i < len(v); i++ {
		v[i] += u.Op(v[i])
	}
}

func main() {
	rand.Seed(12345)
	v := Vector{11, 12, 13, 14}
	startParallel := time.Now()
	v.DoAll(v)
	parallelExecutionTime := time.Since(startParallel)
	fmt.Printf("%v | Completed parallel operation in %v\n", v, parallelExecutionTime)
	v = Vector{11, 12, 13, 14, 15}
	startSequential := time.Now()
	v.DoAllSequential(v)
	sequentialExecutionTime := time.Since(startSequential)
	fmt.Printf("%v | Completed sequential operation in %v\n", v, sequentialExecutionTime)
}
