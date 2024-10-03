import json


"""
Converts nature articles into nature_articles.json

Args: Gets articles from a json object 

Returns: N/A
"""
def nature_converter(articles):
    newArticles = []

    for article in articles:
         if article and len(article) >= 3:
            if article[0] and article[1] and article[2:len(article)]:
                URL = article[0]
                title = article[1]
                content = article[2:len(article)]
                newArticles.append({
                    'URL': URL,
                    'title': title,
                    'content': content
                })
    
    with open('nature_articles.json', 'w', newline='', encoding='utf-8') as f:
        json.dump(newArticles, f, indent=4)



"""
Converts yale articles into yale_articles.json

Args: Gets articles from a json object 

Returns: N/A
"""
def yale_converter(articles):
    newArticles = []

    for article in articles:
         if article and len(article) >= 3:
            if article[0] and article[1] and article[2:len(article)]:
                URL = article[0]
                title = article[1]
                content = article[2:len(article)]
                newArticles.append({
                    'URL': URL,
                    'title': title,
                    'content': content
                })
    
    with open('yale_articles.json', 'w', newline='', encoding='utf-8') as f:
        json.dump(newArticles, f, indent=4)



"""
Converts ScienceNewsExplore articles into snex_articles.json

Args: Gets articles from a json object 

Returns: N/A
"""
def snex_converter(articles):
    newArticles = []

    for article in articles:
         if article and len(article) >= 3:
            if article[0] and article[1] and article[2:len(article)]:
                URL = article[0]
                title = article[1]
                content = article[2:len(article)]
                newArticles.append({
                    'URL': URL,
                    'title': title,
                    'content': content
                })
    
    with open('snex_articles.json', 'w', newline='', encoding='utf-8') as f:
        json.dump(newArticles, f, indent=4)
