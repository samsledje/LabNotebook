import os
import json
import re

DEBUG = False

if DEBUG:
    SITE_ROOT = "localhost:8080/"
else:
    SITE_ROOT = "https://samsledje.github.io/NetNotebook/"

class LinkParser:
    def __init__(self,filePath):
        self.site_root = SITE_ROOT
        self.filePath = filePath
        self.name = self.filePath.rstrip(".md")
        self.links = []

        self._parse_file()

    def _parse_file(self):
        txt = open(self.filePath,"r",encoding="utf8").read()
        #print(txt)
        #print('===================')
        newTxt = ''
        linkTxt = ''
        inLink = False
        for i in range(len(txt)):
            c = txt[i]
            if c == "[":
                if txt[i+1] == "[":
                    inLink = True
                    continue
                elif inLink:
                    linkTxt += c
                    continue
            if c == "]" and txt[i-1] == "]" and inLink:
                linkName = linkTxt[1:-1]
                linkPath = f"[{linkName}]({self.site_root}{linkName}.md)"
                newTxt += linkPath
                linkTxt = ''
                self.links.append((self.name, linkName))
                inLink = False
                continue
            if inLink:
                linkTxt += c
                continue
            newTxt += c

jsonDataFile = "graphFile2.json"

markdown_files = []

for fi in os.listdir():
    if fi.endswith(".md"):
        markdown_files.append(fi)

data = {"nodes":[], "links":[]}
nodes = []
lpObjects = []

for fi in markdown_files:
    lp = LinkParser(fi)
    lpObjects.append(lp)
    if DEBUG:
        url = f"{SITE_ROOT}{lp.name}.md"
    else:
        url = f"{SITE_ROOT}{lp.name}"
    data["nodes"].append({"name":lp.name,"url":url})
    nodes.append(lp.name)

for lp in lpObjects:
    for l in lp.links:
        try:
            sourceIndex = nodes.index(l[0])
            sourceTarget = nodes.index(l[1])
            data["links"].append({"source":sourceIndex,"target":sourceTarget})
        except ValueError:
            pass

with open(jsonDataFile,"w+",encoding="utf8") as f:
    f.write(json.dumps(data))


