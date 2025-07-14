import os
from datetime import datetime
from typing import Dict


def save_persona_to_file(
    persona: Dict, username: str = "unknown", output_dir: str = "output"
):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(output_dir, f"{username}_persona.txt")
    os.makedirs(output_dir, exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"User Persona: {username}\n")
        f.write(f"Generated on: {date_str}\n")
        f.write("---\n")

        # Basic Information
        f.write("Basic Information:\n")
        f.write(f"Name: {persona.get('name', 'N/A')}\n")
        f.write(f"Age: {persona.get('age', 'N/A')}\n")
        f.write(f"Occupation: {persona.get('occupation', 'N/A')}\n")
        f.write(f"Status: {persona.get('status', 'N/A')}\n")
        f.write(f"Location: {persona.get('location', 'N/A')}\n")
        f.write(f"Archetype: {persona.get('archetype', 'N/A')}\n")
        f.write("\n")

        # Personality Traits
        f.write("Personality Traits:\n")
        for trait in persona.get("personality", []):
            f.write(
                f"- {trait['trait']}: Score {trait['score']} (Source: {trait['citation']})\n"
            )
        f.write("\n")

        # Motivations
        f.write("Motivations:\n")
        for motivation in persona.get("motivations", []):
            f.write(
                f"- {motivation['trait']}: Score {motivation['score']} (Source: {motivation['citation']})\n"
            )
        f.write("\n")

        # Preferences
        f.write("Preferences:\n")
        for preference in persona.get("preferences", []):
            f.write(
                f"- {preference['description']} (Source: {preference['citation']})\n"
            )
        f.write("\n")

        # Behavior Habits
        f.write("Behavior Habits:\n")
        for habit in persona.get("behaviour_habits", []):
            f.write(f"- {habit['description']} (Source: {habit['citation']})\n")
        f.write("\n")

        # Frustrations
        f.write("Frustrations:\n")
        for frustration in persona.get("frustrations", []):
            f.write(
                f"- {frustration['description']} (Source: {frustration['citation']})\n"
            )
        f.write("\n")

        # Goals and Needs
        f.write("Goals and Needs:\n")
        for goal in persona.get("goals_needs", []):
            f.write(f"- {goal['description']} (Source: {goal['citation']})\n")
        f.write("\n")

        # Quote
        f.write("Quote:\n")
        f.write(
            f"\"{persona.get('quote', 'N/A')}\" (Source: {persona.get('citation', 'N/A')})\n"
        )
        f.write("---\n")
