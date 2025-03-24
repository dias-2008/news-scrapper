# News Scraper

A Python script that scrapes news articles from Lenta.ru and RIA.ru news websites.

## Features

- Scrapes the latest news from two major Russian news websites
- Stores data in both CSV and Excel formats
- Captures article titles, publication dates, and source links
- Handles Cyrillic characters correctly
- Implements error handling and logging
- Uses user-agent rotation to prevent blocking

## Requirements

- **Python 3.7+**
- Required packages:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dias-2008/news-scrapper.git
   cd news-scrapper
   ```
2. **Install the required packages:**
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
   ```

## Usage

Run the script:

```bash
python news_scraper.py
```

The script will generate the following output files:

- `news.csv` - CSV file with scraped news
- `news.xlsx` - Excel file with formatted data

## Output Format

The data is stored with the following columns:

- **Source**: News source website
- **Title**: Article headline
- **Date**: Publication date
- **Link**: URL to the full article

## Error Handling

The script includes error handling for:

- Network connection issues
- Website structure changes
- File writing operations

## License

This project is licensed under the **MIT License**.

## Disclaimer

Please ensure you comply with the websites' terms of service and `robots.txt` policies when using this scraper.
