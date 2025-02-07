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
For this package, you are unlikely to need to do this.

```bash
ollama run llama3.2:3b
/set parameter num_ctx 8192
/save llama3.2:3b-8k
ollama serve
```

## Example Use

```python
from character import Character, SPECIES, CLASSES

c = Character(model="llama3.2:3b")

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

```
Name: Kaelin Darkshadow
Species: Hadozee
Class: Sorcerer
Concept: A charming (and cunning) thief who uses magic to swipe valuable items, but always seems to end up with a bunch of useless junk instead.
Personality Traits:
  * Kaelin's got a silver tongue
  * Always looks for the angle
  * Charming to strangers, paranoid to friends
  * Loves shiny things, hates practicality
  * Wants out, but never pays up
Flaw:
  Inconsistent Magic Control: Kaelin's sorcery is prone to unpredictable bursts of energy, which can result in either brilliant successes or disastrous accidents.
Conflict:
  Kaelin Darkshadow is haunted by a series of unfortunate escapades where his unpredictable magic has turned his ill-gotten gains into worthless trinkets, forcing him to flee from creditors and former "acquaintances" who still demand payment, leading him to seek adventure as a way to fund his next big score.
Backstory:
  Kaelin Darkshadow's past is a tapestry of quick fixes and hasty escapes. Born into a family of minor nobility, Kaelin was always drawn to the finer things in life - but with no discernible talent for politics or diplomacy, he turned to his natural charisma and cunning to make a name for himself on the streets. He honed his skills as a thief, using magic to augment his thieving abilities, but soon found that his unpredictable bursts of energy were more likely to turn valuable artifacts into worthless trinkets than bring him wealth.

  As his luck - or lack thereof - continued to falter, Kaelin's creditors began to close in. The memory of one particularly disastrous heist, where a magical item meant to grant eternal youth turned out to be nothing more than a cheap perfume bottle and a pair of stained socks, still haunted him. With a dwindling purse and a growing list of enemies, Kaelin saw no other option but to seek his fortune in the wider world, taking on odd jobs and playing the part of a charming thief to make ends meet. But deep down, he longed for something more - a big score that would finally set him free from his cycle of debt and disappointment, and let him live the life of luxury he truly deserved.
```

```
Name: Pixel Ironfist
Species: Goblin
Class: Wizard
Concept: A fierce, pint-sized warrior who wields a massive, oversized sword
Personality Traits:
  * Brutal: Unapologetically forceful in combat and always up for a fight.
  * Childlike: Possesses an unshakeable sense of wonder and curiosity, often leading to mischief.
  * Fierce: Willing to defend allies with overwhelming ferocity.
  * Hot-Headed: Prone to outbursts of rage when provoked or frustrated.
  * Unyielding: Completely dedicated to his craft as a warrior-wizard, refusing to back down from a challenge.
Flaw:
   Lack of Focus: Struggles to maintain concentration in prolonged study sessions, often losing track of his research or neglecting important details.
Conflict:
  Pixel Ironfist's obsessive quest for a ancient tome of forbidden magic was foiled when he inadvertently destroyed his own research notes in a fit of rage after losing focus during an intense study session, forcing him to flee the library and seek out new knowledge - or face the wrath of his patron deity.
Backstory:
  Pixel Ironfist was born in the depths of the Goblin Warrens, where his people had honed their warrior skills for centuries. From a young age, he demonstrated an unnatural aptitude for magic, which only fueled his already fierce temper. As a child, Pixel would often sneak into the warren's armory to practice with oversized swords, much to the chagrin of his elders. They deemed such frivolity unworthy of a true goblin warrior, but Pixel saw it as a calling. His parents, both respected warriors in their own right, recognized their son's potential and began teaching him the arcane arts.

  Tragedy struck when Pixel was just a teenager. During an intense study session, he became frustrated with his research and lashed out at the ancient tome on forbidden magic that had become his obsession. In a fit of rage, he destroyed the notes detailing his research, rendering his progress all but worthless. The incident sent Pixel fleeing from the library, pursued by the wrath of his patron deity, Gorthok the Unyielding. This banishment marked the beginning of Pixel's nomadic existence, driven by an insatiable hunger for knowledge and a fierce determination to reclaim his lost research. His travels have taken him to the farthest reaches of the realm, where he seeks out new sources of power and confronts those who would seek to control him. The oversized sword at his side is a constant reminder of his unyielding resolve and ferocity in battle.
```
