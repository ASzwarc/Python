#!usr/bin/env python

import json
import urllib
import re

total_sum = 0.0
pattern = r"[$]\d*[\.|\,]\d*"
replacement = re.compile('\,')
first_link = ("https://gist.githubusercontent.com/jorinvo/"
			 "6f68380dd07e5db3cf5fd48b2465bb04/raw/"
			 "c02b1e0b45ecb2e54b36e4410d0631a66d474323/"
			 "fd0d929f-966f-4d1a-89cd-feee5a1c5347.json")

def add_value_from_content(content):
	global total_sum
	for match in re.findall(pattern, content):
		value = replacement.sub('.', match[1:])
		print("Adding value: " + value)
		total_sum += float(value)

def follow_link_and_get_value(link):
	print("Current sum: " + str(total_sum))
	print("Getting data from:")
	print(link)
	data = urllib.urlopen(link).read()
	output = json.loads(data)
	add_value_from_content(output['content'])
	for link in output['links']:
		follow_link_and_get_value(link)

def main():
	global total_sum
	follow_link_and_get_value(first_link)
	print("Final value is " + str(total_sum))

if __name__ == '__main__':
	main()