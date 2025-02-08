# Tests for character.py

import pytest
from character import Character

@pytest.fixture
def character():
    return Character()

def test_set_character_from_string(character):
    character.set_character_from_string("""Name: Lyra Moonwhisper
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
Additional Details:
  Lyra is a master of disguise, able to blend in with any crowd or environment.""")
    assert character.name == "Lyra Moonwhisper"
    assert character.species == "Changeling"
    assert character.class_name == "Barbarian"
    assert character.concept == "Swift (Quick) Fox who Never Says No to Snacks"
    assert character.personality_traits == [
        "Cunning: Always looks for an angle, never turns down a challenge.",
        "Quick-Witted: Can talk her way out of (or into) almost any situation.",
        "Opportunistic: Sees snacks and opportunities as one and the same.",
        "Mischievous: Loves to stir up trouble, just to see how far it will get her.",
        "Enthusiastic: Will try anything once, if only for the thrill of it."
        ]
    assert character.flaw == "Lack of Trust: Lyra's Mischievous nature can make it difficult for her to trust others, leading her to question motives and loyalty. This lack of trust can put her at odds with those she cares about."
    assert character.conflict == "Lyra Moonwhisper's nomadic tribe was betrayed by a trusted friend, who sold them out to a rival clan in exchange for a stash of rare, magical pastries - Lyra's mischievous nature initially saw this as an opportunity, but her lack of trust ultimately left her feeling isolated and vengeful."
    assert character.backstory == """Lyra Moonwhisper's tribe was once a nomadic collective of Changelings who roamed the land in search of adventure and the next great feast. Lyra, ever the cunning fox, had an insatiable appetite for both physical challenges and sweet treats. Her tribe's leader, a wise and witty elder named Kael, saw potential in Lyra's mischievous nature and encouraged her to hone it into a tool for their survival. "A quick wit can get you out of any mess," he'd say, and Lyra learned to use her words like a dagger, always looking for the angle that would serve her and her tribe.

But when Kael was betrayed by a trusted friend who sold them out to a rival clan in exchange for a stash of rare pastries - a deal that sealed their fate as nomads forever - Lyra's lack of trust turned into a festering wound. She saw the very thing she had been trained to exploit - the opportunity for power and snacks - turn against her, leaving her tribe vulnerable. Now, Lyra travels the land alone, using her cunning and wit to survive, but always on guard against those who would seek to take advantage of her trustless nature. Her concept of "snacks" has broadened to include any opportunity or connection that might lead to safety - and she'll stop at nothing to claim it.
"""
    assert character.additional_details == "Lyra is a master of disguise, able to blend in with any crowd or environment."