import re


class InputHandler:
    """
    Handles parsing and validation of Reddit user profile URLs.
    """

    USER_URL_PATTERN = re.compile(
        r"https?://(www\.)?reddit\.com/user/(?P<username>[A-Za-z0-9_-]+)/?"
    )

    @staticmethod
    def extract_username(url: str) -> str:
        match = InputHandler.USER_URL_PATTERN.match(url)
        if not match:
            raise ValueError(f"Invalid Reddit user URL: {url}")
        return match.group("username")

    @staticmethod
    def validate_url(url: str) -> bool:
        return bool(InputHandler.USER_URL_PATTERN.match(url))
