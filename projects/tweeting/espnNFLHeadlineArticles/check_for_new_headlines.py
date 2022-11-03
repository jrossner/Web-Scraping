import json

def checkIfNewHeadlines(articles,lastHeadline):
    newHeadlines = []
    for key in articles.keys():
        if key == lastHeadline.keys()[0]:
            break
        else:
            newHeadlines.append(articles[key])
            
    return newHeadlines
