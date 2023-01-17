package main

import (
	"bytes"
	"fmt"
)

type path []byte

func (p *path) TruncateAtFinalSlashPtr() {
	i := bytes.LastIndex(*p, []byte("/"))
	if i >= 0 {
		*p = (*p)[0:i]
	}
}

func (p path) TruncateAtFinalSlashType() { // useless
	i := bytes.LastIndex(p, []byte("/"))
	if i >= 0 {
		p = (p)[0:i]
	}
}

// If we wanted a method that causes changes to the underlying array, the type of the receiver can be a value
// rather than a pointer.

func (p path) ToUpper() {
	for i, b := range p {
		if 'a' <= b && b <= 'z' {
			p[i] = b + 'A' - 'a'
		}
	}
}

func (p *path) ToUpperPtr() { // this of course works too
	pathObject := *p
	for i, b := range pathObject {
		if 'a' <= b && b <= 'z' {
			pathObject[i] = b + 'A' - 'a'
		}
	}
}

func main() {
	pathName := path("/usr/bin/tso") // Conversion from string to path.
	pathName.TruncateAtFinalSlashPtr()
	fmt.Printf("%s\n", pathName)

	fmt.Println("********* TruncateAtFinalSlashType *********")
	pathName.TruncateAtFinalSlashType()
	fmt.Printf("%s\n", pathName) // no change

	fmt.Println("********* ToUpper *********")
	pathName.ToUpper()
	fmt.Printf("%s\n", pathName) // change applied as underlying array is changed

}
