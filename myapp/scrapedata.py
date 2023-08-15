#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from threading import Thread
from subprocess import Popen, DEVNULL

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        thread = Thread(target=run_scraping_script)
        thread.start()
    
    execute_from_command_line(sys.argv)


def run_scraping_script():
    """Run the scraping script."""
    # Define API Key and Results per Request
    api_key = '7fbc388e783dedcc04a140d9c35ec7bd'
    num_results_per_request = 25
    total_results = 50

    # Define Author IDs and CSV File Names
    authors = {
        '36656106400': 'author1_papers.csv',
        '57190968285': 'author2_papers.csv',
        '36471236100': 'author3_papers.csv',
        # Add more author IDs and filenames as needed
    }

    for author_id, filename in authors.items():
        # Make API Requests within the Loop
        query = f'AU-ID({author_id})'
        offset = 0

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Authors', 'Publication Date', 'DOI', 'Source'])

            while offset < total_results:
                url = f'http://api.elsevier.com/content/search/scopus?query={query}&apiKey={api_key}&count={num_results_per_request}&start={offset}'

                response = requests.get(url)
                data = response.json()

                if 'search-results' in data and 'entry' in data['search-results']:
                    entries = data['search-results']['entry']
                    for entry in entries:
                        title = entry['dc:title']
                        authors = entry.get('dc:creator', 'N/A')
                        publication_date = entry.get('prism:coverDate', 'N/A')
                        doi = entry.get('prism:doi', 'N/A')
                        source_title = entry.get('prism:publicationName', 'N/A')

                        writer.writerow([title, authors, publication_date, doi, source_title])

                    offset += num_results_per_request
                else:
                    break

        print(f"Results for Author ID {author_id} saved to {filename}.")


if __name__ == '__main__':
    main()
