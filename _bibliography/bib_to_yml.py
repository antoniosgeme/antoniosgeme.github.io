import bibtexparser
import yaml
from scholarly import scholarly

def main():

    # Load the BibTeX file
    with open('references.bib', 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Convert each entry to a dictionary
    entries = []
    for (i,entry) in enumerate(bib_database.entries):
        print("Processing entry " + str(i+1) + " of "+str(len(bib_database.entries)+1))

        entry_dict = {
            'title': entry.get('title', ''),
            'author': entry.get('author', ''),
            'journal': entry.get('journal', ''),
            'volume': entry.get('volume', ''),
            'number': entry.get('number', ''),
            'pages': entry.get('pages', ''),
            'year': entry.get('year', ''),
            'publisher': entry.get('publisher', ''),
            'type': None,
        }
        title = entry.get('title', '').strip()
        author = entry.get('author', '').split(' and ')[0] 

        doi = find_doi(title,author)
        if not doi == None:
            print("DOI search succesful")
            entry_dict['doi'] = f'https://doi.org/{doi}'
        else:
            print("DOI search unsuccesful")


        possible_abstract_names = [
            "Bulletin of the American Physical Society",
            "APS Division of Fluid Dynamics Meeting Abstracts"
                                ]
        
        if entry['ENTRYTYPE'] == 'article':
            entry_dict['type'] = 'journal'
        else:
            if (entry.get('journal', '') in possible_abstract_names
            or entry.get('booktitle', '') in possible_abstract_names):
                entry_dict['type'] = 'abstract'
            else:
                entry_dict['type'] = 'conference'
        
        # Remove empty fields
        entry_dict = {k: v for k, v in entry_dict.items() if v}

        entries.append(entry_dict)

    # Write the YAML file
    with open('../_data/publications.yml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(entries, yaml_file, default_flow_style=False, allow_unicode=True)
        #yaml_file.write("\n")  # Add an empty line between entries

    print('BibTeX to YAML conversion complete. Output saved as publications.yml.')


def find_doi(title, author):
    # Search Google Scholar
    search_query = scholarly.search_pubs(f'{title} {author}')
    
    try:
        # Fetch first publication result
        pub = next(search_query)
        
        # Retrieve and return DOI
        return pub.bib.get('doi', None)
    except StopIteration:
        # No results found
        return None

def find_doi_old(bibtex_entry):
    # Crossref API endpoint
    crossref_api = "https://api.crossref.org/works"

    # Extract title from BibTeX entry
    title = bibtex_entry.get('title', '').strip()

    # Query Crossref API
    response = requests.get(crossref_api, params={'query.title': title})

    if response.status_code == 200:
        results = response.json()['message']['items']
        for item in results:
            print(item['title'][0].lower())
            # Check if the title matches closely
            if 'title' in item and item['title'][0].lower() == title.lower():
                return item.get('DOI', None)
    return None


if __name__ == "__main__":
    main()