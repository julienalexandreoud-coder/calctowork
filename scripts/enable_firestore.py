import urllib.request
import urllib.error
import json

# Enable Firestore API
try:
    url = "https://firestore.googleapis.com/v1/projects/calctowork/databases?databaseId=%28default%29"
    data = json.dumps({
        "type": "FIRESTORE_NATIVE",
        "locationId": "eur3"
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    
    response = urllib.request.urlopen(req)
    print("Firestore enabled successfully!")
    print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
