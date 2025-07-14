import praw
from typing import List, Dict
import time
from .config import get_reddit_config
from .logger import get_logger


class RedditScraper:
    """
    Fetches posts and comments from a Reddit user's profile using PRAW.
    """

    def __init__(self):
        config = get_reddit_config()
        self.logger = get_logger()
        self.reddit = praw.Reddit(
            client_id=config["REDDIT_CLIENT_ID"],
            client_secret=config["REDDIT_CLIENT_SECRET"],
            user_agent=config["REDDIT_USER_AGENT"],
        )

    def fetch_user_content(self, username: str, limit: int = 200) -> List[Dict]:
        user = self.reddit.redditor(username)
        data = []
        items_fetched = 0
        for item in user.submissions.new(limit=limit):
            data.append(
                {
                    "type": "post",
                    "id": item.id,
                    "text": item.title + "\n" + (item.selftext or ""),
                    "subreddit": str(item.subreddit),
                    "timestamp": int(item.created_utc),
                }
            )
            items_fetched += 1
        for item in user.comments.new(limit=limit):
            data.append(
                {
                    "type": "comment",
                    "id": item.id,
                    "text": item.body,
                    "subreddit": str(item.subreddit),
                    "timestamp": int(item.created_utc),
                }
            )
            items_fetched += 1
        self.logger.info(f"Fetched {items_fetched} items for user {username}")
        return data
