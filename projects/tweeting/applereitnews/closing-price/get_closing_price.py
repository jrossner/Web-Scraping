import yfinance as yf
from datetime import datetime

def getDateSuffix(x):
  suffix = ''
  x = int(x)
  
  if x == 1 or x == 21 or x == 31:
    suffix = 'st'
  elif x == 3 or x == 23:
    suffix = 'rd'
  elif x == 22 or x == 2:
    suffix = 'nd'
  else:
    suffix = 'th'
   
  return suffix


def getClosingPrice():
  info = yf.Ticker("APLE").history(period="365d")
  today = datetime.today().strftime('%Y-%m-%d')
  last = info.tail(1).index.item().strftime('%Y-%m-%d')
  readableDate = datetime.today().strftime('%A, %B %-d')
  dateSuf = getDateSuffix(datetime.today().strftime('%d'))
  
  if (today == last):
      closing = info["Close"][-1]
      change = (info["Close"][-1] - info["Close"][-2])
      changePerc = 100 * (change / info["Close"][-2])
      if changePerc < 0:
          opp = ''
      else:
          opp = '+'
      text = f'{readableDate}{dateSuf}:\nClosing Price: ${round(closing,2)}'
      #text = f'{readableDate}:\nClosing Price: ${round(closing,2)}'
      text += f'\n1-Day Change: {opp}${round(change,2)} ({opp}{round(changePerc,2)}%)'

      monthChangeAmount = info["Close"][-1] - info["Close"][-30]
      monthChangePerc = 100* (monthChangeAmount / info["Close"][-30])

      if monthChangeAmount < 0:
          monthOpp = ''
      else: 
          monthOpp = '+'

      text += f'\n30-Day Change: {monthOpp}${round(monthChangeAmount,2)} ({monthOpp}{round(monthChangePerc,2)}%)'

      yearChangeAmount = info["Close"][-1] - info["Close"][-365]
      yearChangePerc = 100 * (yearChangeAmount / info["Close"][-365])

      if yearChangeAmount < 0:
          yearOpp = ''
      else: 
          yearOpp = '+'

      text += f'\nYTD Change: {yearOpp}${round(yearChangeAmount,2)} ({yearOpp}{round(yearChangePerc,2)}%)'

  else:
      text = f'{readableDate}{dateSuf}: Market Was Closed Today'
      
  return text
