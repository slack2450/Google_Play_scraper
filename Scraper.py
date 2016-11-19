import urllib.parse
import urllib.request
import modules.AppScan

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

print("\n"*2)
print("===Starting App Search===")
print("Apps Found: "+str(len(matching)))
print("\n"*2)
for i in range(len(matching)):
    print("ID: "+matching[i-1])
    modules.AppScan.Name(matching[i-1])
    modules.AppScan.Email(matching[i-1])
    modules.AppScan.Rating(matching[i-1])
    modules.AppScan.Age(matching[i-1])
    print("")

input("To continue Press enter...")
