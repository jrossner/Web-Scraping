from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def checklUpcomingEarnings():
  link = "https://www.marketbeat.com/stocks/NYSE/APLE/earnings/"
  page_request = requests.get(link)
  soup = BeautifulSoup(page_request.text,"lxml")
  head = str(soup.find("dd", class_ = "stat-summary-heading my-1"))
  
  earningsDate = head.split('my-1">')[1].split('<span')[0]
  
  if (datetime.today()+timedelta(days=7)).strftime('%b. %-d') == earningsDate:
    # earnings date is 1 week from today
    text = f'Apple REIT announces earnings 1 week from today ({earningsDate}).'
    
    try:
      page = soup.find("div", {"id": "cphPrimaryContent_pnlCompany"})
      table = str(page.find_all("tbody")[1])
      consensusEst = table.split('</td><td>')[2])
    
      text += f'\nThe Consensus Earnings Estimate for this quarter is {consensusEst}'
    except:
      print("Could not scrape consensus estimates")
  else:
    text = False

  return text

