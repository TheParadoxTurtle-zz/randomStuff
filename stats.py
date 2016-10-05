#!/usr/bin/python
import json, codecs

with codecs.open("popData.json", "r", "utf-8") as f:
    data = json.load(f)

singlePage = True
nums = [0]*9
if(not singlePage):
    for p in data["pages"]:
        for r in p["results"]:
            temp = (r["data"])
            index = -1
            for i in range(len(temp)):
                if(temp[i] == u"\u2660"):
                    index = i
                    break
            nums[int(index+1)] += 1
if(singlePage):
    for r in data["results"]:
        temp = unicode(r["population"])
        index = -1
        for i in range(len(temp)):
            if(temp[i] == u"\u2660"):
                index = i
                break
        nums[int(index+1)] += 1

total = sum(nums)
print "Sample size ", total
for i in range(9):
    print (i+1), 100*(nums[i]/float(total))
