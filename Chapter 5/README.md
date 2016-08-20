# Chapter 5 - Game Playing #
[Flashcards for chapter summary](http://www.cram.com/flashcards/chapter-5-game-playing-7509366)


## Exercise 5.1 ##
This problem exercises the basic concepts of game-playing using Tic-Tac-Toe (noughts and
crosses) as an example. We define X[n] as the number of rows, columns, or diagonals with exactly
n X's and no O's. Similarly, O[n] is the number of rows, columns, or diagonals with just n O's. The
utility function thus assigns +1 to any position with X[3], = 1 and —1 to any position with O[3], - 1.

All other terminal positions have utility 0. We will use a linear evaluation function defined as
`Eval = 3*X[2] + X[1] - (3*O[2] + O[1])`

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


## Exercise 5.4 ##
The algorithms described in this chapter construct a search tree for each move from scratch.
Discuss the advantages and disadvantages of retaining the search tree from one move to the next
and extending the appropriate portion. How would tree retention interact with the use of selective
search to examine "useful" branches of the tree?

### Solution ###
Advantages:
  * Allows you to maintain of states to expand based on the evaluation function without having to recalculate anything

Disadvantages:
  * Takes up more memory
  * Ordering of states can become slow (depending on queuing insert type)

Tree retention would work as described in advantages


## Exercise 5.6 ##
Prove that with a positive linear transformation of leaf values, the move choice remains
unchanged in a game tree with chance nodes.

### Solution ###
Because expectimax uses the sum of the weighted max actions based on probabilities, if you apply a positive linear
transformation it will raise the value of all max actions but preserve the order, and also when the average is taken
the final expectimax values will be the original expectimax values shifted by the transformation. This means the
ordering after taking the expected value is also the same, and so the decision doesn't actually change


## Exercise 5.7 ##
Consider the following procedure for choosing moves in games with chance nodes:
  * Generate a suitable number (say, 50) dice-roll sequences down to a suitable depth (say, 8).
  * With known dice rolls, the game tree becomes deterministic. For each dice-roll sequence,
solve the resulting deterministic game tree using alpha-beta.
  * Use the results to estimate the value of each move and choose the best.

Will this procedure work correctly? Why (not)?

### Solution ###
It will work (is called Monte Carlo Search), but it's accuracy depends on the percentage of nodes cover. With 8 dice
rolls there are 8^6 (262,144) possible outcomes, so using 50 only covers 0.02% of those.


## Exercise 5.8 ##
Let us consider the problem of search in a three-player game. (You can assume no alliances
are allowed for now.) We will call the players 0, 1, and 2 for convenience. The first change is
that the evaluation function will return a list of three values, indicating (say) the likelihood of
winning for players 0, 1, and 2, respectively.

1. Complete the following game tree by filling in the backed-up value triples for all remaining
nodes, including the root
2. Rewrite Minimax-Decision and Minimax-Value so that they work correctly for the three-player game.
3. Discuss the problems that might arise if players could form and terminate alliances as well
as make moves "on the board." Indicate briefly how these problems might be addressed.

### Solution ###
1. See 3 Player Minimax.png
2.
```
function MINIMAX-DECISION(game) returns an operator
for each op in OPERATORS(do)
    VALUE[op] <- MINIMAX-VALUE(APPLY(op, game), game)
end
return the op with the highest VALUE[op]

function MINIMAX-VALUE(state, game) returns a utility value
if TERMINAL-TEST[game](state) then
    return UTILITY[game](state)
else
    return the highest MINIMAX-VALUE of SUCCESSORS(state) for player index in utility tuple
```
3. With alliances it means minimax won't work as the assumption that each player is acting independently in their best
interests is lost. E.g. In the example the the path always choosing option B will lead to a higher score for all players
than the minimax score, however the opportunity to backstab will override this. These problems could be addressed
by not allowing communication between players.


## Exercise 5.9 ##
Describe and implement a general game-playing environment for an arbitrary number of
players. Remember that time is part of the environment state, as well as the board position

### Solution ###
The only addition required is the player turn ordering so the players are aware of who acts after who.


## Exercise 5.10 ##
Suppose we play a variant of Tic-Tac-Toe in which each player sees only his or her own
moves. If the player makes a move on a square occupied by an opponent, the board "beeps" and
the player gets another try. Would the backgammon model suffice for this game, or would we
need something more sophisticated? Why?

### Solution ###
Not sure what the backgammon model is, but to describe this you would need to expand the tree for each unknown space
on the board each time. If the space returns a beep then you can fill it with a O and continue on that branch

