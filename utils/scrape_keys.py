'''
Quick scrape utility to download and store all of the VK_CODEs 
and values so I don't have to copy/paste all of them by hand. 
'''

import json
import urllib
import urllib2
import html5lib
from bs4 import BeautifulSoup


def get(url):
	agent = ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 '
		'(KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31')

	# try:
	headers = {'User-Agent' : agent}

	req = urllib2.Request(url, headers=headers)
	return urllib2.urlopen(req, timeout=16)

def download_page(url, filename):
	response = get(url)
	with open(filename, 'wb') as f:
		f.write(response.read())


if __name__ == '__main__':
	# Initial download so I can work localy.
	# url = ('http://msdn.microsoft.com/en-us/library/'
	# 	'windows/desktop/dd375731(v=vs.85).aspx')
	# download_page(url, 'vk_codes.html')

	with open('vk_codes.html', 'rb') as f:
		soup = BeautifulSoup(f.read(), 'html5lib')


	key_names = []
	vk_values = []
	table = soup.find('table')
	tbody = soup.find('tbody')
	for row in tbody.find_all('tr')[1:]:
		key_name = row.find('p')
		key_names.append(key_name.get_text())
		vk_values.append(row.find_all('dt')[-1].get_text())

	# print map(lambda x: x.lower().encode('ascii'), vk_values)		
	with open('vk_values.json', 'wb') as f:
		f.write(json.dumps(vk_values))

	with open('key_names.json', 'wb') as f:
		f.write(json.dumps([i.replace('key', '').strip().replace(' ', '_').lower()
			for i in key_names]))
