#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
Linear time
The while loop is called n times

b) O(n^2)
Quadratic time
The two loops (for and while), each run at O(n), so multiplying them together we get O(n^2)

c) O(n)
Linear time
The recursive function acts as a loop and is called n times. The rest is O(1) so we can ignore the constants.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

To do it with only 1 egg, we'd need to drop the egg floor by floor until we reach the floor that it breaks from. f will then be that floor -1. This minimizes the number of eggs we use, but at worst, it would take n times. The runtime complexity of this would be O(n).

We can also try a binary search. Throw an egg from floor n/2. If it breaks, then can we can drop another egg from floow (n/2)/2, and continue dividing until we find the floor at which the egg does not break. The runtime complexity of this would be O(logn)
