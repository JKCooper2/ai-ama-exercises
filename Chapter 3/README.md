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
1.  Initial State - x phone books containing n names
..  Goal Test - Does the name match
..  Operators - Select phone book: set of pages; select page: set of names; select name.
..  Past Cost - Time taken to find name
..  Algorithm - Select directory by town name, select page by start of last name, select name by first name
2.  Initial State - x phone books containing n names
..  Goal Test - Does the name match
..  Operators - Select phone book: set of pages; select page: set of names; select name.
..  Past Cost - Time taken to find name
..  Algorithm - Select directory by town name, go through each page searching for first-name
3.  Initial State - Position lat/long/alt, location of sea
..  Goal Test - Are you at the sea
..  Operators - Walk
..  Past Cost - Time taken to reach sea
..  Algorithm - Follow stream downhill as sea is at 0 alt
4.  Initial State - Position/Edges of planes
..  Goal Test - Are all plane colored with no adjacent regions having matching colours
..  Operators - Fill plane with 1 of four colours
..  Past Cost - Number of actions required
..  Algorithm - CSP, can use algorithms like Most Constrained Variable
5.  Initial State - Location of monkey, box and bananas
..  Goal Test - Does the monkey have the bananas
..  Operators - Monkey can move itself and the box
..  Past Cost - Time taken
..  Algorithm - Move box under bananas. Means-Ends Analysis
6.  Initial State - Town layout, your location
..  Goal Test - Are you at the drug store
..  Operators - Walk, look, make map
..  Past Cost - Time taken
..  Algorithm - Walk towards most built-up area and work out from there


## Exercise 3.4 ##
Implement the missionaries and cannibals problem and use breadth-first search to find the
shortest solution. Is it a good idea to check for repeated states? Draw a diagram of the complete
state space to help you decide

### Solution ###
missionaries_and_cannibals.py implements environment/search based on book description. Unfortunately the book
description is unsolvable because it only considers end points to be important, whereas the actual solution requires
a separate variable for who is sitting in the boat, rather than just who is on which side of the bank.

May add actual solution as a later stage