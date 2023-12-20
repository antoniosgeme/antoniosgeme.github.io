import serpapi
import requests
from bs4 import BeautifulSoup
import time
import sys

if len(sys.argv) > 1:
    input_value = sys.argv[1]
    print(f"Input value: {input_value}")
else:
    print("No input value provided.")

params = {
  "api_key": input_value,
  "engine": "google_scholar_author",
  "hl": "en",
  "author_id": "tQpJjzwAAAAJ&hl=en"
}

mysearch = serpapi.search(params)
results = mysearch.as_dict()
articles = results["articles"]
titles = [article["title"] for article in articles]

with open('assets\\CV\\references.bib', 'w', encoding='utf-8') as bibfile:
  for (i,title) in enumerate(titles):
    print("Finding bib entry " + str(i+1) + " of " + str(len(titles)))
    time.sleep(5) # Wait a bit so we do not get banned by google scholar
    params = {
      "api_key": input_value,
      "engine": "google_scholar",
      "q": title,
      "hl": "en"
    }

    mysearch = serpapi.search(params)
    results = mysearch.as_dict()
    result_id = results['organic_results'][0]['result_id']

    params = {
      "api_key": input_value,
      "engine": "google_scholar_cite",
      "q": result_id
    }

    mysearch = serpapi.search(params)
    results = mysearch.as_dict()
    url = results['links'][0]['link']

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        bibfile.write(str(soup))