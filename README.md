# Reddit Persona Builder

## Overview
This Python application scrapes a Reddit user's posts and comments, analyzes them to build a user persona, and outputs the persona to a structured text file with citations.

## Features
- Validates Reddit profile URLs
- Scrapes posts and comments using Reddit API (PRAW)
- Cleans and processes data
- Builds a persona using NLP
- Outputs results to a text file
- Modular, testable codebase

## Project Structure
```
reddit_persona_builder/
├── src/
│   ├── __init__.py
│   ├── input_handler.py
│   ├── reddit_scraper.py
│   ├── data_processor.py
│   ├── persona_builder.py
│   ├── output_generator.py
│   ├── config.py
│   ├── logger.py
├── output/
├── .env.example
├── requirements.txt
├── README.md
├── main.py
```

## Setup
1. **Clone the repository**
2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Reddit API credentials**
   - Copy `.env.example` to `.env` and fill in your Reddit API keys.

## Usage
Run the main script with a Reddit profile URL:
```bash
python main.py https://www.reddit.com/user/kojied/
```
Output files will be saved in the `output/` directory.

## Troubleshooting
- Ensure Reddit API credentials are correct in `.env`.
- Handle rate limits by retrying after some time.
- For issues, check log files or raise an issue on GitHub.

## License
MIT
