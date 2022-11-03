def checkIfNewHeadlines(articles,lastHeadline):
    newHeadlines = {}
    for key in articles.keys():
        if lastHeadline != {}:
            try:
                if key == list(lastHeadline.keys())[0]:
                    break
            except:
                print("Problem in check_for_new_headlines")
        
        newHeadlines[key] = articles[key]
            
    return newHeadlines
