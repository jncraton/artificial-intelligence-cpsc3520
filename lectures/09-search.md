Search
======

Planning
--------

- The correct action is not always obvious
- It can be helpful to consider a series of possible actions
- We must then *search* for optimal outcomes

Goal Formulation
----------------

- Problem-solving agents need an understanding of a goal to achieve
- Examples include checkmating the opponents king or arriving in at a particular destination

Problem Formulation
-------------------

- Agent comes up with a description of states and action to get to reach the goal
- This represents an abstract model for relevant part of the environment

Search
------

- Simulate sequences of actions without taking them in the real world
- Store sequences that reach the goal
- Select the optimal sequence

Execution
---------

- Execute the selected sequence of actions in turn to arrive at the goal

Open-loop
---------

- Open-loop - the proper solution is a fixed sequence of actions
- Actions can be executed ignoring percepts
- Closed-loop - the situation may change during execution and additional planning may be needed

Search Problem
--------------

- State space - Possible environment states
- Initial state - Starting state of agent
- Goal state - State representing success
- Actions - Set of possible actions from a given state
- Transition Model - Describes resultant state for an action
- Cost function - Measure of the value of a particular action in the model

Paths
-----

- Path - Sequence of actions
- Solution - a path that arrives at a goal state
- Optimal solution - lowest path cost solution

Graph
-----

- The search can be represented as a graph
- States are vertices
- Actions are edges
- Costs are edge weights

---

![Shortest Path From A to F](https://upload.wikimedia.org/wikipedia/commons/3/3b/Shortest_path_with_direct_weights.svg)

Abstraction
-----------

- It is important that we choose the right level of abstraction for our search
- Too much detail creates a larger search space
- Too little detail creates suboptimal solutions
