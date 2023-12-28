import wikipedia as wiki

def scrape(name):
    result= wiki.summary(name)
    return result

print(scrape("Facebook"))