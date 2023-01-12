package main

import (
	"encoding/json"
	"fmt"
)

type Dummy struct {
	Name   string `json:"name"`
	Number int64  `json:"number"`
	IsOdd  bool   `json:"is_odd"`
}

func main() {
	data := []byte("{\"name\": \"test\", \"number\": 2}") // , "is_odd": true

	var dummy Dummy
	err := json.Unmarshal(data, &dummy) // if property is missing, fall to default value of designated type
	if err != nil {
		fmt.Printf("%+v\n", err)
	}

	// we want to print the field names as well
	fmt.Printf("dummy = %+v\n", dummy)
	fmt.Printf("pointer = %+v\n", dummy.IsOdd)

	DummyFunction(dummy.IsOdd)

}

func DummyFunction(arg1 bool) {
	fmt.Printf("%+v\n", arg1)
}
