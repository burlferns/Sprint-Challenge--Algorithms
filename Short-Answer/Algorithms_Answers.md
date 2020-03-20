#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```
a) The while loop has a start point of a=0 and an end point of a = n^3. The step size for a is n^2. Therefore the number of steps for a is (n^3-0)/(n^2), which is n. Thus this program runs in O(n) time 
```

```
b) The outer for loop has a start point of i=0 and an end point of i = n-1. The step size for i is 1. Therefore the number of steps for i in the outer loop is ((n-1)-0)/1 = n-1. Thus the outer for loop is O(n) time

The inner while loop has a start point of j=1 and a stop point of the last increment of j that is less than n. The step size of j is such that it doubles every time. Thus j is the sequence of numbers 1,2,4,8,16,32... This is the sequence 2^0, 2^1, 2^2, 2^3, 2^4, 2^5 ... So the value of j at each step index is 2^x, where x is the integer step index number that starts from 0. Thus the while loop ends at the maximum x value for which 2^x < n. Thus x < (log n)/(log 2). Since the maximum x is determined by (log n), the outer while loop is O(log n) 

So the two loops together are O(n * log n) which is O(n log n) run time.
```

```
c) This recursive function will run from the start point of bunnies=n (where n is the integer argument of the first call to the bunnyEars function) to the end point of bunnies = 0. The step size of bunnies is -1. Thus the number of times that the recursive function will run is (0-n)/(-1)+1 which is n+1 (1 is added because it also runs for the value of bunnies=0). So this function runs in O(n) time
```

## Exercise II

```
This is a search for floor f in a building with floors from 1 to n where dropping an egg from floor f or higher will break the egg, but dropping the egg from floor (f-1) or lower will not break the egg.

A linear search from floor 1 to higher floors, dropping an egg from each floor at a time will result in too many dropped & broken eggs.

A better search would be a binary search where half the floors at a time are eliminated for not being a possible floor f.

This better binary search would have a run time complexity of O(log n) and its algoritm would be:

LOW = 1
HIGH = n
while TRUE:
    HALF_POINT = keep_only_integer_portion_of_float_result((HIGH+LOW)/2)
    if LOW + 1 == HIGH
        break_out_of_loop
    if drop_egg_from_floor(HALF_POINT) == breaks_the_egg:
        HIGH = HALF_POINT
    if drop_egg_from_floor(HALF_POINT) != breaks_the_egg:
        LOW = HALF_POINT
print(f'f is {HIGH}')


Note that the keep_only_integer_portion_of_float_result function must not make a float input like 6.5 equal to 7. It must only drop the '.5' and yield a result of 6

```
