import json

def checkIfNewHeadlines(articles,lastHeadline):
    newHeadlines = []
    for key in articles.keys():
        if lastHeadline != {}:
            if key == list(lastHeadline.keys())[0]:
                break
                
        newHeadlines.append(articles[key])
            
    return newHeadlines
