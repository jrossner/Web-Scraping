from bs4 import BeautifulSoup, SoupStrainer
import requests
import json

base_url = 'https://www.espn.com/nba/'
page_request = requests.get(base_url)
soup = BeautifulSoup(page_request.text,"lxml")

# find headlines section
col2 = soup.find("section", class_ = "col-two contentFeed")
mTO = col2.find("section", class_ = "contentItem mobile-tablet-only")
hLStack = mTO.find("div", class_="headlineStack")
lContainer = hLStack.find("section", class_="headlineStack__listContainer")
headlineList = hLStack.find("ul", class_="headlineStack__list")

# get headlines and associated links
headlines = [line.text for line in headlineList.find_all('a')]
links = []
for link in headlineList.findAll('a'):
    links.append('https://www.espn.com/'+link.get('href'))

# compile dictionary of headlines and if they have desired team/city/sport present
hl = {}
for title in headlines:
    link = links[headlines.index(title)]
    sport = link.split('/story')[0].split('//',2)[2]
    present = True if ('boston' in link or 'celtic' in link or 'boston' in title or 'celtic' in title) else False 
    hl[title] = {"link": link, "title": title,"sport": sport,"keyTeamPresent": present}
    
    # for development purposes
    if present:
        print(f'Checkout this article: {link}')

# Write to .json
with open("headlineInfo.json", "w") as outfile:
    outfile.write(json.dumps(hl,indent=1))
