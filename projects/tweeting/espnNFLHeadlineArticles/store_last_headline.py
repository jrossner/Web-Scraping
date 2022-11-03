import json

def storeLastHeadline(newHeadlines):
  last_headline = newHeadlines[list(newHeadlines.keys())[0]]
  object = json.dumps(last_headline)
  
  try:
    with open('last_headline.json', 'w') as outfile:
      outfile.write(object)
      print('json file written successfully')
  except Exception as ex:
    print(f'Could not write json file due to: {ex}')
    
  
