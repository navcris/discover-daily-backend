import json

def cnn_converter(articles):
    newArticles = []

    for article in articles:
        if article and len(article) >= 3:
            URL = article[0]
            title = article[1]
            content = article[3:len(article)]

            newArticles.append({
                'URL': URL,
                'title': title,
                'content': content
            })
        
        
    with open('cnn_articles.json', 'w', newline='', encoding='utf-8') as f:
        json.dump(newArticles, f, indent=4)

def bbc_converter(articles):
    newArticles = []

    for article in articles:
         if article and len(article) >= 3:
            URL = article[0]
            title = article[1]
            content = article[2:len(article)]
            newArticles.append({
                'URL': URL,
                'title': title,
                'content': content
            })
    
    with open('bbc_articles.json', 'w', newline='', encoding='utf-8') as f:
        json.dump(newArticles, f, indent=4)

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
