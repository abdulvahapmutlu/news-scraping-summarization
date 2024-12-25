from utils.scraper import scrape_news_directly
from utils.summarizer import summarize_text_flan_t5

# Define the target URL
target_url = "https://example-news-website.com/article"

# Scrape the news content
news_content = scrape_news_directly(target_url)
if news_content:
    print("Scraped News Content:")
    print(news_content)
    
    # Summarize the news content
    summary = summarize_text_flan_t5(news_content)
    print("\nSummarized News Content:")
    print(summary)
else:
    print("Failed to scrape news content.")
