# Search Engines and Information Retrieval – Spring 2026  
## Practical Coursework Implementation  
### Web Page Content Extractor (Mini Crawler Component)

---

## 📌 Course Information

- **Course:** Search Engines and Information Retrieval – Spring 2026  
- **Faculty:** Dr. Amit Singhal  
- **Institution:** Sitare University  

---

## 📖 Project Overview

This project is developed as part of the practical coursework for the course **Search Engines and Information Retrieval**.

The program implements a basic webpage processing system that:

- Accepts a URL via command-line argument  
- Fetches webpage content using HTTP  
- Extracts structured textual data  
- Saves extracted information into a text file  

This implementation represents the **initial stage of a search engine pipeline**, specifically focusing on:

- Web Crawling  
- Webpage Processing  
- Text Extraction  

---

## 🎯 Objective

The objective of this coursework is to:

- Understand the fundamentals of web crawling  
- Process HTML documents  
- Extract useful information from web pages  
- Apply Python programming concepts in Information Retrieval  

---

## 🛠 Technologies Used

- Python 3.x  
- `requests` (HTTP communication)  
- `BeautifulSoup` (HTML parsing)  
- `sys` (command-line argument handling)  

---

## ⚙️ Program Functionality

The program performs the following steps:

1. Validates the URL provided via command line  
2. Sends an HTTP request to retrieve webpage content  
3. Parses the HTML structure  
4. Extracts:
   - Page Title (without HTML tags)
   - Page Body Text (plain text only)
   - All hyperlinks (`href` attributes of `<a>` tags)
5. Stores the output in `output.txt`

---

## ▶️ How to Run the Program

### 1️⃣ Install Required Libraries

```bash
pip install requests
pip install beautifulsoup4
