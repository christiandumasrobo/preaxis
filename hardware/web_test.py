from urllib.request import urlopen

page = urlopen("http://10.0.0.131:80/move/50&50")
print(page)