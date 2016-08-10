# EXERCISES: #

## 2.5 ##
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

### SOLUTION ###
Solution contained in environment.py and agent.py


## 2.7 ##
Implement an environment for a n x m rectangular room, where each square has a 5% chance
of containing dirt, and n and m are chosen at random from the range  8 to  15, inclusive.

### SOLUTION ###
Set ENV_SIZE and DIRT_CHANCE in main.py


## 2.8 ##
Design and implement a pure reflex agent for the environment of Exercise  2.7, ignoring
the requirement of returning home, and measure its performance. Explain why it is impossible
to have a reflex agent that returns home and shuts itself off. Speculate on what the best possible
reflex agent could do. What prevents a reflex agent from doing very well?

### SOLUTION ##
Load ReflexAgent from agents.py

Impossible for a reflex agent to return home because it only knows it's immediate environment.
Best possible is to wonder around cleaning dirt until it reaches home in which case it turns off.
Prevented by no way to keep track of what it has already seen/done


## 2.9 ##
Design and implement several agents with internal state. Measure their performance. How
close do they come to the ideal agent for this environment?

### SOLUTION ###
Load InternalAgent from agents.py

Performance works well, visiting unknown states until all possible unknown states have been checked before
returning home. Path optimisation, mapping edges, and choice of way to turn could use some work.