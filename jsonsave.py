from inshorts import getNews
import json

with open('data.json', 'w') as fp:
    json.dump(getNews(""), fp)

