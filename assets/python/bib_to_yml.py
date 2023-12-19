import bibtexparser
import yaml
import requests

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
            'doi': entry.get('DOI', ''),
            'type': None,
        }

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
        
        if not entry_dict['type'] == 'abstract':
            doi = get_doi_crossref(entry_dict['title'])
            entry_dict['doi'] = doi
        # Remove empty fields
        entry_dict = {k: v for k, v in entry_dict.items() if v}

        entries.append(entry_dict)

    # Write the YAML file
    with open('../_data/publications.yml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(entries, yaml_file, default_flow_style=False, allow_unicode=True)
        #yaml_file.write("\n")  # Add an empty line between entries

    print('BibTeX to YAML conversion complete. Output saved as publications.yml.')

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

if __name__ == "__main__":
    main()