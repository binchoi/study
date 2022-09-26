package main

import (
	"errors"
	"fmt"
)

func repeatLines(line string, rep int) {
	for i := 0; i < rep; i++ {
		fmt.Println(line)
	}
}

func powerOf(base int, exponent int) (int, error) {
	if exponent < 0 {
		return 0, errors.New("exponent is less than 1")
	}

	res := 1
	for i := 0; i < exponent; i++ {
		res = res * base
	}
	return res, nil
}

func playWithPowerOf() {
	var powerOfArr [8][2]int
	powerOfArr[0][0], powerOfArr[0][1] = 5, 2
	powerOfArr[1][0], powerOfArr[1][1] = 8, 1
	powerOfArr[2][0], powerOfArr[2][1] = 1, 100
	powerOfArr[3][0], powerOfArr[3][1] = 100, 2
	powerOfArr[4][0], powerOfArr[4][1] = 7, 0
	powerOfArr[5][0], powerOfArr[5][1] = 0, 20
	powerOfArr[6][0], powerOfArr[6][1] = -1, 6

	powerOfArr[7][0], powerOfArr[7][1] = 5, -2

	for _, argArr := range powerOfArr {
		res, err := powerOf(argArr[0], argArr[1])
		if err != nil {
			fmt.Println("[ERROR]", err.Error())
		} else {
			fmt.Printf("%3d  ** %3d = %v\n", argArr[0], argArr[1], res)
		}
	}
}

func main() {
	repeatLines("hi", 5)
	playWithPowerOf()
}
