#!usr/bin/env python

import json
import urllib
import re

regexp_patter = re.compile("\$\d*(\.|\,)\d*")

data = urllib.urlopen("https://gist.githubusercontent.com/jorinvo/"
					  "6f68380dd07e5db3cf5fd48b2465bb04/raw/"
					  "c02b1e0b45ecb2e54b36e4410d0631a66d474323/"
					  "fd0d929f-966f-4d1a-89cd-feee5a1c5347.json").read()
output = json.loads(data)

#print(output['content'])

for match in regexp_patter.findall(output['content']):
	print(match)