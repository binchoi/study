package main

import (
	"testing"
	"unicode/utf8"
)

func TestReverse(t *testing.T) {
	testcases := []struct {
		input, expected string
	}{
		{"Hello, world", "dlrow ,olleH"},
		{" ", " "},
		{"!12345", "54321!"},
	}

	for _, tc := range testcases {
		rev, err := Reverse(tc.input)
		if err != nil {
			continue
		}
		if rev != tc.expected {
			t.Errorf("Actual: %q, Expected %q\n", rev, tc.expected)
		}
	}
}

// The unit test has limitations, namely that each input must be added to the test by the developer.
// One benefit of fuzzing is that it comes up with inputs for your code, and may identify edge cases
// that the test cases you came up with did not reach.

func FuzzReverse(f *testing.F) { // function starts with "Fuzz" and takes *testing.F as arg
	testcases := []string{"Hello, world", " ", "!12345"}
	for _, tc := range testcases {
		// Use f.Add to provide a seed corpus (= a set of valid and interesting inputs that
		// serve as starting points for a fuzzer)
		f.Add(tc)
	}
	f.Fuzz(func(t *testing.T, orig string) { // f.Fuzz instead of t.Run
		rev, err := Reverse(orig)
		if err != nil {
			return // you can also call t.Skip() to stop the execution of that fuzz input
		}
		doubleRev, err := Reverse(rev)
		if err != nil {
			return // you can also call t.Skip() to stop the execution of that fuzz input
		}
		// t.Logf prints to CLI if error occurs, or if executing the test with -v, which helps debugging
		t.Logf("Number of runes: orig=%d, rev=%d, doubleRev=%d\n", utf8.RuneCountInString(orig), utf8.RuneCountInString(rev), utf8.RuneCountInString(doubleRev))
		t.Logf("Values: orig=%s, rev=%s, doubleRev=%s\n", orig, rev, doubleRev)
		if orig != doubleRev {
			t.Errorf("Before: %q, after: %q", orig, doubleRev)
		}
		if utf8.ValidString(orig) && !utf8.ValidString(rev) {
			t.Errorf("Reverse produced invalid UTF-8 string %q", rev)
		}
	})
}

// Limitations of Fuzzing: When fuzzing, you can’t predict the expected output, since you
// don’t have control over the inputs.

// Rather, fuzz tests check for certain properties. In our example, we are checking two properties:
// 1. Reversing a string twice preserves the original value
// 2. The reversed string preserves its state as valid UTF-8.

// If a failure occurs while fuzzing, the input that caused the problem is written to a seed corpus
// file (in testdata/) that will be run the next time go test is called, even without the -fuzz flag

// Error uncovered by Fuzzing: The entire seed corpus used strings in which every character was a single byte,
// characters such as 泃 can require several bytes. Thus, reversing the string byte-by-byte will invalidate
// multi-byte characters

// To run specific test cases within your corpus:
// ``go test -run=FuzzReverse/d7da8a4...`` [i.e. {FuzzTestName}/{filename}]

// To run fuzz test for a specified duration (default is to continue indefinitely until error thrown)...
// ``go test -fuzz=Fuzz -fuzztime 30s``
