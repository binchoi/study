# Appending vs Filling Slices in Go: Performance Test

On my second week at work, I noticed that slices were being created and filled in the following manner across multiple Go services (e.g. in builders).

```
func (b *builder) mapDataToRule(dbRules []dbRule) []config.Rule {
	rules := make([]config.Rule, 0)
	for _, dbRule := range dbRules {
		rules = append(rules, b.mapDataToRule(dbRule))
	}
	return rules
}
	
```

Having recently learnt about the growth algorithm that Go's  `append` uses to increase the slice's capacity, I grew suspicious that initializing a slice with `make([]T, 0)` (which behaves the same way as `make([]T, 0, 0)`) and using `append` to add a fixed number of items would have suboptimal performance. 

My hypothesis was that if the length and capacity of the slice is initialized to the expected final length, the performance would be improved as we would prevent the overhead of growing a slice each time the capacity is exceeded.

implementation 1
```
func (b *builder) mapDataToRule(dbRules []dbRule) []config.Rule {
	rules := make([]config.Rule, len(dbRules))
	for i, dbRule := range dbRules {
		rules[i] = b.mapDataToRule(dbRule)
	}
    return rules
}	
```

implementation 2
```
func (b *builder) mapDataToRule(dbRules []dbRule) []config.Rule {
	rules := make([]config.Rule, len(dbRules))
	for i, dbRule := range dbRules {
		rules = append(rules, b.mapDataToRule(dbRule))
	}
    return rules
}	
```



I checked Go's implementation of slice ([code](https://github.com/golang/go/blob/master/src/runtime/slice.go)) which supported my suspicion. 

Before raising this to my colleague/manager, I decided to run benchmark performance tests to support my claim.

## Result

| Slice Length |   AppendToZeroCapacity (ns/op) |   AppendToNCapacity (ns/op) |   FillNLengthSlice (ns/op) |
|-------------:|-------------------------------:|----------------------------:|---------------------------:|
|            1 |                          13.77 |                       9.159 |                      9.136 |
|           10 |                         101.3  |                      23.46  |                     22.19  |
|          100 |                         347.3  |                     126.6   |                    126.5   |
|          500 |                        1032    |                     578.8   |                    548.6   |
|         1000 |                        2171    |                    1058     |                   1045     |

See line graph visualization [here](performance-test-results-visualized.ipynb).

## Outcome

When these findings were shared and the appropriate optimizations were applied to our projects (in tandem with other optimizations), 
there was visible increase in performance. Some services, such as one that is responsible for providing remote configurations for SDKs, 
experienced upto a **10% decrease in latency** (p50) in one of their core APIs.


---

#### fyi. Go's `append` under the hood

When the capacity of a slice is exceeded and the built-in `append` function is used to add an element to the slice, Go 
dynamically allocates a new, larger underlying array to hold the slice's elements. The elements from the original slice 
are then copied to the new array, and the new element is added to the end of the new array. The slice's internal 
pointers are then updated to point to the new array, and the original array is garbage collected. This process is known 
as a "grow" and it can cause a performance hit as it has to copy all elements over to new memory location.



