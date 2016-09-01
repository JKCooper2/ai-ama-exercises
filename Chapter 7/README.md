# Chapter 7 - First Order Logic #
[Flashcards for chapter summary](http://www.cram.com/flashcards/chapter-7-first-order-logic-7511681)


To be completed:
7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 7.10, 7.11, 7.12, 7.13, 7.14, 7.15, 7.16

## Exercise 7.1 ##
A logical knowledge base represents the world using a set of sentences with no explicit
structure. An analogical representation, on the other hand, is one in which the representation has
structure that corresponds directly to the structure of the thing represented. Consider a road map
of your country as an analogical representation of facts about the country. The two-dimensional
structure of the map corresponds to the two-dimensional surface of the area.
1. Give five examples of symbols in the map language.
2. An explicit sentence is one that the creator of the representation actually writes down. An
implicit sentence is one that results from explicit sentences because of properties of the
analogical representation. Give three examples each of implicit and explicit sentences in
the map language.
3. Give three examples of facts about the physical structure of your country that cannot be
represented in the map language.
4. Give two examples of facts that are much easier to express in the map language than in
first-order logic,
5. Give two other examples of useful analogical representations. What are the advantages
and disadvantages of each of these languages?

### Solution ###
1. Road, river, town, mountain, lake
2. Explicit:
  * Scale showing distance
  * Road colours indicating surface type
  * Lakes are coloured in blue
Implicit:
  * An intersection is where two roads meet
  * A river can flow into a lake
  * A road can't go through a lake

3. Whether a road goes through a mountain or over it, how deep a lake a is, whether there are bike paths on the roads
4. Possible paths from one place to another, how many lakes are within a towns borders
5. Architects plans for a house, colour matching palette. Advantages are it provides a simpler view of the relationship
between items that are considered important, in a less abstract manner. Disadvantages are it is more difficult to
compare knowledge from that representation to other representations


## Exercise 7.2 ##
Represent the following sentences in first-order logic, using a consistent vocabulary (which
you must define):
1. Not all students take both History and Biology.
2. Only one student failed History.
3. Only one student failed both History and Biology.
4. The best score in History was better than the best score in Biology.
5. Every person who dislikes all vegetarians is smart.
6. No person likes a smart vegetarian.
7. There is a woman who likes all men who are not vegetarians.
8. There is a barber who shaves all men in town who do not shave themselves.
9. No person likes a professor unless the professor is smart.
10. Politicians can fool some of the people all of the time, and they can fool all of the people
some of the time, but they can't fool all of the people all of the time.

### Solution ###
See folder 7.2


## Exercise 7.3 ##
We noted that there is often confusion because the => connective does not correspond
directly to the English "if ... then" construction. The following English sentences use "and,"
"or," and "if" in ways that are quite different from first-order logic. For each sentence, give
both a translation into first-order logic that preserves the intended meaning in English, and
a straightforward translation (as if the logical connectives had their regular first-order logic
meaning). Show an unintuitive consequence of the latter translation, and say whether each
translation is valid, satisfiable or invalid.

1. One more outburst like that and you'll be in contempt of court.
2. Annie Hall is on TV tonight, if you're interested.
3. Either the Red Sox win or I'm out ten dollars.
4. The special this morning is ham and eggs.
5. Maybe I'll come to the party and maybe I won't.
6. Well, I like Sandy and I don't like Sandy.
7. I don't jump off the Empire State Building implies if I jump off the Empire State Building
then I float safely to the ground.
8. It is not the case that if you attempt this exercise you will get an F. Therefore, you will
attempt this exercise.
9. If you lived here you would be home now. If you were home now, you would not be here.
Therefore, if you lived here you would not be here.

### Solution ###
See Folder 7.3


## Exercise 7.4 ##
Give a predicate calculus sentence such that every world in which it is true contains exactly
one object.

### Solution ###
See 7.4.jpg


## Exercise 7.5 ##
Represent the sentence "All Germans speak the same languages" in predicate calculus. Use
Speaks(x, l), meaning that person x speaks language l.

### Solution ###
See 7.5.jpg


## Exercise 7.6 ##
Write axioms describing the predicates Grandchild, GreatGrandparent, Brother, Sister,
Daughter, Son, Aunt, Uncle, Brother-In-Law, Sister-In-Law, and FirstCousin. Find out the proper
definition of mth cousin n times removed, and write it in first-order logic.
Write down the basic facts depicted in the family tree in Figure 7.4. Using the logical reasoning
system in the code repository, TELL it all the sentences you have written down, and ASK it
who are Elizabeth's grandchildren, Diana's brothers-in-law, and Zara's great-grandparents.

### Solution ###
See 7.6.jpg


## Exercise 7.7 ##
Explain what is wrong with the following proposed definition of the set membership
predicate G :
\forall x,s x \in {x|s}
\forall x,s x \in s => \forall y x \in {y|s}

### Solution ###
The implication results in it being true when the premise is false