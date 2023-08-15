# myapp/management/commands/scrape_data.py

import csv
import requests
from django.core.management.base import BaseCommand
from myapp.models import Lecturer
from myproject import settings

class Command(BaseCommand):
    help = 'Run the scraping script'

    def handle(self, *args, **options):
        api_key = 'your_api_key'
        num_results_per_request = 25
        total_results = 50

        authors = {
            '36656106400': 'author1_papers.csv',
            '57190968285': 'author2_papers.csv',
            '36471236100': 'author3_papers.csv',
            # Add more author IDs and filenames as needed
        }

        for author_id, _ in authors.items():
            self.run_scraping_script(author_id)

    def run_scraping_script(self, author_id):
        api_key = 'your_api_key'
        num_results_per_request = 25
        total_results = 50

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

                        lecturer = Lecturer(
                            title=title,
                            description=authors,
                            publication_date=publication_date,
                            doi=doi,
                            source_title=source_title
                        )
                        lecturer.save()

                    offset += num_results_per_request
                else:
                    break

        self.stdout.write(self.style.SUCCESS(f"Results for Author ID {author_id} saved to database."))
