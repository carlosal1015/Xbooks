import urllib.request as www
version = eval(www.urlopen("https://api.github.com/repos/xsoft-technologies/Xbooks/tags").read())[0]["name"]
