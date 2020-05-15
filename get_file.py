import urllib.request, json 
def get_file(link):
    with urllib.request.urlopen(link) as url:
        return json.loads(url.read().decode())