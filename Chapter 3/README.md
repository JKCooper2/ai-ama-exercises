# Chapter 3 - Solving Problems By Searching #
[Flashcards for chapter summary](http://www.cram.com/flashcards/chapter-3-7507199)


## Exercise 3.1 ##
Explain why problem formulation must follow goal formulation

### Solution ###
The goal is part of the problem definition. A different goal can result in an entirely different problem


## Exercise 3.2 ##
Consider the accessible, two-location vacuum world under Murphy's Law. Show that for
each initial state, there is a sequence of actions that is guaranteed to reach a goal state.

### Solution ###
Since the world is accessible you can just follow the steps: If there is dirt then suck, else move


## Exercise 3.3 ##
Give the initial state, goal test, operators, and path cost function for each of the following.
There are several possible formulations for each problem, with varying levels of detail. The
main thing is that your formulations should be precise and "hang together" so that they could be
implemented.

1. You want to find the telephone number of Mr. Jimwill Zollicoffer, who lives in Alameda,
given a stack of directories alphabetically ordered by city.
2. As for part (a), but you have forgotten Jimwill's last name.
3. You are lost in the Amazon jungle, and have to reach the sea. There is a stream nearby.
4. You have to color a complex planar map using only four colors, with no two adjacent
regions to have the same color.
5. A monkey is in a room with a crate, with bananas suspended just out of reach on the ceiling.
He would like to get the bananas.
6. You are lost in a small country town, and must find a drug store before your hay fever
becomes intolerable. There are no maps, and the natives are all locked indoors.

### Solution ###
#### Q1 ####
  * Initial State - x phone books containing n names
  * Goal Test - Does the name match
  * Operators - Select phone book: set of pages; select page: set of names; select name.
  * Past Cost - Time taken to find name
  * Algorithm - Select directory by town name, select page by start of last name, select name by first name

#### Q2 ####
  * Initial State - x phone books containing n names
  * Goal Test - Does the name match
  * Operators - Select phone book: set of pages; select page: set of names; select name.
  * Past Cost - Time taken to find name
  * Algorithm - Select directory by town name, go through each page searching for first-name

#### Q3 ####
  * Initial State - Position lat/long/alt, location of sea
  * Goal Test - Are you at the sea
  * Operators - Walk
  * Past Cost - Time taken to reach sea
  * Algorithm - Follow stream downhill as sea is at 0 alt

#### Q4 ####
  * Initial State - Position/Edges of planes
  * Goal Test - Are all plane colored with no adjacent regions having matching colours
  * Operators - Fill plane with 1 of four colours
  * Past Cost - Number of actions required
  * Algorithm - CSP, can use algorithms like Most Constrained Variable

#### Q5 ####
  * Initial State - Location of monkey, box and bananas
  * Goal Test - Does the monkey have the bananas
  * Operators - Monkey can move itself and the box
  * Past Cost - Time taken
  * Algorithm - Move box under bananas. Means-Ends Analysis

#### Q6 ####
  * Initial State - Town layout, your location
  * Goal Test - Are you at the drug store
  * Operators - Walk, look, make map
  * Past Cost - Time taken
  * Algorithm - Walk towards most built-up area and work out from there


## Exercise 3.4 ##
Implement the missionaries and cannibals problem and use breadth-first search to find the
shortest solution. Is it a good idea to check for repeated states? Draw a diagram of the complete
state space to help you decide

### Solution ###
missionaries_and_cannibals.py implements environment/search based on book description. Unfortunately the book
description is unsolvable because it only considers end points to be important, whereas the actual solution requires
a separate variable for who is sitting in the boat, rather than just who is on which side of the bank.

May add actual solution as a later stage


## Exercise 3.5 ##
On page 76, we said that we would not consider problems with negative path costs. In this
exercise, we explore this in more depth.

1. Suppose that a negative lower bound c is placed on the cost of any given step — that is,
negative costs are allowed, but the cost of a step cannot be less than c. Does this allow
uniform-cost search to avoid searching the whole tree?
2. Suppose that there is a set of operators that form a loop, so that executing the set in some
order results in no net change to the state. If all of these operators have negative cost, what
does this imply about the optimal behavior for an agent in such an environment? :
3. One can easily imagine operators with high negative cost, even in domains such as route-finding.
For example, some stretches of road might have such beautiful scenery as to far j
outweigh the normal costs in terms of time and fuel. Explain, in precise terms, why humans
do not drive round scenic loops indefinitely, and explain how to define the state space and I
operators for route-finding so that artificial agents can also avoid looping.
4. Can you think of a real domain in which step costs are such as to cause looping?

### Solution ###

1. Not if it wants to find the optimal solution, because there is always the possible of a loop of
negative cost in the future that can undo all positive cost actions
2. If they are the only negative cost nodes in the environment then the agents optimal behaviour is a continuous loop
3. You can explain this by states having a bias that decays towards 0 each time the agent visits. It starts at a large
negative cost and reduces down until taking the scenic route has less utility than taking the freeway
4. If a vacuum bot's reward was based on only dirt picked up it could constantly loop picking up and putting down dirt


## Exercise 3.6 ##
The GENERAL-SEARCH algorithm consists of three steps: goal test, generate, and ordering function, in that order.
It seems a shame to generate a node that is in fact a solution, but to fail to recognize it because the ordering
function fails to place it first.

1. Write a version of GENERAL-SEARCH that tests each node as soon as it is generated and stops immediately if it has found a goal.
2. Show how the GENERAL-SEARCH algorithm can be used unchanged to do this by giving it the proper ordering function

### Solution ###

1. GeneralSearchImmediateCheck() in immediate_search.py
2. BreadthFirstSearchImmediateCheck() in immediate_search.py


## Exercise 3.7 ##
The formulation of problem, solution, and search algorithm given in this chapter explicitly
mentions the path to a goal state. This is because the path is important in many problems. For
other problems, the path is irrelevant, and only the goal state matters. Consider the problem
"Find the square root of 123454321." A search through the space of numbers may pass through
many states, but the only one that matters is the goal state, the number 11111. Of course, from a
theoretical point of view, it is easy to run the general search algorithm and then ignore all of the
path except the goal state. But as a programmer, you may realize an efficiency gain by coding a
version of the search algorithm that does not keep track of paths. Consider a version of problem
solving where there are no paths and only the states matter. Write definitions of problem and
solution, and the general search algorithm. Which of the problems in Section 3.3 would best use
this algorithm, and which should use the version that keeps track of paths?

### Solution ###
Problem - Solving a jigsaw puzzle
Solution - When each piece is in it's correct spot
General Search - Where does each piece need to be placed

Because all actions can be considered independently the ordering of the paths are irrelevant, and so the problem
can be solved with needing to keep track of paths


## Exercise 3.9 ##
Describe a search space in which iterative deepening search performs much worse than depth-first search

### Solution ###
Depth First would perform better if the branching factor is very low but goal state quite deep, or the correct path
happens to be down the path of the first options.


## Exercise 3.10 ##
Figure 3.17 shows a schematic view of bidirectional search. Why do you think we chose
to show trees growing outward from the start and goal states, rather than two search trees growing
horizontally toward each other

### Solution ###
The dimensions along with the search space expands is only dependent on the root node and search policy,
the goal node could essentially be positioned around any point of the start node


## Exercise 3.11 ##
Write down the algorithm for bidirectional search, in pseudo-code or in a programming
language. Assume that each search will be a breadth-first search, and that the forward and
backward searches take turns expanding a node at a time. Be careful to avoid checking each node
in the forward search against each node in the backward search

### Solution ###
BidirectionalSearch() in search.py. Uses updated GeneralSearch with hashed nodes and step expansion ability


## Exercise 3.12 ##
Give the time complexity of bidirectional search when the test for connecting the two
searches is done by comparing a newly generated state in the forward direction against all the
states generated in the backward direction, one at a time.

### Solution ###
O(n^2). Worst case every node gets compared to half the other nodes (constant factor)


## Exercise 3.13 ##
We said that at least one direction of a bidirectional search must be a breadth-first search.
What would be a good choice for the other direction? Why?

For optimality with constant step cost BFS or UCS will work, depth first could run into loops.
From the goal-side searches point of view there is just has an additional goal node added every step.


## Exercise 3.14 ##
Consider the following operator for the 8-queens problem: place a queen in the column
with the fewest un-attacked squares, in such a way that it does not attack any other queens. How
many nodes does this expand before it finds a solution? (You may wish to have a program
calculate this for you.)

### Solution ###
Run n_queens.py with search as relevant algorithm. Using DepthFirst can solve in with approx 2,000 nodes expanded.
Using BreadthFirst can solve with approx 120,000 checks (much slower from list concatenation as well)


## Exercise 3.15 ##
The chain problem (Figure 3.20) consists of various lengths of chain that must be reconfigured
into new arrangements. Operators can open one link and close one link. In the standard
form of the problem, the initial state contains four chains, each with three links. The goal state
consists of a single chain of 12 links in a circle. Set this up as a formal search problem and find
the shortest solution.

### Solution ###
See chain_problem.py. Quite slow as deepcopy of node takes time and problem has high branching factor.
Implementation slightly different to description as each side can be independently opened and closed,
as opposed to link being open and having a maximum of 2 other links added. May revisit in future

Shortest solution 8 actions for this model, either by opening and connecting each edge link,
or by breaking apart one chain into 3 links and connecting each of them.