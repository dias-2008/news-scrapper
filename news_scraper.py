import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime
from typing import List, Dict
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_user_agent() -> str:
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    ]
    return random.choice(user_agents)

def scrape_lenta() -> List[Dict]:
    news_list = []
    try:
        headers = {
            'User-Agent': get_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
        
        logger.info("Attempting to scrape Lenta.ru...")
        response = requests.get('https://lenta.ru/', headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Updated selector for Lenta.ru
        news_items = soup.select('a.card-mini._compact')[:10]
        
        for item in news_items:
            title = item.get_text(strip=True)
            link = item.get('href')
            if not link.startswith('http'):
                link = f"https://lenta.ru{link}"
            
            news_list.append({
                'title': title,
                'date': datetime.now().strftime('%Y-%m-%d'),
                'link': link
            })
            logger.info(f"Found article: {title}")
            
    except requests.RequestException as e:
        logger.error(f"Error scraping Lenta.ru: {e}")
    except Exception as e:
        logger.error(f"Unexpected error while scraping Lenta.ru: {e}")
    
    return news_list

def scrape_ria() -> List[Dict]:
    news_list = []
    try:
        headers = {
            'User-Agent': get_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
        
        logger.info("Attempting to scrape RIA.ru...")
        response = requests.get('https://ria.ru/', headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Updated selector for RIA.ru
        news_items = soup.select('div.cell-list__item')[:10]
        
        for item in news_items:
            title_element = item.select_one('a.cell-list__item-link')
            if title_element:
                title = title_element.get_text(strip=True)
                link = title_element.get('href')
                
                news_list.append({
                    'title': title,
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'link': link
                })
                logger.info(f"Found article: {title}")
                
    except requests.RequestException as e:
        logger.error(f"Error scraping RIA.ru: {e}")
    except Exception as e:
        logger.error(f"Unexpected error while scraping RIA.ru: {e}")
    
    return news_list

def save_as_table(news_data: List[Dict], filename: str):
    # Create DataFrame
    df = pd.DataFrame(news_data)
    
    # Add source column based on URL
    df['source'] = df['link'].apply(lambda x: 'Lenta.ru' if 'lenta.ru' in x else 'RIA.ru')
    
    # Reorder columns
    df = df[['source', 'title', 'date', 'link']]
    
    # Save as CSV
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    
    # Display table in console
    print("\nNews Articles Table:")
    print(df.to_string(max_colwidth=50))
    
    # Save as Excel for better formatting
    excel_file = filename.replace('.csv', '.xlsx')
    df.to_excel(excel_file, index=False, sheet_name='News Articles')
    
    print(f"\nFiles saved as:\n{filename}\n{excel_file}")

def main():
    lenta_news = scrape_lenta()
    ria_news = scrape_ria()
    
    all_news = lenta_news + ria_news
    save_as_table(all_news, 'news.csv')

if __name__ == "__main__":
    main()