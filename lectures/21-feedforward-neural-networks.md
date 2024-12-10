Feedforward Neural Networks
===========================

Logistic Regression
-------------------

- Provides a powerful tool for learning relationships between input features and outputs
- Is not able to learn all functions

XOR
---

A   B   Q
--- --- ---
0   0   0
0   1   1
1   0   1
1   1   0

---

XOR can't be effectively learned by logistic regression.

---

How could we enhance logistic regression to learn XOR?

---

- The challenging case can be viewed as returning 0 when both inputs are 1.
- What if we add a variable to our model to account for this?
- Let's add a value H that is A&B

---

A   B   H   Q
--- --- --- ---
0   0   0   0
0   1   0   1
1   0   0   1
1   1   1   0

---

Could logistic regression now learn XOR given A, B, and H as input?

---

Yes.

- A and B would have positive weights
- H would have a large negative weight that can overcome the weights of A and B

---

- This should feel like cheating
- However, what if we used logistic regression to learn H?
