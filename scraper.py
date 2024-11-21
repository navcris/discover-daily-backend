import requests
from bs4 import BeautifulSoup
from URLfilter import KEYWORDS
import os
import re

imgFile_Path = "imgs"

"""
Takes Nature urls, filters based on blacklisted words in title, and
scrapes article text into json object

Args: URLs in an array 

Returns: Article text content json object
"""
def nature_scraper(urls):
    
    articles = []
    
    for url in urls:
        bottomCheck = False
        individual_list = [] 
        
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')
        title = soup.find('h1').string
        
        article_element = soup.find('article')
        if not article_element:
            continue

        section = article_element.find_all(['p', 'img', 'h2'])
        typeArticle = soup.find("span", class_="c-article-identifiers__type")
        if typeArticle is None or "NEWS" not in typeArticle.text or "VIEWS" in typeArticle.text:
            continue
        check = True
        for keyword in KEYWORDS:
            if title is None or keyword in title:
                check = False
                break
        if check == True:
           individual_list.append(url)
           individual_list.append(title)
           
           for content in section:
               
               if bottomCheck == True:
                break
               else:
               
                if content.name == 'img':
                    
                    if content.get('alt'):
                            newFilename = content.get('alt')
                            newFilename = re.sub(r'[\\/*?:"<;>|—().]', "", newFilename)
                            newFilename = re.sub(r'\s+', '_', newFilename)
                            newFilename = newFilename[:100]
                            individual_list.append('*' + newFilename)
                            
                            
                            img_data = requests.get("https:" + content.get('src')).content
                            
                            
                            final_path = os.path.join(imgFile_Path, newFilename + '.jpg')
                            
                            with open(final_path, 'wb') as handler:
                                handler.write(img_data)

                
                if content.name == "h2":
                    individual_list.append("h2" + content.text)
                
                if content.name == 'p':
                    if content.get('class') is None: 
                        individual_list.append(content.text)
                    elif content.get('class') == ['figure__caption', 'u-sans-serif']:
                        individual_list.append(content.text)
                    if "doi:" in content.text:
                                    bottomCheck = True
        
           
          
           articles.append(individual_list)
        
        continue
    
        
    return articles
           
    
"""
Takes Yale urls, filters based on blacklisted words in title, and
scrapes article text into json object

Args: URLs in an array 

Returns: Article text content json object
"""
def yale_scraper(urls):
    i = 0
    articles = []
    
    for url in urls:
        
        individual_list = [] 
        
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')

        if soup.find('h1', class_= "article__title") is None:
            continue
        title = soup.find('h1', class_= "article__title").string
        
        main = soup.find('main', class_="main")
        main_img = main.find('img')
        img_cap = soup.find('span', class_='article__caption')
        
        article_element = soup.find('section', class_='article__body')
        
        if not article_element:
            continue

        section = article_element.find_all(['p', 'img', 'blockquote', 'iframe', 'h4'])
        
       
        if main_img and img_cap:
            section.insert(0, img_cap)
            section.insert(0, main_img)
        
        check = True
        for keyword in KEYWORDS:
            if title is None or keyword in title:
                check = False
                break
        if check == True:
           individual_list.append(url)
           individual_list.append(title)
           

           for content in section:
               
               
                if content.name == 'img' and content.parent and content.parent.get('class') != ["footnote-image"]:
                            
                            if content.get('alt'):
                                newFilename = content.get('alt')
                            else: 
                                newFilename = title + str(i)
                                i += 1
                            

                            newFilename = re.sub(r'[\\/*?:"<;>|—().]', "", newFilename)
                            newFilename = re.sub(r'\s+', '_', newFilename)
                            newFilename = newFilename[:100]
                            individual_list.append('*' + newFilename)
                            
                            
                            img_data = requests.get("https://e360.yale.edu" + content.get('src')).content
                            
                            
                            final_path = os.path.join(imgFile_Path, newFilename + '.jpg')
                            
                            with open(final_path, 'wb') as handler:
                                handler.write(img_data)


                if content.name == "h4":
                    individual_list.append("h4" + content.text)
                
                if content.name == "iframe":
                    
                    individual_list.append("iF" + content.get('src'))
                    
                
                if content.name == "p" and content.parent and content.parent.name != 'aside':
                    
                    if content.get("class") == ['article__figcaption-p']:
                        individual_list.append("fC" + content.text)
                    else:
                        individual_list.append(content.text)
                    
                    
                
                if content.name == "blockquote":
                    individual_list.append("BQ" + content.text)
                

           if (individual_list[2][0] == '*'):
               articles.append(individual_list)
           
        
        continue
    
        
    return articles
           
    
"""
Takes ScienceNewsExplore urls, filters based on blacklisted words in title, and
scrapes article text into json object

Args: URLs in an array 

Returns: Article text content json object
"""   
def snex_scraper(urls):
    i = 0
    articles = []
    
    for url in urls:
         
        individual_list = [] 
        
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')
        
        if soup.find('h1', class_= "header-default__title___ychM4") is None:
            continue
        title = soup.find('h1', class_= "header-default__title___ychM4").string
        
        article_element = soup.find('div', class_='rich-text rich-text--with-sidebar single__rich-text___DT62t')
        
        if not article_element:
            continue

        section = article_element.find_all(['p', 'img', 'figcaption', 'iframe'])
        
        main = soup.find('main', class_="site-main")
        main_img = main.find('img')
        if soup.find('span', class_='header-default__caption___sYDk1'):
            img_cap = soup.find('span', class_='header-default__caption___sYDk1').findChild()
        
        
        if main_img and img_cap:
            section.insert(0, img_cap)
            section.insert(0, main_img)
        
        check = True
        # for keyword in KEYWORDS:
        #     if title is None or keyword in title:
        #         check = False
        #         break
        if check == True:
           individual_list.append(url)
           individual_list.append(title)
           

           for content in section:
               
               
                if content.name == 'img' and content.get("class") and content.get('class') != ["newsletter-signup__background___Eym8W"]:
                           
                            if content.get('alt'):
                                newFilename = content.get('alt')
                            elif title:
                                newFilename = title + str(i)
                                i += 1
                            else: 
                                i += 1
                            

                            newFilename = re.sub(r'[\\/*?:"<;>|—().]', "", newFilename)
                            newFilename = re.sub(r'\s+', '_', newFilename)
                            newFilename = newFilename[:100]
                            individual_list.append('*' + newFilename)
                            
                            
                            img_data = requests.get(content.get('src')).content
                            
                            
                            final_path = os.path.join(imgFile_Path, newFilename + '.jpg')
                            
                            with open(final_path, 'wb') as handler:
                                handler.write(img_data)

                
                if content.name == "iframe":
                    
                    individual_list.append("iF" + content.get('src'))
                    
                
                if content.name == "p" and content.parent and content.parent.get('class') != ["newsletter-signup__message___pemaq"] and content.get('class') != ["newsletter-signup__thankyou___K6GGN"] and content.get('class') != ["newsletter-signup__error___hCsJI"]:
                    individual_list.append(content.text)
                    
                
                if content.name == "figcaption":
                    if content.findChild():
                        individual_list.append("fC" + content.findChild().text)
                    else:
                        individual_list.append(content.text)    
        
           
          
           articles.append(individual_list)
        
        continue
    
        
    return articles