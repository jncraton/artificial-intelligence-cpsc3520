Game Theory
===========

Competitive Environments
------------------------

- Multi-agent - more than one system is making decisions
- Adversarial - the systems do not share the same goals

Stances
-------

1. Economy - consider agent decisions in aggregate
2. Environment - consider agents as random elements of the environment
3. Model opposing agent - treat the opposing agent as intelligent and consider their behavior

Simple games
------------

- Two player - only two agents
- Zero-sum - what is good for one player is bad for the other
- Perfect information - fully observable
- Turn-based

Formal Definition
-----------------

- $S_0$ - the initial state
- $Player(s)$ - the player whose turn it is in state `s`
- $Actions(s)$ - the set of legal moves in state `s`
- $Result(a, a)$ - transition model
- $IsTerminal(s)$ - True if game is over
- $Utility(s, p)$ - Assigns final score to player

Game Tree
---------

- We can convert the game model to a tree that can be searched

---

![Tic-tac-toe Tree](media/tic-tac-toe-tree.png)

State space
-----------

- Becomes large quickly
- A simple game like Tic-tac-toe includes 9! = 362,880 nodes
- Chess includes over $10^{40}$ nodes

Optimal Decisions
-----------------

- We need a way to define optimal decision in competitive environments

Minimax
-------

- We focus maximizing our utility for a worst case (maximum loss) scenario
- Our opponent is trying to minimize our utility
- Minimax decision leads to the state with the highest (from `max` point of view)  minimax value

---

![Minimax tree example](https://upload.wikimedia.org/wikipedia/commons/6/6f/Minimax.svg)

---

```python
def minimax(node, depth, maximizingPlayer):
  if node is terminal_node:
    return the heuristic value of node
  if maximizingPlayer:
    value = −∞
    for child in node:
      value = max(value, minimax(child, FALSE))
    return value
  else: # Minimizing player
    value = +∞
    for child in node:
      value = min(value, minimax(child, TRUE))
    return value
```

Minimax complexity
------------------

- Performs complete depth-first search
- Exponential time performance with the number of legal moves per turn and tree depth

Pruning
-------

Our search space will generally be too large to fully explore, so we will prune branches that are not work pursuing

---

How do we decide what to prune?
 
Pruning Decisions
-----------------

- Use a heuristic to determine who is winning in a given state
- Or simulate many games from that state and use the average to determine the quality of the state

Alpha-beta Pruning
------------------

- We can't fully avoid the exponential growth
- We can improve performance by not exploring branches that can have no impact on the outcome

---

![Alpha-beta Pruning](https://upload.wikimedia.org/wikipedia/commons/9/91/AB_pruning.svg)

---

```python
def alphabeta(node, depth, α, β, maximizingPlayer):
  if depth = 0 or node is terminal_node:
    return the heuristic value of node
  if maximizingPlayer:
    value = −∞
    for child in node:
      value = max(value, 
                  alphabeta(child, depth−1, α, β, FALSE))
      α = max(α, value)
      if α ≥ β then
        break (* β cutoff *)
    return value
  else:
    value = +∞
    for child in node:
      value = min(value,
                  alphabeta(child, depth−1, α, β, TRUE))
      β = min(β, value)
      if β ≤ α then
        break (* α cutoff *)
    return value
```

Forward pruning
---------------

- Prune nodes that appear less good based on a heuristic
- May not return optimal results

Beam search
-----------

- Type of forward pruning
- Consider only the top-n nodes based on a heuristic when searching
- Identical to breadth-first search when beam width is infinite

Weaknesses
----------

- Missing good moves that look weak in the present but play out favorably
- Pushing moves over the horizon
- [Move horizon example](https://lichess.org/editor/3p2k1/4p3/8/5K2/8/1N6/8/r1r5_b_-_-_0_1)

Lookup
------

- The first moves of a game are the most expensive to search
- As an optimization, we may simply choose to lookup the winningest first move from a database of games

Monte Carlo Tree Search
=======================

Go
--

- Turn-based game typically played on a 19x19 board
- Players take turns placing a stone on the board
- Goal it to surround more territory than your opponent

---

![Example Go Game](https://upload.wikimedia.org/wikipedia/commons/9/9f/Fineart_vs_Golaxy.gif)

Go complexity
-------------

- Hundreds of legal moves per turn
- Hundreds of total moves per game
- Total game tree complexity is approximately ${250}^{150}$ or ${10}^{360}$

Go Search
---------

- Search space is far too large even for a modest search depth
- e.g. searching 4 plies (player turns) ahead would be ${250}^4$ or 3.9 billion nodes
- Difficult to apply heuristics to determine who is winning a given position

Monte Carlo Method
------------------

- Algorithms that rely on random sampling to obtain results
- Used in physics, engineering, ray tracing, and applied statistics

Monte Carlo Tree Search
-----------------------

- Does not use heuristic evaluation
- Estimates the value of states by running simulations of complete games
- Average utility simply become win/loss percentage for simple games

Playout Policy
--------------

- How do we decide which moves to play in our simulations?
- Ideally, we would play optimal moves for both players, but if we knew these we wouldn't need MCTS
- Random moves can work for simple games

Pure Monte Carlo Search
-----------------------

- Runs `n` simulations for each legal move from the current game state
- Select the move with the highest expected utility
- Increasing `n` improves performance and requires additional compute

Selection Policy
--------------

- We can extend pure Monte Carlo search by exploring nodes that are more important
- Balance exploration and exploitation
- Exploration - getting more information for states with few playouts
- Exploitation - getting more information about states that have done well in past playouts

Search Tree Growth
------------------

1. Selection - Use selection policy to descend tree to leaf node
2. Expansion - Generate a new node
3. Simulation - Perform playout from new node
4. Backpropogation - Send results back up the tree

---

![Selection](media/mcts-selection.png){height=540px}

---

![Expansion and Simulation](media/mcts-expansion-simulation.png){height=540px}

---

![Backpropogation](media/mcts-backprop.png){height=540px}

MCTS Advantages
---------------

- No need for heuristic design
- Much smaller search tree compared to full search
- Can play games with only knowledge of the rules (simple form of reinforcement learning)
