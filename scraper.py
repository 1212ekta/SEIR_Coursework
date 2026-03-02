import sys #for reading command line argument 
import requests     #for sending requests to the server
from bs4 import BeautifulSoup #for parsing the page

def scrap_webUrl():
    if(len(sys.argv))<2:    #format is filename.py weblink
        print("atleast two argument required ,one is file name other one webUrl")
        sys.exit()
    
    web_url = sys.argv[1]
    if not web_url.startswith("http"):  #if url starts without https add it for extracting the content
        web_url="https://"+web_url      #it looks like https://univ.sitare.org
    
    try:
        browser_request = {"User-Agent":"Mozilla/5.0"}     #request as browser so that there is less chance to deny your request
        serv_response =requests.get(web_url,headers=browser_request)
    except requests.exceptions.RequestException as e:   #
        print("Code is not able to fetch page",e)
        return
    parsed_doc = BeautifulSoup(serv_response.text,"html.parser")

    if parsed_doc.title and parsed_doc.title.string:
        title = parsed_doc.title.string.strip()     #strip removes the extra spaces
    else:
        title = "there is not title"
    print(title)
        
    if parsed_doc.body:
        body_content = parsed_doc.body.get_text(separator="\n",strip=True)
        print(body_content)
    else:
        print("no content in body")

    
    anch_tags=parsed_doc.find_all("a") #all outlinks in the given web page url
    for i in anch_tags:
        href = i.get("href")
        if href:
            print(href)

scrap_webUrl()
