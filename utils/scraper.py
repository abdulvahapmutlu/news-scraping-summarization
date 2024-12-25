from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_news_directly(url): 
    """
    Scrapes news content from the provided URL.
    Args:
        url (str): The URL of the news article.
    Returns:
        str: Combined headline and content of the news.
    """
    try:
        # Setup WebDriver
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)

        # Scrape headline
        headline = driver.find_element(By.XPATH, '//h1[@class="news-headline"]').text

        # Scrape paragraphs
        content_elements = driver.find_elements(By.XPATH, '//p[@class="news-paragraph"]')
        content = ' '.join([paragraph.text for paragraph in content_elements])
        
        driver.quit()

        return f"{headline}\n{content}"
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
