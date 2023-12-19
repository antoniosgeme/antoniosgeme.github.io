import bibtexparser
import yaml
from scholarly import scholarly
import requests
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.error import HTTPError

def get_doi(title):
    # Replace spaces with '+' for the query
    query = title.replace(' ', '+')

    # Crossref API URL for works
    url = f"https://api.crossref.org/works?query={query}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        items = data.get('message', {}).get('items', [])
        if items:
            for item in items:
                if 'title' in item and item['title'][0].lower() == title.lower():
                    return item.get('DOI', 'DOI not found')
        else:
            return "No results found"
    else:
        return "Failed to retrieve data"
    
    return "Failed to retrieve data"



def retrieve_bibtex_from_doi(doi):
    BASE_URL = 'http://dx.doi.org/'

    url = BASE_URL + doi
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')

    try:
        with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
            return bibtex
    except HTTPError as e:
        if e.code == 404:
            return 'DOI not found.'
        else:
            return 'Service unavailable.'


author_name = "Antonios Gementzopoulos"
search_author = scholarly.search_author(author_name)
author = scholarly.fill(next(search_author),["publications"])
for pub in author['publications']:
    title = pub['bib']['title']
    doi = get_doi(title)
    print(title,doi)
    #bibtex_entry = retrieve_bibtex_from_doi(doi)
    #print(bibtex_entry)



