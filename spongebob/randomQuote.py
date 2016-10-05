#!/usr/bin/python
import json
import codecs
import random

with codecs.open("quotes.json", "r", "utf-8") as f:
    data = json.load(f)

quotes = []

for p in data["pages"]:
    for r in p["results"]:
        quote = r["quote/_text"]
        character = ""
        try:
            character = r["character"]
        except KeyError:
            pass
        quotes.append([quote, character])

while True:
    raw_input()
    index = int(random.random()*len(quotes))
    pair = quotes[index]
    print pair[0]
    raw_input()
    print pair[1]
