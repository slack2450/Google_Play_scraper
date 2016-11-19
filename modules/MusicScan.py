import urllib.parse
import urllib.request
def Album(x):
    url = "https://play.google.com/"+x
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())
    the_page = the_page.split("class")
    matching = [s for s in the_page if "document-title\"" in s]
    matching = matching[0].replace("mailto:","")
    print("Email: "+matching)
def Name(x):
    url = "https://play.google.com/"+x
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())
    the_page = the_page.split("<")
    matching = [s for s in the_page if "id-app-title" in s]
    matching = matching[0].replace("div class=\"id-app-title\" tabindex=\"0\">","")
    print("Name: "+matching)
def Rating(x):
    url = "https://play.google.com/"+x
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())
    the_page = the_page.split("<")
    matching = [s for s in the_page if "div class=\"score\" aria-label=" in s]
    matching = matching[0].replace("div class=\"score\" aria-label=\"Rated ","")
    matching = matching.replace(" stars out of five stars\">","")
    matching = matching.split()[0][0:3]
    print("Rating: "+matching)
def Age(x):
    url = "https://play.google.com/"+x
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())
    the_page = the_page.split("<")
    matching = [s for s in the_page if "content-rating-title\"" in s]
    matching = matching[0].replace("div class=\"document-subtitle content-rating-title\">","")
    print("Age Rating: "+matching)
