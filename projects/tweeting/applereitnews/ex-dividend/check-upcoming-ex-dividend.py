import yfinance as yf
from datetime import datetime, timedelta

def checkForUpcomingExDividend():
  exDividendEpoch = yf.Ticker("APLE").info['exDividendDate']
  lastDayToOwn = datetime.fromtimestamp(exDividendEpoch).strftime('%Y-%m-%d')
  today = datetime.today()
  
  if lastDayToOwn == (today+timedelta(days=1)).strftime('%Y-%m-%d'):
    text = "Tomorrow is APLE's Ex-Dividend Date.\nThis is the last day to be recorded as an owner of APLE stock to receive the next dividend."
  else:
    text = False

  return text
