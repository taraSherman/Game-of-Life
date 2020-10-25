# Game of Life

Created by British mathematician John Conway in 1970, The Game of Life begins with a grid of cells and an initial configuration wherein each cell is in one of 2 possible states: live or dead. 

>A cellular automaton is a model of a system consisting of a collection of cells on a grid of specified shape and size that evolve through a number of discrete time steps, changing states according to a set of rules based on the states of adjacent cells. The rules are then applied iteratively for as many time steps as desired.

Every cell is evaluated according to the state of its eight neighbors (adjacent cells), using the four 'rules' of The Game of Life:

### Rules

    1. A live cell that has less than 2 live neighbors will die.
    2. A live cell with either 2 or 3 live neighbors will continue to live.
    3. A live cell with more than 3 live neighbors will die.
    4. A dead cell with exactly 3 live neighbors will come to life.

### Turing Completeness

If a system (language, model) is theoretically capable of solving any computational problem, given infinite space and time, then  it is said to be Turing-complete. Theoretically, the Game of Life is as powerful as any computer with unlimited memory and no time constraints, i.e. a universal Turing machine; anything that can be computed algorithmically can be computed within the Game of life.

### Patterns
There are many types of patterns that have been observed in The Game of Life. Each pattern is classified according to its behavior. Some examples include:

![example-patterns](https://media.giphy.com/media/4VVZTvTqzRR0BUwNIH/giphy.gif)

[from Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)

## Implementation
This repository is an implementation of the Game of Life using Python 3.8.5 and Pygame 1.9.6. I would classify it as a work in progress as it is a tool for me to learn Python and Pygame. At this point in time, it is not available except by forking, although I hope to add more functionality in the future.

#### Lesson Objectives
https://github.com/taraSherman/Game-of-Life/blob/main/objectives.md
https://github.com/taraSherman/Game-of-Life/tree/tara-sherman/objectives.md