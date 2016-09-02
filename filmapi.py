from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

film_2002 = []


for film in json_obj:
	if film["release_year"] == "2002":
		if film["title"] not in film_2002:
			film_2002.append(film["title"])
			film_2002.sort()


print film_2002_sort