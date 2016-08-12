# Chapter 2 - Intelligent Agents #
[Flashcards for chapter summary](http://www.cram.com/flashcards/chapter-2-7503921)


## Exercise 2.1 ##
What is the difference between a performance measure and a utility function?

### Solution ###
A performance measure is objective and can include information unavailable to the agent. A utility function
only includes information available to the agent and is an estimate of the performance measure


## Exercise 2.2  ##
For each of the environments in Figure 2.3, determine what type of agent architecture is
most appropriate (table lookup, simple reflex, goal-based or utility-based).

### Solution ###
* Medical Diagnosis System - Utility Based
* Satellite Image Analysis System - Goal Based
* Part Picking Robot - Goal Based
* Refinery Controller - Utility Based
* Interactive English Tutor - Goal Based


## Exercise 2.3 ##
Choose a domain that you are familiar with, and write a PAGE description of an agent
for the environment. Characterize the environment as being accessible, deterministic, episodic,
static, and continuous or not. What agent architecture is best for this domain?

### Solution ###
Selected Domain: Poker
Percepts: Cards in hand, cards on table, chip counts, table position, bet amounts
Actions: Fold, Check, Bet, Raise
Goals: Maximise chip count
Environment: Poker Table


## Exercise 2.4 ##
While driving, which is the best policy?

1. Always put your directional blinker on before turning,
2. Never use your blinker,
3. Look in your mirrors and use your blinker only if you observe a car that can observe you?

What kind of reasoning did you need to do to arrive at this policy (logical, goal-based, or utility-based)?
What kind of agent design is necessary to carry out the policy (reflex, goal-based, or utility-based)?

### Solution ###
Best policy is 1. Logical reasoning based on if everyone takes that action the world will work in a desirable way.
Reflex agent can carry out this policy


## Exercise 2.5 ##
Implement a performance-measuring environment simulator for the vacuum-cleaner  world.

This world can be described as follows:
*Percepts:*
Each vacuum-cleaner agent gets a three-element percept vector on eac  turn.
The first element, a touch sensor, should be a 1 if the  machine has bumped into something
and a 0 otherwise.  The second comes from a photosensor under the machine, which emits
a 1 if there is dirt there and a 0 otherwise. The third comes from an infrared sensor, which
emits a 1 when the agent is in its home location, and a 0 otherwise.

*Actions:*
There  are  five  actions  available:
 - Go  forward
 - Turn right  by 90°
 - Turn  left  by 90°
 - Suck up dirt
 - Turn off.

*Goals:*
The goal for each agent is to clean up and go home. To be precise, the performance
measure will be 100 points for each piece of dirt vacuumed up, minus 1 point for each
action taken, and minus 1000 points if it is not in the home location when it turns itself off.

*Environment:*
The environment consists of a grid of squares. Some squares contain
obstacles (walls and furniture) and other squares are open space.  Some of the open squares
contain dirt. Each "go forward" action moves one square unless there is an obstacle in that
square, in which case the agent stays where it is, but the touch sensor goes on. A "suck up
dirt" action always cleans up the dirt. A "turn off" command ends the simulation.

### Solution ###
Solution contained in environment.py and agent.py


## Exercise 2.7 ##
Implement an environment for a n x m rectangular room, where each square has a 5% chance
of containing dirt, and n and m are chosen at random from the range  8 to  15, inclusive.

### Solution ###
Set ENV_SIZE and DIRT_CHANCE in main.py


## Exercise 2.8 ##
Design and implement a pure reflex agent for the environment of Exercise  2.7, ignoring
the requirement of returning home, and measure its performance. Explain why it is impossible
to have a reflex agent that returns home and shuts itself off. Speculate on what the best possible
reflex agent could do. What prevents a reflex agent from doing very well?

### Solution ##
Load ReflexAgent from agents.py

Impossible for a reflex agent to return home because it only knows it's immediate environment.
Best possible is to wonder around cleaning dirt until it reaches home in which case it turns off.
Prevented by no way to keep track of what it has already seen/done


## Exercise 2.9 ##
Design and implement several agents with internal state. Measure their performance. How
close do they come to the ideal agent for this environment?

### Solution ###
Load InternalAgent from agents.py

Performance works well, visiting unknown states until all possible unknown states have been checked before
returning home. Path optimisation, mapping edges, and choice of way to turn could use some work.


## Exercise 2.10 ##
Calculate the size of the table for a table-lookup agent in the domain of Exercise 2.7.
Explain your calculation. You need not fill in the entries for the table

### Solution ###
For a 10x10 room each row would take (r = 10*2 + 1) actions to clear (suck-move * 10 plus a turn before the final move).
For the entire board this would be (b = r*10 - 2) because the final turn and move actions aren't needed
Each turn has (t = (10x10)^2) possible percept vectors (dirt or no dirt in each square)
Lookup size = t^b = ((10*10)^2) ^ ((10*2+1)*10-2) = 10000^208 = 10^211 table values
See TableLookup10x10() in agents for completed table


## Exercise 2.11 ##
Experiment with changing the shape and dirt placement of the room, and with adding
furniture. Measure your agents in these new environments. Discuss how their performance
might be improved to handle more complex geographies.

### Solution ###
Agent could be improved by first identifying the edges of the location and then optimising a path through the
remaining squares. Could also make actions based on largest area of unknown squares, or always choose unknown
squares over known ones when available and moving towards a point.

