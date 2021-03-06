import os
import json
import re

WRITE_HTML = False
DEBUG = False

if DEBUG:
    SITE_ROOT = "localhost:8080/"
else:
    SITE_ROOT = "https://samsledje.github.io/LabNotebook/"

class LinkParser:
    def __init__(self,filePath):
        self.site_root = SITE_ROOT
        self.filePath = filePath
        self.name = self.filePath.split(".md")[0]
        self.shortname = self.name
        if len(self.name) > 35:
            self.shortname = self.name[:32]+"..."
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
                linkName = linkTxt[1:-1].split('|')[0]
                linkPath = f"[{linkName}]({self.site_root}{linkName}.md)"
                newTxt += linkPath
                linkTxt = ''
                self.links.append((self.shortname, linkName))
                inLink = False
                continue
            if inLink:
                linkTxt += c
                continue
            newTxt += c
        if WRITE_HTML:
            with open(f"html/{self.name}.html","w+",encoding='utf8') as f:
                f.write(newTxt)

jsonDataFile = "graphFile.json"

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
    data["nodes"].append({"name":lp.shortname,"url":url,"full_name":lp.name})
    nodes.append(lp.name)

for lp in lpObjects:
    for l in lp.links:
        try:
            sourceIndex = nodes.index(l[0])
            sourceTarget = nodes.index(l[1])
            data["links"].append({"source":sourceIndex,"target":sourceTarget})
            data["links"].append({"source":sourceTarget,"target":sourceTarget})
        except ValueError:
            pass

with open(jsonDataFile,"w+",encoding="utf8") as f:
    f.write(json.dumps(data))


