from bs4 import BeautifulSoup, SoupStrainer
import requests
import json

def check_headlines(sport="nba",keys=["boston","celtic"]):
    base_url = f'https://www.espn.com/{sport}/'
    page_request = requests.get(base_url) 
    soup = BeautifulSoup(page_request.text,"lxml")

    try:
        col2 = soup.find("section", class_ = "col-two contentFeed")
        mTO = col2.find("section", class_ = "contentItem mobile-tablet-only")
        hLStack = mTO.find("div", class_="headlineStack")
        lContainer = hLStack.find("section", class_="headlineStack__listContainer")
        headlineList = hLStack.findAll("ul", class_="headlineStack__list")
    except AttributeError:
        return "Can't find a page for that sport..."

    links = []
    headlines = []
    for list in headlineList:
        for link in list.findAll('a'):
            links.append('https://www.espn.com/'+link.get('href'))
            headlines.append(link.text)

    # relevant headlines
    hl = {}
    for title in headlines:
        link = links[headlines.index(title)]
        sport = link.split('/story')[0].split('//',2)[2]
        if keys == None or len(keys) == 0:
            present = True
        else:
            present = False
            for key in keys:
                if (key in link) or (key in title):
                    present = True
                    
        if present == True:
            hl[title] = {"link": link, "title": title,"sport": sport}
            # print(f'Checkout this article: {link}')
            
    return hl

# call function
check_headlines()
