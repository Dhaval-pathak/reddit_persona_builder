import os
import openai
from typing import List, Dict


class PersonaBuilder:
    @staticmethod
    def build_persona_with_llm(cleaned_data: List[Dict]) -> Dict:
        # Use OpenAI v1+ API
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        user_text = "\n".join(
            [entry["cleaned_text"] for entry in cleaned_data if "cleaned_text" in entry]
        )
        prompt = f"""
                Given the following Reddit user's posts and comments, extract a detailed, structured user persona. 
                For each trait (personality, motivation, preferences, habits, frustrations, goals), provide:
                - A description
                - A citation: post/comment ID, a 1-2 sentence snippet, subreddit, timestamp (from the data)

                Return the persona as a JSON object with these fields:
                - name, age, occupation, status, location, archetype
                - personality: list of trait, score (0-5), citation
                - motivations: list of trait, score (0-5), citation
                - preferences: list of description, citation
                - behaviour_habits: list of description, citation
                - frustrations: list of description, citation
                - goals_needs: list of description, citation
                - quote: text, citation

                If information is missing, infer reasonably or mark as 'Unspecified'.

                User Data:
                {user_text}

                Persona JSON:
                """
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[{"role": "user", "content": prompt}],
        )
        import json

        persona_text = response.choices[0].message.content
        try:
            persona = json.loads(persona_text)
        except Exception:
            persona = {"persona_text": persona_text}

        return persona
