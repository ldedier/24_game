# 24_game
24 game solver

![oops something went wrong, try to check on https://raw.githubusercontent.com/ldedier/24_game/master/resources/example.gif](https://raw.githubusercontent.com/ldedier/24_game/master/resources/example.gif)

## Summary

The 24 Game is an arithmetical card game in which the objective is to find a way to manipulate four integers so that the end result is 24. For example, for the card with the numbers 4, 7, 8, 8, a possible solution is (7 - (8 ÷ 8)) ✕ 4 = 24.

* The expression may use **parenthesis**, **additions**, **multiplications**, **divisions** and **substractions**.
* The expression must use **a single instance** of **all** of its input integers.

In this implementation, input integers have to be contained between **1** and **13**.
* For more informations about 24 game: [its wikipedia page](https://en.wikipedia.org/wiki/24_Game)


## Generalisation

In opposition to its official rules, this program may accept N integers with N ∈ [1-5].

Its upper limitation is only due to time constraints since all permutations of **operands**, **operators** and **parenthesis** are evaluated.

## Usage

**./24_game** `[-q]` **integer1** `[integer2][integer3][integer4][integer5]` 

## Result

This program lists every distinct ways to compute the goal of 24 according to the 24 game rules described previously.
