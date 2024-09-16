import requests
from bs4 import BeautifulSoup
# response.text ----> shows all html code

target_url = input("Enter a target website url:")


def make_request(url):
    response =  requests.get(url)
    response.encoding = "utf-8"
    # HTML Parsing
    soup = BeautifulSoup(response.text,"lxml")
    return soup
foundLinks = []



def crawler(url):
    links = make_request(url)  # links = soup
    for link in links.find_all('a'):
        found_link = link.get("href")
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if "?" in found_link:
                found_link = found_link.split("?")[0]
            if target_url in found_link and  found_link not in foundLinks:
                foundLinks.append(found_link)
                crawler(found_link)
            
crawler(target_url)

