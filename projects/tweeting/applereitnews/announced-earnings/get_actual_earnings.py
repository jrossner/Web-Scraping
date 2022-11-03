from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def checkEarningsFigures():
  link = "https://www.marketbeat.com/stocks/NYSE/APLE/earnings/"
  page_request = requests.get(link)
  soup = BeautifulSoup(page_request.text,"lxml")
  
  section = soup.find("div", {"id": "cphPrimaryContent_pnlCompany"})
  tiles = section.find_all("div", class_="d-flex justify-content-center align-items-center align-content-center w-100 py-1 shadow mb-3 text-center stat-summary-wrapper py-1 earnings-wrapper")

  actual = ""
  for tile in tiles:
    tile = str(tile)
    if "Actual EPS" in tile:
        actual += tile
  
  postedDate = actual.split("Actual EPS <br/> (")[1].split(") </dt>")[0]
  
  head = str(soup.find("dd", class_ = "stat-summary-heading my-1"))
  earningsDate = head.split('my-1">')[1].split('<span')[0]

  if postedDate == earningsDate:
    actualEarnings = actual.split(">$")[1].split(" <span")[0]
    diff = actual.split(" By ")[1].split(" </span>")[0]
    
    text = f'Apple Hospitality REIT announced earnings of ${actualEarnings} this quarter'
    if '-' in diff:
        text += f', missing consensus estimates by ${diff.split("$")[1]}'
    if diff == '$0.00':
        text += f', on par with consensus estimates'
    else:
        text += f', beating consensus estimates by ${diff.split("$")[1]}'
  else:
    text = False

  return text
