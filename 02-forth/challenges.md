# Forth Challenges

## Warm up challenges

1. Write two subroutines say-odd and say-even. say-odd prints the word odd to the screen and say-even prints the word even to the screen. Expected output:
        ```
        > say-odd
        odd
        > say-even
        even
        ```
2. Write a subroutine say-odd-or-even. The subroutine takes a number from the stack, prints that number; then, if it's odd, it calls say-odd, otherwise, it calls say-even.
        ```
        > 3 say-odd-or-even
        odd
        > 4 say-odd-or-even
        even
        ```
3. Write a subroutine say-odd-or-even-up-to. The subroutine takes a number from the stack, counts from 1 up to that number, and for each number encountered, calls say-odd-or-even.
        ```
        > 5 say-odd-or-even-up-to
        1 odd
        2 even
        3 odd
        4 even
        5 odd
        ```
## Grand Challenge

Implement the fibonacci subroutine. The subroutine takes a number t from the stack and replaces it with the number at the t-th position in he fibonacci sequence. 
The [fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number), if you haven't seen it, is a sequence of numbers which start with 1, and 1, but starting the 3rd number we can calculate the value as the sum of the previous two numbers.

*Hint: you can do it either using a loop or recursion. The key will be figuring out the correct
way to use stack manipulation subroutines.*