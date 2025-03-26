Search Algorithms
================

---

A search algorithm takes as input a search problem and returns a valid solution

Process
-------

- Begin at the start state
- Expand the node by considering possible actions
- Generate a new node for each resultant state
- Continue this process

Frontier
--------

- Nodes in the search tree that have not been expanded
- A node that has been generated (whether expanded or not) has been **reached**

---

How do we decide which node to expand next as we search?

Best First Search
-----------------

- Choose the node with the minimal value for some evaluation function
- e.g. shortest distance to the final destination

Dijkstra's Algorithm
--------------------

- Best First Search using path cost as the evaluation function
- Also known as *Uniform-Cost Search* in AI and when the search graph is expanded on the fly

---

![Dijkstra's Algorithm](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif){height=540px}

Breadth First Search
--------------------

- Expand all nodes on the same level of the tree before moving to the next level
- Identical to best-first search using node depth as the evaluation function

Depth First Search
------------------

- Fully expand the first node before moving to the next
- May not return optimal solution

---

Why would we use depth first search?

Memory
------

- Depth first search requires linear rather than exponential memory
- Depth first search uses a very basic recursive algorithm

Depth-First Search
------------------

```
procedure DFS(G, v) is
    label v as reached
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as reached then
            recursively call DFS(G, w)
```

Performance
-----------

- Searching a nearly infinite space will take nearly infinite time
- Using highly optimized software can help
- Using very powerful hardware can help

Heuristics
----------

- It is often much more efficient to pursue a course that is good enough, but not optimal
- We can employ various metrics to determine whether a course is likely to result in a positive outcome
- A heuristic is **admissible** if it never overestimates the cost of reaching the goal (the estimate won't cause us to miss the shortest path)

A*
---

---

![A* with 0 heuristic (uniform cost search)](https://upload.wikimedia.org/wikipedia/commons/2/23/Dijkstras_progress_animation.gif){height=540px}

---

![A* with admissible heuristic](https://upload.wikimedia.org/wikipedia/commons/5/5d/Astar_progress_animation.gif){height=540px}

---

![A* with inadmissible heuristic](https://upload.wikimedia.org/wikipedia/commons/8/85/Weighted_A_star_with_eps_5.gif){height=540px}
