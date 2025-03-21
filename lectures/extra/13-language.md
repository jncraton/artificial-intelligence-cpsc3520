Language
========

Chomsky Hierarchy
-----------------

Grammar       Automaton (Computer)
------------- ----------------------
Unrestricted  Turing Machines
Context Free  Pushdown Automata
Regular       Finite State Automata

Regular Languages
-----------------

- Are insufficient to parse most programming languages
- Are useful for parsing tokens
- Can be processed by a simple finite automaton

Deterministic Finite Automaton (DFA)
------------------------------------

- Finite set of states $Q$
- Finite set of input symbols called the alphabet $\Sigma$
- Transition function $\delta : Q \times \Sigma \rightarrow Q$
- Initial or start state $q_0 \in Q$
- Set of accept states $F \subseteq Q$

Drawing DFAs
------------

- States are nodes on the graph
- Start state indicated by arrow
- Accept states indicated by double border
- Transitions indicated as labeled arrows

---

![DFA to accept string containing an even number of zeroes](https://upload.wikimedia.org/wikipedia/commons/9/9d/DFAexample.svg){height=540px}

Regular Expressions
-------------------

A string used as a search pattern for a member of a regular language.

DFA RE Equivalence
------------------

- A DFA can be created to match any regular expression
- A regular expression can be created to match a language accepted by any DFA

---

![Pumping Lemma for Regular Languages](https://upload.wikimedia.org/wikipedia/commons/f/f5/Pumping-Lemma_xyz_svg.svg){height=360px}

Context-free Languages
----------------------

Big Idea
--------

- Grammar rules are applied recursively to generate members of the language.
- Grammar rules can be applied in reverse to parse a string to determine language membership.
- The parsing process can result in a parse tree showing token structure.

English Example
---------------

- S -> NP VP
- NP -> Adj Noun
- NP -> Noun
- VP -> Verb Adv
- VP -> Verb

---

![Parse tree](https://connectiongrammar.netlify.com/docs/english-parse-example.png)

Implementing a parser
---------------------

---

![Parse tree example](https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Parse_Tree_Example.svg/525px-Parse_Tree_Example.svg.png)


Top-down parsing
----------------

- Begins with overall structure (sometimes guessed or assumed) and then determines details
- Top-down refers to order in which nodes in the final parse tree are determined

---

![Top-down parse](https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Top-down_Parse_Tree_Order.svg/495px-Top-down_Parse_Tree_Order.svg.png)

Bottom-up parsing
-----------------

- Determines low-level details first then builds our surrounding structure.

---

![Bottom-up parse](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Bottom-up_Parse_Tree_Order.svg/512px-Bottom-up_Parse_Tree_Order.svg.png)

Shift-reduce parsing
--------------------

- Bottom-up
- Shifts tokens onto a stack
- Reduces them when they match against a rule

LR Parsing
----------

- Shift-reduce, bottom-up parse
- Left-to-right, Rightmost derivation first
- Deterministic algorithm
- Linear time performance

Parsing English
---------------

> The horse raced past the barn fell.

---

> The old man the boats.

Punctuation
-----------

> A woman, without her man, is nothing.

---

> A woman: without her, man is nothing.

Inflection
----------

> I didn't say you stole my money.

Context Sensitivity
-------------------

> Alice is a good student, so she earns good grades.

---

> Alice is a good student, so it earns good grades.
