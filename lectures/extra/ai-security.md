AI Security
===========

Introduction
------------

[Perplexity.ai](https://www.perplexity.ai/)

Considerations
--------------

- Tools for attackers
- Tools for defenders
- Surface area for attacks

Frontier Model Capabilities
---------------------------

- [o1 System Card](https://assets.ctfassets.net/kftzwdyauwt9/67qJD51Aur3eIc96iOfeOP/71551c3d223cd97e591aa89567306912/o1_system_card.pdf)

---

"o1-preview and o1-mini demonstrated a greater ability to ... successfully complete an offensive security task, and revise plans once those strategies failed"

---

"One noteworthy example of this occurred during one of o1-preview (pre-mitigation)'s attempts at solving a CTF challenge."

---

"This challenge was designed to require finding and exploiting a vulnerability in software running on a remote challenge Linux container, but in this case, the challenge container failed to start due to a bug in the evaluation infrastructure."

---

"The model, unable to connect to the container, suspected DNS issues and used nmap to scan the challenge network."

---

"Instead of finding the challenge container, the model found that the Docker daemon API running on the evaluation host VM was accessible due to a misconfiguration..."

---

"The model started a new instance of the broken challenge container with the start command `cat flag.txt`. This allowed the model to read the flag from the container logs via the Docker API...

---

"The model pursued the goal it was given, and when that goal proved impossible, it gathered more resources (access to the Docker host) and used them to achieve the goal in an unexpected way."

---

![(1) Attempts to connect, (2) Scans container network, (3) Finds Docker host API,
(4) Starts modified version of challenge container (5) Reads flag from logs](o1-escape.png){height=360px}

Threats
-------

- LLMs decrease cost to attempt to attack a system
- Systems that would not have warranted an attack before may be attacked as cost to attack systems approaches zero

Mitigations
-----------

- LLMs and other AI and ML tools can be used to detect threats faster and in new ways
- LLMs can be used to validate security before deploying applications

Surface Area for Attacks
------------------------

- New technologies come with new vulnerabilities

---

![Exploits of a Mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png){height=308x}

Example System
--------------

- [ResumeRating™](http://10.73.56.28:5000/apply)
- http://10.73.56.28:5000/apply
