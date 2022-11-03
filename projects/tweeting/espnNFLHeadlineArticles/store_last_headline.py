import json

def storeLastHeadline(newHeadlines):
  print("check 1")
  last_headline = {newHeadlines[list(newHeadlines.keys())[0]]}
  
  print(f'last_headline: {str(last_headline)}')
  object = json.dumps(last_headline)
  
  with open('last_headline.json', 'w') as outfile:
    outfile.write(object)
  
