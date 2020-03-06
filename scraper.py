import requests, time
from bs4 import BeautifulSoup


#get_episode links

baseurl = "https://www.springfieldspringfield.co.uk/"
start = "episode_scripts.php?tv-show=bojack-horseman-2014"

response = requests.get(f'{baseurl}{start}')

soup = BeautifulSoup(response.text, "html.parser")

all_tags = soup.findAll('a')

ep_links = [] 


for tag in all_tags:

	if 'view_episode_scripts' in tag['href']:

		ep_links.append(tag['href'])

#Go to each and get ep text

fileToWrite = 'allEpisodes.txt'

with open(fileToWrite, 'w') as file:
	for link in ep_links:

		response = requests.get(f'{baseurl}{link}')

		pgSoup =  BeautifulSoup(response.text, "html.parser")

		divs = pgSoup.findAll('div')

		for div in divs:
			try:
				dvClass = div['class']
			except:
				dvClass = []
			
			if 'scrolling-script-container' in dvClass:
				breaks = div.findAll('br')
				for br in breaks:
					br.replace_with('\n')

				print(div.text.strip())
				file.write(div.text.strip())

		
		time.sleep(1)

