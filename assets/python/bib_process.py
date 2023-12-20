import pybtex.database as pyb

def add_keyword_to_entries(bib_file_path):
    # Load the BibTeX file
    bib_data = pyb.parse_file(bib_file_path)

    # Define the keywords to add
    keyword_to_add = "baps"

    # Iterate through entries and add keyword based on conditions
    for entry in bib_data.entries.values():
        journal = entry.fields.get('journal', '')
        booktitle = entry.fields.get('booktitle', '')
        if "Bulletin of the American Physical Society" in journal or "APS Division of Fluid Dynamics Meeting Abstracts" in booktitle:
            entry.fields['keyword'] = keyword_to_add

    # Save the modified BibTeX file
    bib_data.to_file(bib_file_path)

if __name__ == "__main__":
    bib_file_path = "../CV/references.bib"  # Specify the path to your .bib file
    add_keyword_to_entries(bib_file_path)
