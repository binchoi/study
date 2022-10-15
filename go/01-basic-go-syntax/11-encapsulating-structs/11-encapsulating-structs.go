package main

import (
	"fmt"
	"github.com/binchoi/study/go/a-util/calendar"
)

func main() {
	date := calendar.Date{}
	if err := date.SetDate(1972, 1, 19); err != nil {
		fmt.Println("Oh No!")
	}
	fmt.Println(date.Year(), date.Month(), date.Day())
}
