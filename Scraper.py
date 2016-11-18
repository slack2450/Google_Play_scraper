import urllib.parse
import urllib.request

a = input("Search>")
a = a.replace(" ","%20")
url = "https://play.google.com/store/search?q="+a+"&c=apps"

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    the_page = str(response.read())
the_page = the_page.split("span")
matching = [s for s in the_page if "preview-overlay-container\" data-docid=\"com" in s]
for i in range(len(matching)):
    matching[i-1] = matching[i-1].replace(" class=\"preview-overlay-container\" data-docid=\"","")
    matching[i-1] = matching[i-1].replace("\">  </","")

def appScanEmail(x):
    url = "https://play.google.com/store/apps/details?id="+x+"&hl=en_GB"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())
    the_page = the_page.split("\"")
    matching = [s for s in the_page if "mailto:" in s]
    matching = matching[0].replace("mailto:","")
    print("Email: "+matching)
def appScanName(x):
    url = "https://play.google.com/store/apps/details?id="+x+"&hl=en_GB"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())
    the_page = the_page.split("<")
    matching = [s for s in the_page if "id-app-title" in s]
    matching = matching[0].replace("div class=\"id-app-title\" tabindex=\"0\">","")
    print("Name: "+matching)
def appScanRating(x):
    url = "https://play.google.com/store/apps/details?id="+x+"&hl=en_GB"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())
    the_page = the_page.split("<")
    matching = [s for s in the_page if "div class=\"score\" aria-label=" in s]
    matching = matching[0].replace("div class=\"score\" aria-label=\"Rated ","")
    matching = matching.replace(" stars out of five stars\">","")
    matching = matching.split()[0][0:3]
    print("Rating: "+matching)

print("\n"*2)
print("===Starting App Search===")
print("Apps Found: "+str(len(matching)))
print("\n"*2)
for i in range(len(matching)):
    print("ID: "+matching[i-1])
    appScanName(matching[i-1])
    appScanEmail(matching[i-1])
    appScanRating(matching[i-1])
    print("")

input()
