#!/usr/bin/python

import json, os, os.path
from StringIO import StringIO

# For each json file
languages = {}
for d in os.listdir("."):
  ext = os.path.splitext(os.path.basename(d))[1]
  if not ext == '.json': continue
  if d == 'docs.json': continue
  print(d)
  f = open(d)
  contents = f.read()
  f.close()
  j = json.load(StringIO(contents))
  languages[d] = j

amalg = json.dumps(languages, separators=(',',':'))
print amalg

f = file("docs.json", "w+")
f.write(amalg)
f.close()
print("-------")
print("Data written to docs.json")
