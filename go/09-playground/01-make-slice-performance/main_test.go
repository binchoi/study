package main

import "testing"

var SLICE_LEN int = 1000

func BenchmarkAppendToZeroCapacity(b *testing.B) {
	for i := 0; i < b.N; i++ {
		AppendToZeroCapacity(SLICE_LEN)
	}
}

func BenchmarkAppendToNCapacity(b *testing.B) {
	for i := 0; i < b.N; i++ {
		AppendToNCapacity(SLICE_LEN)
	}
}

func BenchmarkFillNLengthSlice(b *testing.B) {
	for i := 0; i < b.N; i++ {
		FillNLengthSlice(SLICE_LEN)
	}
}
