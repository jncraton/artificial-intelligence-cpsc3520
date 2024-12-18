Recurrent Neural Network
========================

---

![Recurrent Neural Network](https://upload.wikimedia.org/wikipedia/commons/b/b5/Recurrent_neural_network_unfold.svg)

Properties
----------

- First implemented in the 1970s
- RNNs naturally maintain state over time
- Have difficulties with long-range dependencies
- Difficult to parallelize and scale

LSTM
====

RNN Weaknesses
--------------

- Difficult to scale
- Long term relationships vanish

Long Short-term Memory
----------------------

- Memory cells can be added to RNNs to remember long-term relationships
- First demonstrated in 1995

Uses
----

- SotA approach for many tasks from ~2009-2019
- Machine Translation
- Language Modelling
- Game playing (Dota 2, StarCraft 2)

Transformers
============

Properties
----------

- First published in 2017
- Solves the long-range dependency issue in RNNs
- Solves the parallelization issues of RNNs
- Achieves SotA results on many ML tasks, starting with translation

---

![Transformer Architecture ([Attention is All you Need](https://arxiv.org/pdf/1706.03762.pdf))](media/transformer.png){height=540px}

---

Attention
---------

---

![Scaled Dot-product Attention](media/scaled-dot-product-attention.png)

---

![Multihead Attention](media/multihead-attention.png)

Self-attention Advantages
-------------------------

- Reduced computational complexity per layer
- Increased parallelism
- Reduced path length for long-range dependencies

---

![GPT-1 Decoder-only Transformer](media/gpt1.png){height=540px}

Sampling
--------

Temperature
-----------

- Adjusts all probabilities to tune output sampling
- 0.0 to 1.0
- 0.0 is greedy sampling
- 1.0 creates more variety

Top K
-----

- Will only select from the top K tokens
- Tokens will still be weighted using their probability

Top P
-----

- Will only select from the top tokens whose probabilities sum to P
- Tokens will still be weighted using their probability

Open-ended Generation
---------------------

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")

prompt = "def hello_world():"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

completion = model.generate(input_ids, max_new_tokens=8, pad_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(completion[0]))
```

Translation
-----------

```
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

prompt = "translate English to German: How old are you?"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
```
