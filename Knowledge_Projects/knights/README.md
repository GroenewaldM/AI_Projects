# Knights


## Summary

This program represents 'Knights and Knaves' puzzles using propositional logic, such that an AI running a model-checking algorithm could solve these puzzles for us.


## Background

In 1978, logician Raymond Smullyan published “What is the name of this book?”, a book of logical puzzles. Among the puzzles in the book were a class of puzzles that Smullyan called “Knights and Knaves” puzzles.

In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.

The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave.

For example, consider a simple puzzle with just a single character named A. A says “I am both a knight and a knave.”

Logically, we might reason that if A were a knight, then that sentence would have to be true. But we know that the sentence cannot possibly be true, because A cannot be both a knight and a knave – we know that each character is either a knight or a knave, but not both. So, we could conclude, A must be a knave.


## Getting Started

* Download the distribution code from https://github.com/GroenewaldM/AI_Projects/tree/main/Knowledge_Projects/knights.
* Run puzzle.py


## Understanding

logic.py defines several classes for different types of logical connectives. 
logic.py also contains a function model_check. model_check takes a knowledge base and a query. model_check recursively considers all possible models, and returns True if the knowledge base entails the query, and returns False otherwise.

The main function of puzzle.py loops over all puzzles, and uses model checking to compute, given the knowledge for that puzzle, whether each character is a knight or a knave, printing out any conclusions that the model checking algorithm is able to make.


## Example Output

py -m puzzle

Puzzle 0

A is a Knave 

Puzzle 1

A is a Knave 

B is a Knight

Puzzle 2

A is a Knave

B is a Knight

Puzzle 3

A is a Knight

B is a Knave

C is a Knight


## Authors

* Project by HarvardX CS50AI: CS50's Introduction to Artificial Intelligence with Python
* Project completed by Monique Groenewald
