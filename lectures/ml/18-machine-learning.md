Machine Learning
================

---

Creating algorithms that improve automatically and learn from seeing new data.

Applications
------------

- Game playing
- NLP
- Computer vision
- Speech recognition
- Language models

Object Classification
---------------------

- Model that takes an image as input and returns a list of likely classes (or labels) for that image

MNIST
-----

- Database of labeled handwritten digits
- Labeled data means that **supervised learning** can be applied
- MNIST has become a "Hello, world" of sorts for ML algorithms

---

![MNIST Sample](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

MNIST Results
-------------

- Simple linear classifiers can achieve a ~10% error rate
- More complex models such as boosted tree and SVN can achieve an error rate of ~1%
- Deep neural net models can achieve an error rate of ~.25%

Big Idea
--------

- Labeled data is provided for training and testing
- Models are create to map an input to an output
- Models have parameters (weights) that can be updated as the data is examined

Object Detection
----------------

- The ability to detect objects in images is useful in many areas
- Self-driving, machine translation, machine reading, etc
- Models take images as input and return locations and labels for objects

---

![Object Detection](https://upload.wikimedia.org/wikipedia/commons/3/3b/Computer_vision_sample_in_Sim%C3%B3n_Bolivar_Avenue%2C_Quito.jpg)

Google Translate example
------------------------

Self-driving
------------

- Combines many ML tools to create a complete automated driving experience
- Takes images (and/or) Lidar as input and provides driving actions

---

[Tesla Self-driving example](https://www.youtube.com/watch?v=tlThdr3O5Qo)

---

[Autopilot with annotations](https://www.youtube.com/watch?v=_1MHGUC_BzQ)

Language Models
---------------

- Predict the next token in a text sequence
- Trained on a large corpus of text
- State-of-the-art models require deep knowledge of languages and the world

GPT-2 Example
-------------

```python3
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import time
import sys

torch.set_num_threads(12)

start_time = time.perf_counter()

def log(text):
    current_ms = int((time.perf_counter() - start_time) * 1000)
    print(f"{current_ms}ms {text}")

model_name = 'gpt2-medium'

log(f"Loading {model_name} tokenizer...")
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

log(f"Loading {model_name}...")
model = GPT2LMHeadModel.from_pretrained(model_name)
log(f"{model_name} Loading complete.")

model.eval()

while(1):
    temperature = input("Temperature:") or .8
    top_k = input("Top k:") or 5
    prompt_text = input("Prompt:")

    encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")

    for i in range(64):
        generated_sequences = model.generate(
            input_ids = encoded_prompt,
            max_length = len(encoded_prompt[0]) + 1,
            temperature = float(temperature),
            repetition_penalty=1.5,
            top_k=int(top_k),
            top_p=1.0,
            do_sample=False,
            num_return_sequences=1,
            pad_token_id = 50256, # EOS
        )

        generated_sequence = generated_sequences[0].tolist()

        # Decode text
        text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)

        # Add the prompt at the beginning of the sequence. Remove the excess text that was used for pre-processing
        print(text[len(tokenizer.decode(encoded_prompt[0], clean_up_tokenization_spaces=True)) :], end='')
        sys.stdout.flush()

        if "<|endoftext|>" in text:
            break

        # TODO: there's probably a way to avoid re-encoding here
        encoded_prompt = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

    print("")
    log("Generation complete")
```

GPT-3 Example
-------------

Image Synthesis
---------------

- Text to image model
- An input text is provided, and the model returns a set of likely images that best match the text.

---

![giraffe dragon chimera](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/DALL-E_sample.png/499px-DALL-E_sample.png)

More examples
-------------

[DALL-E blog post](https://openai.com/blog/dall-e/)

---

What is the possible economic impact of a system like DALL-E?

Robotics
--------

- Machines can learn to perform tasks
- Tasks can be learned from examples and experience

---

[Boston Dynamics Atlas](https://www.youtube.com/watch?v=fRj34o4hN4I)
