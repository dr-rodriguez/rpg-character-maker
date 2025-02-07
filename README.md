# Ollama RPG Character Maker

A proof-of-concept python program that calls Ollama to generate characters suitable for a TTRPG. 

Ollama allows you to run LLM models locally. For more information, and to download other models, go to https://ollama.com/

## Windows and Conda

To activate the conda environment in windows, you may need to do something like:
```bash
D:\\Anaconda3\\Scripts\\activate.bat D:\\PycharmProjects\\ollama-rpg\\.conda
```
Then you can use pip to add any dependencies.

## Increasing Context Size

This will use more resources but allow the LLM to retain more information for context.

```bash
ollama run llama3.2:3b
/set parameter num_ctx 8192
/save llama3.2:3b-8k
ollama serve
```

## Example Use

```python
from character import Character, SPECIES, CLASSES

c = Character(model="llama3.2:3b-8k")

c.species = random.choice(SPECIES)
c.class_name = random.choice(CLASSES)

names = c.generate_random_names()
c.name = random.choice(names)

concepts = c.generate_random_concepts()
c.concept = random.choice(concepts)

traits = c.generate_personality_traits()
c.personality_traits = traits

flaws = c.generate_random_flaws()
c.flaw = random.choice(flaws)

conflict = c.generate_conflict()
c.conflict = conflict

backstory = c.generate_backstory()
c.backstory = backstory

print("\n\nCharacter Summary:\n")
print(c.get_character())
```

## Example Generations

```
Name: Lyra Moonwhisper
Species: Changeling
Class: Barbarian
Concept: Swift (Quick) Fox who Never Says No to Snacks
Personality Traits:
  * Cunning: Always looks for an angle, never turns down a challenge.
  * Quick-Witted: Can talk her way out of (or into) almost any situation.
  * Opportunistic: Sees snacks and opportunities as one and the same.
  * Mischievous: Loves to stir up trouble, just to see how far it will get her.
  * Enthusiastic: Will try anything once, if only for the thrill of it.
Flaw: 
  Lack of Trust: Lyra's Mischievous nature can make it difficult for her to trust others, leading her to question motives and loyalty. This lack of trust can put her at odds with those she cares about.  
Conflict:
  Lyra Moonwhisper's nomadic tribe was betrayed by a trusted friend, who sold them out to a rival clan in exchange for a stash of rare, magical pastries - Lyra's mischievous nature initially saw this as an opportunity, but her lack of trust ultimately left her feeling isolated and vengeful.
Backstory:
  Lyra Moonwhisper's tribe was once a nomadic collective of Changelings who roamed the land in search of adventure and the next great feast. Lyra, ever the cunning fox, had an insatiable appetite for both physical challenges and sweet treats. Her tribe's leader, a wise and witty elder named Kael, saw potential in Lyra's mischievous nature and encouraged her to hone it into a tool for their survival. "A quick wit can get you out of any mess," he'd say, and Lyra learned to use her words like a dagger, always looking for the angle that would serve her and her tribe.

But when Kael was betrayed by a trusted friend who sold them out to a rival clan in exchange for a stash of rare pastries - a deal that sealed their fate as nomads forever - Lyra's lack of trust turned into a festering wound. She saw the very thing she had been trained to exploit - the opportunity for power and snacks - turn against her, leaving her tribe vulnerable. Now, Lyra travels the land alone, using her cunning and wit to survive, but always on guard against those who would seek to take advantage of her trustless nature. Her concept of "snacks" has broadened to include any opportunity or connection that might lead to safety - and she'll stop at nothing to claim it.
```