import urllib.parse
import urllib.request
import modules.AppScan
import modules.MusicScan

searchCriteria = input("Songs(S) or Apps(A)?")
while searchCriteria.lower() != "s" and searchCriteria.lower() !="a":
    searchCriteria = input("Songs(S) or Apps(A)?")
a = input("Search>")
a = a.replace(" ","%20")
if searchCriteria.lower() == "a":
    url = "https://play.google.com/store/search?q="+a+"&c=apps"
    search = "com"
if searchCriteria.lower() == "s":
    url = "https://play.google.com/store/search?q=other&c=music&docType=4"
    search = "song"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    the_page = str(response.read())
the_page = the_page.split("span")
if searchCriteria.lower() == "a":
    matching = [s for s in the_page if "preview-overlay-container\" data-docid=\"com" in s]
if searchCriteria.lower() == "s":
    matching = [s for s in the_page if "card-click-target\" href=\"" in s]
if searchCriteria.lower() == "a":
    for i in range(len(matching)):
        matching[i-1] = matching[i-1].replace(" class=\"preview-overlay-container\" data-docid=\"","")
        matching[i-1] = matching[i-1].replace("\">  </","")
if searchCriteria.lower() == "s":
    for i in range(len(matching)):
        matching[i-1] = matching[i-1].replace("\" aria-hidden=\"true\" tabindex=\"-1\"> </a>   </div> </div>       <div class=\"reason-set\">  <","")
        matching[i-1] = matching[i-1].replace(">  <a class=\"card-click-target\" href=\"","")

print("\n"*2)
print("===Starting App Search===")
print("Apps Found: "+str(len(matching)))
print("\n"*2)
if searchCriteria.lower() == "a":
    for i in range(len(matching)):
        print("ID: "+matching[i-1])
        modules.AppScan.Name(matching[i-1])
        modules.AppScan.Email(matching[i-1])
        modules.AppScan.Rating(matching[i-1])
        modules.AppScan.Age(matching[i-1])
        print("")
if searchCriteria.lower() == "s":
    for i in range(len(matching)):
        print("ID: "+matching[i-1])
        modules.MusicScan.Album(matching[i-1])
        print("")

input("To continue Press enter...")
