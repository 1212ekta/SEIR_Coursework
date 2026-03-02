import sys
import requests
from bs4 import BeautifulSoup
import re

def web_url():#take  two urls in command line
    if len(sys.argv) < 3:#provide two url's
        print("Argument is None ,please provide it with two URL's")
        sys.exit()  #stop the program prevent from code creashing
    else:
        link1 = sys.argv[1]
        link2 = sys.argv[2]
        if not link1.startswith("http") or not link2.startswith("http"):#secured link
            print("Not an authentic url")
            sys.exit()
    return link1, link2
def retreive_page(link): #it downloads the content of html
    try:
        headers = {"User-Agent": "Mozilla/5.0"} #request to the server as a browser
        server_response = requests.get(link, headers=headers)
    except requests.exceptions.RequestException as e:
        print("error in page loading:", e)
        sys.exit()

    if server_response.status_code != 200:  #200 means page found and everything is ok 
        print("not able to fetch the page")
        sys.exit()
    return server_response.text
def page_html(html_content):
    parsed_cont = BeautifulSoup(html_content, "html.parser")#it extracts the html content by using web scraper 
    return parsed_cont
def retreive_body(parsed_doc):
    if parsed_doc.body:
        visible_text = parsed_doc.body.get_text(separator="\n", strip=True)#remove trailing space 
        return visible_text
    return ""
def count_word_freq(text):
    text = text.lower()
    words = re.findall(r'[a-z0-9]+', text) #it will add the valid alphanumeric character
    freq_count = {}#datastructure which stores the word as key and freq as value
    for elmt in words:
        freq_count[elmt] = freq_count.get(elmt, 0) + 1
    return freq_count
def hash64bit(word):
    p = 53
    m = 2**64 #this number fits in unsigned 64 bit integer space 
    hash_score = 0
    
    for element in word:
        hash_score = (hash_score*p + ord(element) ) % m  #polynomial rolling hash method
    return hash_score

def compute_simhash_64bitt(freq_count): #simhash is use to detect similar documents quickly
    bit_weights = [0] * 64  #store 64bit

    for word in freq_count:
        word_hash = hash64bit(word) #I am not  getting further logic how to do it and facing difficulty in compution of simhash and bit comparison 
    return 0

print("program done")
link1, link2 = web_url()
html1 = retreive_page(link1)
soup1 = page_html(html1)
body1 = retreive_body(soup1)
freq1 = count_word_freq(body1)

print("\nWord_count in a url1")
for word, count in freq1.items():
    print(word, ":", count)

print("\nHash value of url 1")
for word in freq1:
    print(word, "-", hash64bit(word))

html2 = retreive_page(link2)
soup2 = page_html(html2)
body2 = retreive_body(soup2)
freq2 = count_word_freq(body2)

print("\nWord count of url2")
for word, count in freq2.items():
    print(word, ":", count)

print("\nHash values of url2")
for word in freq2:
    print(word, "-", hash64bit(word))
