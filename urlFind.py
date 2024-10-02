from bs4 import BeautifulSoup
import requests



"""
Scrapes homepage of Yale news and stores article URLs in array

Args: N/A

Returns: N/A
"""
def yale_links():
    
    all_urls = []
    url = 'https://e360.yale.edu'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
        all_urls.append(a['href'])
        
    article_urls = [url for url in all_urls if yale_is_article(url)]
    
    return article_urls



"""
Checks if Yale url is an article

Args: URL scraped from Yale Homepage

Returns: Whether or not the url leads to an article
"""
def yale_is_article(url):
    if url:
         if 'e360.yale.edu' in url and '/features' in url:
            return True
    return False



"""
Scrapes homepage of Nature.com and stores article URLs in array

Args: N/A

Returns: N/A
"""
def nature_links():
    
    all_urls = []
    url = 'https://www.nature.com/news'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
            
        all_urls.append(a['href'])
    
    article_urls = [url for url in all_urls if nature_is_article(url)]
    
    return article_urls



"""
Checks if Nature url is an article

Args: URL scraped from Nature Homepage

Returns: Whether or not the url leads to an article
"""
def nature_is_article(url):
    if url:
         if 'nature.com' in url and '/articles' in url:
            return True
    return False



"""
Scrapes homepage of ScienceNewsExplore and stores article URLs in array

Args: N/A

Returns: N/A
"""
def snex_links():
    
    all_urls = []
    url = 'https://www.snexplores.org/'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
            
        all_urls.append(a['href'])
    
    article_urls = [url for url in all_urls if snex_is_article(url)]
    
    return article_urls



"""
Checks if ScienceNewsExplore url is an article

Args: URL scraped from ScienceNewsExplore Homepage

Returns: Whether or not the url leads to an article
"""
def snex_is_article(url):
    if url:
         if 'snexplores.org' in url and '/article/' in url:
            return True
    return False
  