# Sum Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in finding the sum of a group of even numbers.

Our function will be given a 2D tuple of numbers and a starting position tuple in (row, column) format. For example:

```py
nums = (
    (1, 2, 3, 4),
    (7, 8, 6, 4),
    (6, 9, 8, 2),
    (2, 5, 2, 1)
)
starting_position = (0, 1)
```

We can see that the value at `starting_position` is 2. We can notice that this 2 is adjacent to another even number, an 8. This 8 is adjacent to a 6, which is adjacent to other even numbers, and so on. These even numbers are connected other adjacent even numbers in a group. Including the starting position, there are 8 numbers connected to it in a group. The sum of the numbers in this group is 36.

Note that the 6 and the 2 in the bottom left hand corner are NOT connected to this larger group. We only consider values to be adjacent that are directly above, below, left of, or right of another value (no diagonals).

Write a function that takes a grid and a starting position and returns the sum of even numbers in a group connected to the starting position. _Include the value at the starting position in the sum._

It is guaranteed that the starting position will be within the bounds of the grid and will have an even value.

## Examples

For the following grid data:

```py
nums = (
    (1, 2, 3, 4),
    (7, 8, 6, 4),
    (6, 9, 8, 2),
    (2, 5, 2, 1),
)
```

The following table shows a selection of starting locations, and the sum that would result from starting there:

| Starting Position | Sum |
| ----------------- | --- |
| (0, 1)            | 36  |
| (2, 2)            | 36  |
| (3, 0)            | 8   |
