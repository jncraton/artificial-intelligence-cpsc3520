Vectors
=======

Vector
------

- Object with length and direction

---

![Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg)

Components
----------

- Often defined as a tuple of components that act as multipliers against basic vectors

---

![Vector Components](https://upload.wikimedia.org/wikipedia/commons/f/fd/3D_Vector.svg){height=540px}

Basis
-----

- We commonly use the standard basis to represent vectors
- The standard basis vectors will have all components equal to zero, which the exception of one value that is one
- Standard basis vectors are therefore unit vectors

---

![Change of Basis](https://upload.wikimedia.org/wikipedia/commons/f/f4/3d_two_bases_same_vector.svg){height=540px}

Vector Addition
---------------

- We can add two vectors by simply adding their components (assuming the same basis)

---

![Vector Addition](https://upload.wikimedia.org/wikipedia/commons/2/28/Vector_addition.svg){height=540px}

Vector Magnitude
----------------

- Provides the length of the vector as a scalar
- Also know as the Euclidean norm
- $\|a\| = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}$

Vector Multiplication
---------------------

- There are many ways to apply a multiplication operation to vectors

Scalar Multiplication
---------------------

- Multiply each component of the vector by a scalar
- This changes the length of the vector
- This does not change the direction of the vector

---

![Scalar multiplication](https://upload.wikimedia.org/wikipedia/commons/f/fa/Scalar_multiplication_by_r%3D3.svg)

Dot Product
-----------

- Sums the product of each vector component
- $a \cdot b=\sum_{i=1}^n a_i{b}_i={a}_1{b}_1+{a}_2{b}_2+\cdots+{a}_n{b}_n$
- $a \cdot b=\|a\|\ \|b\|\cos\theta$

Cosine Similarity
-----------------

- One measure for similarity between vectors is the angle between them
- One way to calculate this angle is by using the dot product and vector magnitude
- $\cos(\theta) = {a \cdot b \over \|a\| \|b\|}$
- Note that for unit vectors cosine similarity is the same as the dot product

Vector Magnitude
----------------

- With an understanding of the dot product, we have a new way to define magnitude
- $\|a\| = \sqrt{a \cdot a}$

---

[Python Example](https://repl.it/@jncraton/vector#main.py)

Applications
------------

- Physics
- Lighting
- SVG
