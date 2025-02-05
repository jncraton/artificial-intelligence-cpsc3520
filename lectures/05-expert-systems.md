# Expert Systems

## What are Expert Systems?

- AI systems that mimic human decision making
- Use knowledge and reasoning to solve complex problems

## Key Components

- **Knowledge Base**: Stores facts and rules
- **Inference Engine**: Applies rules to facts to derive new knowledge

## History

- Developed in the 1970s and 1980s
- Pioneered by researchers like Edward Feigenbaum

## MYCIN

- Early backward chaining expert system
- Diagnosed bacterial infections
- Recommended antibiotics
- Achieved 65% accuracy, better than some human experts

## Example Rule

```lisp
(defrule 52
 if (site culture is blood)
  (gram organism is neg)
  (morphology organism is rod)
  (burn patient is serious)
 then .4
  (identity organism is pseudomonas))
```

## How They Work

- **Forward Chaining**: Start with known facts, apply rules to derive new facts
- **Backward Chaining**: Start with a goal, work backward to find supporting facts

## Forward Chaining Example

```python
rules = {
    "R1": {"if": "A", "then": "B"},
    "R2": {"if": "B", "then": "C"}
}

facts = ["A"]

def forward_chain(rules, facts):
    while True:
        new_facts = []
        for rule in rules.values():
            if rule["if"] in facts and rule["then"] not in facts:
                new_facts.append(rule["then"])
        if not new_facts:
            break
        facts.extend(new_facts)
    return facts

print(forward_chain(rules, facts))
```

## Backward Chaining Example

```python
rules = {
    "R1": {"if": "A", "then": "B"},
    "R2": {"if": "B", "then": "C"}
}

goal = "C"

def backward_chain(rules, goal, facts):
    if goal in facts:
        return True
    for rule in rules.values():
        if rule["then"] == goal:
            if backward_chain(rules, rule["if"], facts):
                return True
    return False

facts = ["A"]
print(backward_chain(rules, goal, facts))
```

---

![Backward chaining](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/BackwardChaining_David_C_England_1990_p21.gif/640px-BackwardChaining_David_C_England_1990_p21.gif)

## Limitations

- **Scalability**: Difficult to manage large knowledge bases
- **Maintenance**: Requires frequent updates and expert knowledge
- **Flexibility**: Limited to predefined rules and facts

## Modern Applications

- **Medical Diagnosis**: IBM Watson for Oncology
- **Financial Services**: Fraud detection systems
- **Customer Support**: Chatbots and virtual assistants

---

What are the key differences between expert systems and machine learning?

---

How do expert systems handle uncertainty and incomplete information?

---

What are some potential ethical concerns with using expert systems in critical domains?
