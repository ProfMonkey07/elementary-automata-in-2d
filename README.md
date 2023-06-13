# elementary-automata-in-2d
An implementation of wolframs 1d elementary automata using a 2 dimensional grid. Rendered with pygame
it uses the top 3 sides of each cell to get the next state
it does so by creating 3 sets of 3 cells, the 3 on the left, the 3 on top, and the three on the right
it then uses the 1d rules to get a state from each of those, and assembles them into a set of 3 states, (left, top, right)
to get the cell state it applies the rules to the state made up of all 3 sides

many patterns result in chaos but some rules result in really interesting behavior


![alt text]([http://url/to/img.png](https://github.com/ProfMonkey07/elementary-automata-in-2d/blob/main/Screen%20Shot%202023-06-12%20at%2023.43.33.png?raw=true))
