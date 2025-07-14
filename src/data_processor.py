import re
from typing import List, Dict


class DataProcessor:
    """
    Cleans and structures scraped Reddit data for analysis.
    """

    @staticmethod
    def clean_data(raw_data: List[Dict]) -> List[Dict]:
        cleaned = []
        for entry in raw_data:
            text = entry.get("text", "")
            if not text or text.lower() in {"[deleted]", "[removed]"}:
                continue
            # Normalize text
            normalized = re.sub(r"[^\w\s]", "", text.lower())
            entry["cleaned_text"] = normalized
            cleaned.append(entry)
        return cleaned
