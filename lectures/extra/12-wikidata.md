Wikidata
========

Wikipedia
---------

- Encyclopedia that anyone can edit
- Over 300 editions of Wikipedia in different languages
- A single factual update requires editors to change 300 pages

---

> Wikidata is a collaboratively edited multilingual knowledge graph

> document-oriented database, focused on items, which represent topics, concepts, or objects

Entities
--------

- Identified by a unique id
- Description
- Optional aliases
- Statements

Claims
------

- Map values to properties of an entity
- Organized in groups of values mapped to properties
- Qualifiers determine when claims are applicable

Statements
----------

- Claims that include references
- Include rank to distinguish between multiple claims for the same property

Snak
----

> refers to the combination of a property and either a value or one of the special cases "no value" and "unknown value". Snaks can be found in claims (then they are called main snaks) or in qualifiers as part of statements (then they are called qualifier snaks)

---

![Data Model](https://upload.wikimedia.org/wikipedia/commons/a/ae/Datamodel_in_Wikidata.svg){height=540px}

---

Database size?

---

Over 90 million entities

---

~90GB gzipped json as of 2021

More Information
----------------

- [Introduction](https://www.wikidata.org/wiki/Wikidata:Introduction)
- [Glossary](https://www.wikidata.org/wiki/Wikidata:Glossary)

API
---

- [Search example](https://www.wikidata.org/w/api.php?action=wbsearchentities&search=Anderson%20University&language=en)
- [Entity JSON example](https://www.wikidata.org/wiki/Special:EntityData/Q4754216.json)
