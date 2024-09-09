from bs4 import BeautifulSoup
import requests



def bbc_links():
    
    all_urls = []
    url = 'https://www.bbc.com'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
        all_urls.append(a['href'])
        
    article_urls = [url for url in all_urls if bbc_is_article(url)]
    
    return article_urls

def bbc_is_article(url, current_year='2024'):
    if url:
         if 'bbc.com' in url and '/article' in url:
            return True
    return False


def cnn_links():
    
    all_urls = []
    url = 'https://www.cnn.com'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
        all_urls.append(a['href'])
        
    article_urls = [url for url in all_urls if cnn_is_article(url)]
    
    return article_urls

def cnn_is_article(url, current_year='2024'):
    if url:
         if 'cnn.com/{}/'.format(current_year) in url and '/gallery/' not in url:
            return True
    return False

def ap_links():
    
    all_urls = []
    url = 'https://www.apnews.com/'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
        all_urls.append(a['href'])
        
    article_urls = [url for url in all_urls if ap_is_article(url)]
    
    return article_urls

def ap_is_article(url, keyword='article'):
    if url:
         if 'apnews.com' in url and '/{}/'.format(keyword) in url:
            return True
    return False


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

def yale_is_article(url, current_year='2024'):
    if url:
         if 'e360.yale.edu' in url and '/features' in url:
            return True
    return False

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

def nature_is_article(url, current_year='2024'):
    if url:
         if 'nature.com' in url and '/articles' in url:
            return True
    return False
  
def science_links():
    
    all_urls = []
    url = 'https://www.sciencenews.org/topic/space'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
            
        all_urls.append(a['href'])
    
    article_urls = [url for url in all_urls if science_is_article(url)]
    
    return article_urls

def science_is_article(url, current_year='2024'):
    if url:
         if 'sciencenews.org' in url and '/article' in url:
            return True
    return False
  
def newsci_links():
    
    all_urls = []
    url = 'https://www.newscientist.com/'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
            
        all_urls.append(a['href'])
    
    article_urls = [url for url in all_urls if newsci_is_article(url)]
    
    return article_urls

def newsci_is_article(url, current_year='2024'):
    if url:
         if 'newscientist.com' in url and '/article' in url:
            return True
    return False
  

def snex_links():
    
    all_urls = []
    url = 'https://www.snexplores.org/'
    data = requests.get(url).text
    soup = BeautifulSoup(data, features="html.parser")
    
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
            
        all_urls.append(a['href'])
    
    article_urls = [url for url in all_urls if newsExpl_is_article(url)]
    
    return article_urls

def newsExpl_is_article(url, current_year='2024'):
    if url:
         if 'snexplores.org' in url and '/article/' in url:
            return True
    return False
  