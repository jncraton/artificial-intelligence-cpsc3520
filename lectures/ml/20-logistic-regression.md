Logistic Regression
===================

Logistic Regression
-------------------

Statistical model to predict the likelihood of an event from known data

Logistic Function
-----------------

$f(x) = \frac{1}{1 + e^{-k(x-x_0)}}$

---

![Logistic Function](https://upload.wikimedia.org/wikipedia/commons/8/88/Logistic-curve.svg)

Fitting
-------

- Least squares is not meaningful for logistic regression
- We are dealing with probabilities of events, not a simple value

---

![Logistic Regression Example](https://upload.wikimedia.org/wikipedia/commons/6/6d/Exam_pass_logistic_curve.jpeg)

Maximum Likelihood Estimation
-----------------------------

- We have a set of examples, $X=\{x_1, x_2,...x_n\}$, drawn independently from a data generation probability distribution $p_{data}(x)$

$\theta_{ML} = \underset{\theta}{\operatorname{arg\;max}}\ p_{model}(X; \theta)$

Maximum Likelihood Estimation
-----------------------------

We want to select model parameters that minimize the dissimilarity between our model and our data

---

[More info (section 5.5)](http://www.deeplearningbook.org/contents/ml.html)

Iterative Solving
-----------------

- We fit our model iteratively


Logistic Regression in Python
-----------------------------

```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

clf.fit(X. y)
```

Pure Python Example
-------------------

Linear Separability
-------------------

- Points in classes can be separated by a hyperplane
- A hyperplane is simply a space with one less dimension than its ambient space
- A line is a hyperplane of two dimensions, a plane is a hyperplane of 3 dimensions, etc

---

![Linearly separable](https://upload.wikimedia.org/wikipedia/commons/b/b8/VC2.svg)

---

![Not linearly separable](https://upload.wikimedia.org/wikipedia/commons/3/37/VC4.svg)

