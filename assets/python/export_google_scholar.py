## This script finds all the google scholar entries of an author and 
# creates a bibtex file for them

import bibtexparser
import yaml
from scholarly import scholarly
import requests
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.error import HTTPError
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def main():
    author_name = "Antonios Gementzopoulos"
    search_author = scholarly.search_author(author_name)
    author = scholarly.fill(next(search_author),["publications"])
    with open('references_test.bib', 'w') as file:
        for pub in author['publications']:
            title = pub['bib']['title']
            doi = get_doi_crossref(title)
            if doi:
                bibtex_entry = retrieve_bibtex_from_doi(doi)
                file.write(bibtex_entry + "\n")

def get_doi_crossref(title):
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
            return None
    else:
        return None
    
    return None

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

def generate_bibtex_entry(pub):
    # Extract relevant information from the 'pub' dictionary
    title = pub['bib']['title']
    pub_year = pub['bib']['pub_year']
    publication_source = pub['bib']['citation']
    authors = ", ".join(pub['authors'])  # Join the list of authors into a comma-separated string

    # Generate a unique key based on the first author's last name and the publication year
    unique_key = f'{authors.split(",")[0].strip()}{pub_year}'

    # Construct the BibTeX entry
    bibtex_entry = f'@inproceedings{{{unique_key},\n'
    bibtex_entry += f'    author = {{{authors}}},\n'
    bibtex_entry += f'    title = {{{title}}},\n'
    bibtex_entry += f'    year = {{{pub_year}}},\n'
    bibtex_entry += f'    booktitle = {{{publication_source}}},\n'
    bibtex_entry += f'}}\n'

    return bibtex_entry

def extract_bibtex_from_url(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Locate the <pre> tag containing BibTeX information (adjust the class as needed)
            bibtex_tag = soup.find('pre', class_='bibtex-data')

            if bibtex_tag:
                # Extract the BibTeX data
                bibtex_data = bibtex_tag.get_text()
                return bibtex_data
            else:
                return "BibTeX data not found on the page."
        else:
            return f"Failed to retrieve the webpage (status code: {response.status_code})."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def get_google_scholar_url(article_title):
    try:
        # Format the article title for the Google Scholar search URL
        formatted_title = '+'.join(article_title.split())

        # Construct the Google Scholar search URL
        search_url = f'https://scholar.google.com/scholar?q={formatted_title}'

        # Send an HTTP GET request to the search result page
        response = requests.get(search_url)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Locate the title element (adjust the tag and class as needed)
            title_element = soup.find('h3', class_='gs_rt')

            if title_element:
                # Extract the link URL from the title's <a> tag
                link_url = title_element.find('a')['href']
                return link_url
            else:
                for a_tag in soup.find_all('a', href=True, text=True):
                    if article_title.lower() in a_tag.get_text().lower():
                        return a_tag['href']
                return "Failed"
        else:
            return f"Failed to retrieve the search result page (status code: {response.status_code})."
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    main()

