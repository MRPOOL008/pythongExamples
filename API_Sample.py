import requests
import sys
import json

def main():

    if(len(sys.argv)) !=2:
        sys.exit()
    
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
    
    #print(json.dumps(response.json(), indent= 2))

    out = response.json()

    for results in out["results"]:
        print(results["trackName"])


main()