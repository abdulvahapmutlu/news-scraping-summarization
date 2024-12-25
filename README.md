# **News Scraping and Summarization**

This project showcases a real-time pipeline for scraping news articles from websites and summarizing their content using the **FLAN-T5-XL** model. It integrates modern tools like Selenium for dynamic web scraping and HuggingFace Transformers for generating concise summaries of lengthy articles.

---

## **Features**
- **Real-Time News Scraping**: Extracts headlines and article content from dynamic news websites using Selenium.
- **High-Quality Summarization**: Summarizes scraped articles into concise, meaningful highlights using FLAN-T5-XL.
- **Customizable**: Supports flexibility in scraping logic (XPath and URLs) and summarization parameters.
- **Efficient Execution**: Optimized for GPUs to accelerate summarization with large models.

---

## **Technologies Used**
- **Python 3.9+**: The primary programming language.
- **Selenium**: For automated and dynamic web scraping.
- **HuggingFace Transformers**: For utilizing the FLAN-T5-XL model.
- **Torch**: Backend framework for model inference, optimized for GPU.
- **Jupyter Notebook**: For development and demonstration.

---

## **Requirements**
- Python 3.8 or higher
- GPU (optional but recommended for faster summarization)
- The following Python libraries:
  - `selenium`
  - `transformers`
  - `torch`

---

## **Setup Instructions**

### **1. Clone the Repository**
```
git clone https://github.com/abdulvahapmutlu/news-scraping-summarization.git
cd news-scraping-summarization
```

### **2. Install Dependencies**
Use the `requirements.txt` file to install the necessary Python packages:
```
pip install -r requirements.txt
```

### **3. Install ChromeDriver**
- Download ChromeDriver from [here](https://chromedriver.chromium.org/downloads).
- Ensure that the version matches your installed Chrome browser.
- Add ChromeDriver to your system's PATH.

---

## **How to Use**

### **1. Update the Target URL**
Replace the placeholder URL in `main.py` with the desired news article URL:
```
target_url = "https://example-news-website.com/article"
```

### **2. Run the Script**
Run the `main.py` file to scrape and summarize the article:
```
python main.py
```

### **3. View the Output**
The script will print both the scraped news content and the summarized version:
```
Scraped News Content:
[Full news content here...]

Summarized News Content:
[Summarized news content here...]
```

---

## **Customization**

### **1. Changing the XPath**
The XPath values in `scraper.py` can be updated to match the structure of different websites:
```
headline = driver.find_element(By.XPATH, '//h1[@class="news-headline"]').text
content_elements = driver.find_elements(By.XPATH, '//p[@class="news-paragraph"]')
```

### **2. Adjusting Summarization Parameters**
In `summarizer.py`, modify the `min_length` and `max_length` values to control the summary's length:
```
summary_ids = model.generate(
    inputs.input_ids,
    max_length=200,  # Maximum length of the summary
    min_length=50,   # Minimum length of the summary
    num_beams=5      # Beam search for better quality
)
```

---

## **License**
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

### **Ethical Considerations and Usage**

This project is intended for educational and research purposes, demonstrating the integration of web scraping and text summarization technologies. Please adhere to the following guidelines to ensure ethical and responsible use:

1. **Respect Website Terms of Service**:
   - Before scraping any website, review and comply with its terms of service to avoid violating policies.
   - Seek permission if the content you wish to scrape requires explicit authorization.

2. **Data Privacy**:
   - Avoid scraping sensitive or personal information from websites.
   - Ensure that the data collected is used responsibly and does not infringe on privacy rights.

3. **Attribution**:
   - Attribute the source of the scraped content where applicable, especially when sharing results or publishing summaries.

4. **Non-Commercial Use**:
   - This project should not be used for commercial purposes without proper licensing or agreements with content owners.

5. **Impact on Servers**:
   - Implement respectful scraping practices, such as rate-limiting and pausing between requests, to prevent overloading the target website's servers.

By adhering to these ethical guidelines, you can ensure that this project is used responsibly and benefits the broader community.
