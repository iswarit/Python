import requests as req
from bs4 import BeautifulSoup as bs
import os
import subprocess


BASE_URL = 'http://dl.filmbaroon.net/serial/Sacred-Games/'


def download_files(links, idx):
	for link in links:
		subprocess.call([
			"aria2c",
			"-s",
			"16",
			"-x",
			"16",
			"-d",
			"season"+str(idx),
			link
		])


def main():
	for i in range(1,5):
		r = req.get(BASE_URL+'S0'+str(i)+'/480/')
		soup = bs(r.text, 'html.parser')
		link_ = []
		for link in soup.find_all('a'):
			if '.mkv' in link.get('href'):
				link_.append(BASE_URL++'S0'+str(i)+'/480/'+link.get('href'))
		if not os.path.exists('season'+str(i)):
			os.makedirs('season'+str(i))
		download_files(link_, i)



if __name__ == '__main__':
	main()