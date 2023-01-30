# study repo

## directory structure

```
└── study
    ├── README.md
    ├── go
    │   ├── 01-basic-go-syntax
    │   │   ├── 01-file-structure.go
    │   │   ├── 02-variables.go
    │   │   ├── 03-string-format.go
    │   │   ├── 04-control-structures.go
    │   │   ├── 05-arrays.go
    │   │   ├── 06-maps.go
    │   │   ├── 07-structs.go
    │   │   ├── 08-functions.go
    │   │   ├── 09-slices.go
    │   │   ├── 10-defined-types.go
    │   │   ├── 11-encapsulating-structs
    │   │   │   ├── 11-encapsulating-structs.go
    │   │   │   └── go.mod
    │   │   ├── 12-pointers.go
    │   │   └── 13-testing-methodology.go
    │   ├── 02-effective-go
    │   │   ├── 01-names.go
    │   │   └── 0x-leaky-buffer.go
    │   ├── 03-parallel-concurrent-distributed-programming
    │   │   ├── 01-goroutines.go
    │   │   ├── 02-channel-as-semaphore.go
    │   │   ├── 03-parallel-demultiplexing.go
    │   │   └── 04-parallelization.go
    │   ├── 04-applying-data-structure-and-algorithms
    │   │   └── 01-sliding-window.go
    │   ├── 05-deeper-dive
    │   │   └── 01-arrays-slices-and-strings
    │   │       ├── 01-arrays.go
    │   │       ├── 02-slices.go
    │   │       ├── 03-capacity.go
    │   │       └── a-slice-pointer-receiver.go
    │   ├── 06-design-patterns
    │   │   └── creational-design-patterns
    │   │       └── 01-singleton
    │   │           ├── 01-singleton-naive.go
    │   │           ├── 02-singleton-thread-safe.go
    │   │           └── 03-singleton-thread-safe-alt.go
    │   ├── 07-web-apps
    │   │   ├── 01-gowiki
    │   │   │   ├── data
    │   │   │   │   ├── FrontPage.txt
    │   │   │   │   ├── test.txt
    │   │   │   │   ├── test2.txt
    │   │   │   │   └── test3.txt
    │   │   │   ├── tmpl
    │   │   │   │   ├── edit.html
    │   │   │   │   └── view.html
    │   │   │   └── wiki.go
    │   │   └── 02-gin-tasting
    │   │       ├── go.mod
    │   │       ├── go.sum
    │   │       └── main.go
    │   ├── 08-testing
    │   │   └── 02-fuzzing
    │   │       ├── go.mod
    │   │       ├── main.go
    │   │       ├── reverse_test.go
    │   │       └── testdata
    │   │           └── fuzz
    │   ├── 09-playground
    │   │   ├── 01-make-slice-performance
    │   │   │   ├── README.md
    │   │   │   ├── go.mod
    │   │   │   ├── main.go
    │   │   │   ├── main_test.go
    │   │   │   └── performance-test-results-visualized.ipynb
    │   │   └── 02-goroutine-performance
    │   │       └── main.go
    │   └── a-util
    │       ├── 01-marshal-unmarshal.go
    │       ├── calendar
    │       │   ├── date.go
    │       │   └── event.go
    │       └── go.mod
    └── python
        ├── 01-20-patterns
        │   ├── 00-util
        │   │   └── template.py
        │   ├── 01-sliding-window
        │   │   ├── 1763-longest-nice-substring.py
        │   │   ├── 1876-substring-with-distinct-char.py
        │   │   ├── 219-contains-duplicate-ii.py
        │   │   ├── 2269-k-beauty-of-number.py
        │   │   ├── 395-longest-substring-w-min-k-repeating-char.py
        │   │   ├── 643-max-avg-subarrary-i.py
        │   │   ├── 904-fruit-into-baskets.py
        │   │   └── README.md
        │   ├── 02-matrix-traversal-(islands)
        │   │   ├── 200-number-of-islands.py
        │   │   └── README.md
        │   └── 03-two-pointers
        │       ├── 15-3sum.py
        │       ├── 160-intersection-of-two-linkedlist.py
        │       ├── 26-remove-duplicates-from-sorted-arr.py
        │       ├── 88-merge-sorted-array.py
        │       └── README.md
        ├── 02-blind75
        │   ├── 01-two-sum.py
        │   └── 02-longest-substring-without-repeating-characters.py
        ├── 03-playground
        │   └── main.py
        ├── 04-design-patterns
        │   └── creational-design-patterns
        │       └── 01-singleton
        │           ├── 01-singleton-naive.py
        │           └── 02-singleton-thread-safe.py
        └── 05-top-leet-questions
            ├── 01-easy-collection
            │   ├── 01-arrays
            │   │   ├── best-time-to-buy-sell-stock-2.py
            │   │   ├── contains-duplicates.py
            │   │   ├── intersection-of-two-arrays-ii.py
            │   │   ├── move-zeros.py
            │   │   ├── plus-one.py
            │   │   ├── remove-duplicates-from-sorted-array.py
            │   │   ├── rotate-array.py
            │   │   ├── rotate-image.py
            │   │   ├── single-number.py
            │   │   ├── two-sum.py
            │   │   └── valid-sudoku.py
            │   ├── 02-strings
            │   │   ├── first-unique-character-in-a-string.py
            │   │   ├── implement-strstr.py
            │   │   ├── longest-common-prefix.py
            │   │   ├── reverse-integer.py
            │   │   ├── reverse-string.py
            │   │   ├── string-to-integer-atoi.py
            │   │   ├── valid-anagram.py
            │   │   └── valid-palindrome.py
            │   ├── 03-linked-list
            │   │   ├── linked-list-cycle.py
            │   │   ├── merge-two-sorted-list.py
            │   │   ├── reverse-linked-list.py
            │   │   └── util.py
            │   ├── 04-trees
            │   │   ├── binary-tree-level-order-traversal.py
            │   │   ├── convert-sorted-array-to-bst.py
            │   │   ├── maximum-depth-of-binary-tree.py
            │   │   ├── tree-traversal-guide.py
            │   │   ├── util.py
            │   │   └── validate-binary-search-tree.py
            │   ├── 05-dynamic-programming
            │   │   ├── best-time-to-buy-and-sell-stock.py
            │   │   ├── climbing-stairs.py
            │   │   └── maximum-subarray.py
            │   ├── 06-maths
            │   │   ├── count-primes.py
            │   │   ├── fizzbuzz.py
            │   │   └── power-of-three.py
            │   ├── 07-sorting-and-searching
            │   │   └── first-bad-version.py
            │   ├── 08-design
            │   │   ├── min-stack.py
            │   │   └── shuffle-an-array.py
            │   └── 09-others
            │       ├── number-of-1-bits.py
            │       ├── pascals-triangle.py
            │       ├── reverse-bits.py
            │       └── valid-parenthesis.py
            └── 02-medium-collection
```
---
## Version
30 Jan 2023