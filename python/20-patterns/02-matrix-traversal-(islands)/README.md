# Sliding Window
Window Sliding Technique is a computational technique which aims to reduce the use of nested loop and 
replace it with a single loop, thereby reducing the time complexity.

## Prereqs
The **size of window** for computation is (generally) fixed throughout the complete nested loop.

## General Instructions
1. Find the size of window required 
2. Compute the result for 1st window, i.e. from start of data structure 
3. Then use a loop to slide the window by 1, and keep computing the result window by window.

## Time Complexity
Time Complexity: `O(n)` [at least]  
Space Complexity: `O(1)` [window size is generally fixed