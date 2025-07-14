import sys
from src.input_handler import InputHandler
from src.reddit_scraper import RedditScraper
from src.data_processor import DataProcessor
from src.persona_builder import PersonaBuilder
from src.output_generator import save_persona_to_file
from src.logger import get_logger

def main():
    logger = get_logger()
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py <reddit_user_profile_url>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        username = InputHandler.extract_username(url)
        logger.info(f"Extracted username: {username} (extract_username)")
        scraper = RedditScraper()
        raw_data = scraper.fetch_user_content(username)
        logger.info(f"Fetched raw data (fetch_user_content)")
        cleaned_data = DataProcessor.clean_data(raw_data)

        persona = PersonaBuilder.build_persona_with_llm(cleaned_data)
        print("persona")
        print("--------------------------------------------")
        print(persona)

        save_persona_to_file(persona, username)
        logger.info(f"Persona file generated for {username} (save_persona_to_file)")
    except Exception as e:
        logger.error(f"Error at {sys._getframe().f_code.co_name}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
