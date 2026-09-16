**Goal**: provide the steps for the right penguin to reach the fish as fast as possible



**General Rules:**

* A penguin in motion will not stop until colliding with a wall or another penguin
* The goal is not fulfilled if a different colored penguin reaches the fish
* you must reach the fish within 10 seconds





**Observations**:





*  It's inferred that only one penguin can move at a time





* A penguin will most likely be in the position adjacent to the source of a collision (A penguin, wall, edge of map)





* According to Patel, the layout of the board is will always be the same no matter the random seed







**What I need to do:**



* figure out a method for detecting a collision with a wall or penguin that varies depending on the direction (if a penguin is going up, are there any walls ahead?)





*  Figure out where collisions could occur to lead the designated penguin to the fish (basically pathfinding)



* Set up the environment in VsCode



**Tips from mentors:**



might be easier to look for a path by going from the fish to the penguin rather then the penguin to the fish. I didn't fully understand how though.

