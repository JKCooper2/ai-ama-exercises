# Chapter 6 - Propositional Logic #
[Flashcards for chapter summary](http://www.cram.com/flashcards/chapter-6-agents-that-reason-logicaly-7511652)

To be completed:
6.11, 6.12, 6.13, 6.14, 6.15, 6.16

## Exercise 6.1 ##
We said that truth tables can be used to establish the validity of a complex sentence. Show
how they can be used to decide if a given sentence is valid, satisfiable, or unsatisfiable.

### Solution ###
See Truth Table Q1.jpg for examples where sentences are satisfiable (can be sometimes true), valid (always matches
a fact), or unsatisfiable (never matches a fact)


## Exercise 6.2 ##
Use truth tables to show that the following sentences are valid, and thus that the equivalences
hold. Some of these equivalence rules have standard names, which are given in the right column

### Solution ###
See tables in folder 6.2


## Exercise 6.3 ##
Look at the following sentences and decide for each if it is valid, unsatisfiable, or neither.
Verify your decisions using truth tables, or by using the equivalence rules of Exercise 6.2. Were
there any that initially confused you?
1. Smoke => Smoke
2. Smoke => Fire
3. (Smoke => Fire) => (-Smoke => -Fire)
4. Smoke V Fire V —Fire
5. ((Smoke & Heat) => Fire) <=> ((Smoke => Fire) V (Heat => Fire))
6. (Smoke => Fire) => ((Smoke & Heat) => Fire)
7. Big V Dumb V (Big => Dumb)
8. (Big & Dumb) V -Dumb

### Solution ###
1. Valid - Something implies itself
2. Satisfiable - Nothing states that fire has to follow smoke
3. Satisfiable - Contraposition would require -Fire and -Smoke to be swapped
4. Valid - Either fire or -fire will always be true
5. Valid - If either imply then both must
6. Valid - Adding a conjunct that doesn't negate maintains the original sentence
7. Valid - True if big, true if dumb, true if not big (default for false premise)
8. Satisfiable - States on big things can be dumb


## Exercise 6.4 ##
Is the sentence "Either 2 + 2 = 4 and it is raining, or 2 + 2 = 4 and it is not raining" making
a claim about arithmetic, weather, or neither? Explain

### Solution ###
It is making a claim about arithmetic because it's stating that the sentence 2+2=4 is valid in all models


## Exercise 6.5 ##
(Adapted from (Barwise and Etchemendy, 1993). Given the following, can you prove that
the unicorn is mythical? How about magical? Horned?
"If the unicorn is mythical, then it is immortal, but if it is not mythical, then it is a
mortal mammal. If the unicorn is either immortal or a mammal, then it is horned.
The unicorn is magical if it is horned."

### Solution ###
Mythical: Can't be stated
Horned: Yes because it covers entire mythical partition from which direct extensions determine if it has a horn
Magical: Yes, follows from being horned


## Exercise 6.6 ##
What ontological and epistemological commitments are made by the language of real number arithmetic?

### Solution ###
Ontological Commitments:
  * That number has a value related to each other, which is contained in their label
  * How operator functions alter variables
  * That a function can only have one output

Epistemological Commitments:
  * Equality
  * Lesser/Greater Than


## Exercise 6.7 ##
Consider a world in which there are only four propositions, A, B, C, and D. How many
models are there for the following sentences?

1. A & B
2. A V B
3. A & B & C

### Solution ###
Number is possible values for that proposition that would leave the sentence true
1. 4 (2C * 2D)
2. 12 (1A * 2C * 2D + 1B * 2C * 2D + 1A * 1B * 2C * 2D)
3. 2 (2D)


## Exercise 6.8 ##
We have defined four different binary logical connectives.
1. Are there any others that might be useful?
2. How many binary connectives can there possibly be?
3. Why are some of them not very useful?

### Solution ###
1. XOR, =, !=
2. 24, 4! combinations
3. They don't relate to ways that humans normally thing about things


## Exercise 6.9 ##
Some agents make inferences as soon as they are told a new sentence, while others wait until
they are asked before they do any inferencing. What difference does this make at the knowledge
level, the logical level, and the implementation level?

### Solution ###
Knowledge Level: Agents that make inferences at the start will know more things
Logical Level: More predicates will be available
Implementation Level: The process of proving sentences will involve a much larger search space as the KB will contain
a lot of irrelevant rules


## Exercise 6.10 ##
We said it would take 64 prepositional logic sentences to express the simple rule "don't
go forward if the wumpus is in front of you." What if we represented this fact with the single rule
WumpusAhead => -Forward
Is this feasible? What effects does it have on the rest of the knowledge base?

### Solution ###
This simply places the 64 rules under the definition of WumpusAhead, so the end result is just an additional rule
being added rather which covers the rest
