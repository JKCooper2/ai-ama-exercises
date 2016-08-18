# Chapter 5 - Game Playing #
[Flashcards for chapter summary](http://www.cram.com/flashcards/chapter-5-game-playing-7509366)


## Exercise 5.1 ##
This problem exercises the basic concepts of game-playing using Tic-Tac-Toe (noughts and
crosses) as an example. We define X[n] as the number of rows, columns, or diagonals with exactly
n X's and no O's. Similarly, O[n] is the number of rows, columns, or diagonals with just n O's. The
utility function thus assigns +1 to any position with X[3], = 1 and —1 to any position with O[3], - 1.

All other terminal positions have utility 0. We will use a linear evaluation function defined as
Eval = 3*X[2] + X[1] - (3*O[2] + O[1])

1. Approximately how many possible games of Tic-Tac-Toe are there?
2. Show the whole game tree starting from an empty board down to depth 2, (i.e., one X and
one O on the board), taking symmetry into account. You should have 3 positions at level
1 and 12 at level 2.
3. Mark on your tree the evaluations of all the positions at level 2.
4. Mark on your tree the backed-up values for the positions at levels 1 and 0, using the
minimax algorithm, and use them to choose the best starting move.
5. Circle the nodes at level 2 that would not be evaluated if alpha-beta pruning were applied,
assuming the nodes are generated in the optimal order for alpha-beta pruning.

### Solution ###
1. 9^3 (9 squares by 3 options [X, O, _] per square = 729
2. Level 1:
```
 X   Y   Z
X__ _X_ ___
___ ___ _X_
___ ___ ___

Level 2:
 A   B   C   D   E
XO_ X_O X__ X__ X__
___ ___ __O _O_ ___
___ ___ ___ ___ __O

 F   G   H   I   J
OX_ _X_ _X_ _X_ _X_
___ O__ _O_ ___ ___
___ ___ ___ O__ _O_

 K   L
_O_ O__
_X_ _X_
___ ___
```

3. A: 1, B: 0, C: 1, D: -1, E: 0
   F: -1, G: 0, H: -2, I: -1, J: 0
   K: 2, L: 1

4. X: -1, Y: -2, Z: 1

5. A, B, C, D, E, F, G, H, I, J would all not be evaluated as Z is clearly a better choice
