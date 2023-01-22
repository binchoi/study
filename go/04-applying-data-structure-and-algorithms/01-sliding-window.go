package main

// https://leetcode.com/problems/longest-nice-substring/

// A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
// For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
// appears, but 'B' does not.

// Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of
// the earliest occurrence. If there are none, return an empty string.

func longestNiceSubstring(s string) string {
	// base cases
	if len(s) < 2 {
		return ""
	}

	lonely_alphabets_set = findLonelyAlphabets(s)

}

func findLonelyAlphabets(s string) {
	search := make(map[string]int)
	res := make(map[string]int)

	for _, c := range s { // how to iterate thorugh the substrings/chars of a string
		search[c] = 0
	}

}

func isNice(s string) bool {
	return true
}

func main() {

}
