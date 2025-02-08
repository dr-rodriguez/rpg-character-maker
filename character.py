import random
import re

from ollama import chat

MODEL = "llama3.2:3b"
SPECIES = [
    "Human",
    "Elf",
    "Dwarf",
    "Halfling",
    "Orc",
    "Goblin",
    "Tiefling",
    "Dragonborn",
    "Half-Elf",
    "Half-Orc",
    "Aasimar",
    "Gnome",
    "Firbolg",
    "Tabaxi",
    "Triton",
    "Genasi",
    "Kenku",
    "Lizardfolk",
    "Kobold",
    "Aarakocra",
    "Goliath",
    "Tortle",
    "Changeling",
    "Shifter",
    "Warforged",
    "Centaur",
    "Loxodon",
    "Hadozee",
    "Giff",
    "Thri-Kreen",
    "Githzerai",
    "Githyanki",
]
CLASSES = [
    "Artificer",
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard",
]


def clean_response(response: dict) -> str:
    """Clean the response from the chat function."""
    raw_text = response["message"]["content"]
    cleaned_content = re.sub(r"<think>.*?</think>", "", raw_text, flags=re.DOTALL)
    cleaned_content = cleaned_content.lstrip().rstrip()
    return cleaned_content


class Character:
    def __init__(
        self,
        name: str = None,
        species: str = None,
        class_name: str = None,
        concept: str = None,
        personality_traits: list[str] = [],
        flaw: str = None,
        conflict: str = None,
        backstory: str = None,
        additional_details: str = None,
        model: str = MODEL,
    ):
        # Character parameters
        self.name = name
        self.species = species
        self.class_name = class_name
        self.concept = concept
        self.personality_traits = personality_traits
        self.flaw = flaw
        self.conflict = conflict
        self.backstory = backstory
        self.additional_details = additional_details

        # Model parameters
        self.model = model
        self.base_context = """
        You are designing characters appropriate for a table top role-playing game, 
        such as Dungeons and Dragons. 
        You are creative, yet concise in your responses. 
        In your responses, you do not need to explain how it all fits together, just provide the raw material.\n"""

    def reset_character(self):
        """Reset the character to default values."""
        self.name = None
        self.species = None
        self.class_name = None
        self.concept = None
        self.personality_traits = []
        self.flaw = None
        self.conflict = None
        self.backstory = None
        self.additional_details = None

    def get_character(self):
        """Return the character's information as a string."""
        character_info = ""

        if self.name is not None:
            character_info += f"Name: {self.name}\n"
        if self.species is not None:
            character_info += f"Species: {self.species}\n"
        if self.class_name is not None:
            character_info += f"Class: {self.class_name}\n"
        if self.concept is not None:
            character_info += f"Concept: {self.concept}\n"
        if self.personality_traits:
            character_info += "Personality Traits:\n" + "".join(
                [f"  * {x}\n" for x in self.personality_traits]
            )
        if self.flaw is not None:
            character_info += f"Flaw: \n  {self.flaw}\n"
        if self.conflict is not None:
            character_info += f"Conflict: \n  {self.conflict}\n"
        if self.backstory is not None:
            character_info += f"Backstory: \n  {self.backstory}\n"
        if self.additional_details is not None:
            character_info += f"Additional Details: \n  {self.additional_details}\n"

        return character_info

    def enhanced_context(self):
        """Enhance the context for the character."""
        if self.get_character() == "":
            return self.base_context
        else:
            return (
                self.base_context
                + "Use the following context for the character:\n"
                + self.get_character()
            )

    def generate_random_concepts(
        self,
        num: int = 5,
        extra="Include a funny twist for each.",
        use_full_context=True,
    ) -> list[str]:
        """Generate random concepts for the character."""
        context = self.enhanced_context() if use_full_context else self.base_context

        messages = [
            {
                "role": "system",
                "content": context,
            },
            {
                "role": "user",
                "content": f"""
                Generate a list of {num} character concepts. Use * as the bullets.
                These should be of the form "* A(n) (adjective) (noun) who (verb phrase)". 
                Do not generate any names or backstories at this point. 
                Avoid using the species or class in the concept. 
                {extra}
                """,
            },
        ]

        print("\nGenerating random concepts...")
        response = chat(
            model=self.model,
            messages=messages,
        )

        concepts = clean_response(response)
        print(concepts)

        # Extract concepts that start with an asterisk
        concept_list = [
            trait.strip()[1:].strip().replace("*", "")
            for trait in concepts.split("\n")
            if trait.strip().startswith("*")
        ]

        return concept_list

    def generate_personality_traits(
        self, num: int = 5, extra="", use_full_context=True
    ) -> list[str]:
        """Generate personality traits for the character."""
        context = self.enhanced_context() if use_full_context else self.base_context

        messages = [
            {
                "role": "system",
                "content": context,
            },
            {
                "role": "user",
                "content": f"""
            Generate a bulleted list of {num} personality traits. Use * as the bullets.
            These should be adjectives or short phrases of the form "* Trait: Description."
            {extra}
            """,
            },
        ]

        print("\nGenerating random personality traits...")
        response = chat(
            model=self.model,
            messages=messages,
        )

        traits = clean_response(response)
        print(traits)

        # Extract traits that start with an asterisk
        trait_list = [
            trait.strip()[1:].strip().replace("*", "")
            for trait in traits.split("\n")
            if trait.strip().startswith("*") and trait.strip()[1:].strip().replace("*", "") != ""
        ]

        return trait_list

    def generate_random_flaws(
        self, num: int = 5, extra="", use_full_context=True
    ) -> list[str]:
        """Generate random flaws for the character."""
        context = self.enhanced_context() if use_full_context else self.base_context

        messages = [
            {
                "role": "system",
                "content": context,
            },
            {
                "role": "user",
                "content": f"""
            Generate a bulleted list of {num} character flaws. Use * as the bullets.
            These should be of the form "* Flaw: Description."
            {extra}
            """,
            },
        ]

        print("\nGenerating random flaws...")
        response = chat(
            model=self.model,
            messages=messages,
        )

        flaws = clean_response(response)
        print(flaws)

        # Extract flaws that start with an asterisk
        flaw_list = [
            flaw.strip()[1:].strip().replace("*", "").replace("Flaw: ", "")
            for flaw in flaws.split("\n")
            if flaw.strip().startswith("*")
        ]

        return flaw_list

    def generate_conflict(self, extra=""):
        """Generate a conflict for the character."""

        messages = [
            {
                "role": "system",
                "content": self.enhanced_context(),
            },
            {
                "role": "user",
                "content": f"""
            Generate a single conflict for the character. 
            This should be a sentence or two describing a personal struggle or dilemma that has led them to become an adventurer. 
            Ideally this should be tied to their flaw and maybe their personality traits. 
            You do not need to explain how it all fits together, just provide the raw material. 
            {extra}
            """,
            },
        ]

        print("\nGenerating a conflict...")
        response = chat(
            model=self.model,
            messages=messages,
        )

        conflict = clean_response(response)
        print(conflict)

        return conflict

    def generate_backstory(self, extra=""):
        """Generate a backstory for the character."""

        messages = [
            {
                "role": "system",
                "content": self.enhanced_context(),
            },
            {
                "role": "user",
                "content": f"""
            Generate a single backstory for the character. 
            This should be one or two short paragraphs that provides some history and context for the character. 
            Ideally it should tie together their concept, personality traits, flaw, and conflict. 
            {extra}
            """,
            },
        ]

        print("\nGenerating a backstory...")
        response = chat(
            model=self.model,
            messages=messages,
        )

        backstory = clean_response(response)
        print(backstory)

        return backstory

    def generate_random_names(self, num: int = 5, extra=""):
        """Generate random names for the character."""

        messages = [
            {
                "role": "system",
                "content": self.enhanced_context(),
            },
            {
                "role": "user",
                "content": f"""
            Generate a bulleted list of {num} character names. Use * as the bullets.
            {extra}
            """,
            },
        ]

        print("\nGenerating random names...")
        response = chat(
            model=self.model,
            messages=messages,
        )

        names = clean_response(response)
        print(names)

        # Extract names that start with an asterisk
        name_list = [
            name.strip()[1:].strip().replace("*", "")
            for name in names.split("\n")
            if name.strip().startswith("*") and name.strip()[1:].strip().replace("*", "") != ""
        ]

        return name_list

    def prompt(self, prompt: str):
        """Prompt the LLM for a response. 
        This can be used to generate any type of content."""

        messages = [
            {
                "role": "system",
                "content": self.enhanced_context(),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

        response = chat(
            model=self.model,
            messages=messages,
        )

        return clean_response(response)


if __name__ == "__main__":
    c = Character()

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
