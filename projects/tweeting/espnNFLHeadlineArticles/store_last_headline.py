import json

def storeLastHeadline(newHeadlines):
  last_headline = {newHeadlines[list(newHeadlines.keys())[0]]}
  
  object = json.dumps(last_headline)
  
  with open('last_headline.json', 'w') as outfile:
    outfile.write(object)
  
