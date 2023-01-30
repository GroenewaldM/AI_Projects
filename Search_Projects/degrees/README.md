# Degrees


## Summary
This program finds the shortest path between any two actors by choosing a sequence of movies that connects them.


## Background

According to the Six Degrees of Kevin Bacon game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.

For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.”


## Getting Started

* Download the distribution code from https://github.com/GroenewaldM/AI_Projects/tree/main/Search_Projects/degrees.
* Run degrees.py


## Understanding
The distribution code contains a CSV data file. This is a small dataset for ease of testing and experimentation.

The dataset consists of three CSV files. In small/people.csv you’ll see that each person has a unique id, corresponding with their id in IMDb’s database. They also have a name, and a birth year.

In small/movies.csv you’ll see here that each movie also has a unique id, in addition to a title and the year in which the movie was released.

small/stars.csv establishes a relationship between the people in people.csv and the movies in movies.csv. Each row is a pair of a person_id value and movie_id value. The first row (ignoring the header), for example, states that the person with id 102 starred in the movie with id 104257. Checking that against people.csv and movies.csv, you’ll find that this line is saying that Kevin Bacon starred in the movie “A Few Good Men.”

The people dictionary maps each person’s id to another dictionary with values for the person’s name, birth year, and the set of all the movies they have starred in. And the movies dictionary maps each movie’s id to another dictionary with values for that movie’s title, release year, and the set of all the movie’s stars. The load_data function loads data from the CSV files into these data structures.

The main function in this program first loads data into memory. Then, the function prompts the user to type in two names. The person_id_for_name function retrieves the id for any person (and handles prompting the user to clarify, in the event that multiple people have the same name). The function then calls the shortest_path function to compute the shortest path between the two people, and prints out the path.


### Example Output

py -m degrees
Loading data...
Data loaded.
Name: tom cruise
Name: tom hanks
2 degrees of separation.
1: Tom Cruise and Kevin Bacon starred in A Few Good Men
2: Kevin Bacon and Tom Hanks starred in Apollo 13

## Authors

* Project by HarvardX CS50AI: CS50's Introduction to Artificial Intelligence with   Python
* Project completed by Monique Groenewald
