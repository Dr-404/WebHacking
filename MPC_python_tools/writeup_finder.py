#!/usr/bin/env python3
"""
Google Search Scraper for HackerOne Reports

This tool allows you to scrape Google search results to find reports on hackerone.com based on an intext query.
It supports scraping multiple pages and dynamically searching for topics using intext queries.

Usage:
    hackerone_scraper.py -q QUERY [-n NUM_PAGES] [-o OUTPUT_FILE]

Example:
    hackerone_scraper.py -q "graphql" -n 5 -o reports.txt

Options:
    -q, --query       The intext search query (e.g., "graphql", "XSS", etc.)
    -n, --num_pages   (Optional) The number of Google search result pages to scrape. Default is 5.
    -o, --output      (Optional) The file to save the output links. If not provided, outputs to console.

Note:
    Use responsibly and beware of Google’s scraping limitations.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import argparse
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class HackerOneScraper:
    def __init__(self, query, num_pages=5, output_file=None):
        self.query = query
        self.num_pages = num_pages
        self.output_file = output_file
        self.links = []

    def extract_links_from_page(self, start):
        """Extract links from a single Google search result page."""
        url = "https://www.google.com/search"
        params = {
            'q': self.query,
            'start': start
        }

        # Headers to mimic a browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        # Make the GET request
        response = requests.get(url, headers=headers, params=params)

        # Parse the HTML response
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all <a> tags in the result
        for link in soup.find_all("a"):
            href = link.get("href")
            # Check if 'url=' is in the href and process only those Google search result links
            if href and "/url?" in href:
                # Use regex to extract the real URL
                match = re.search(r'url=(https://hackerone.com/reports.+?)&', href)
                if match:
                    actual_url = match.group(1)
                    self.links.append(actual_url)

    def scrape(self):
        """Main logic to scrape multiple pages."""
        for page_num in range(self.num_pages):
            start = page_num * 10
            self.extract_links_from_page(start)

            # Sleep to avoid being blocked by Google
            time.sleep(2)

    def output_results(self):
        """Output the results to a file or console."""
        if self.output_file:
            with open(self.output_file, 'w') as f:
                for link in self.links:
                    f.write(link + '\n')
            print(Fore.GREEN + f"\nFound {len(self.links)} links. Saved to '{self.output_file}'.")
        else:
            if self.links:
                print(Fore.GREEN + "\nFound the following report links:")
                for link in self.links:
                    print(Fore.CYAN + link)
            else:
                print(Fore.RED + "\nNo report links found.")

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Google Search Scraper for HackerOne Reports")
    
    # Define arguments
    parser.add_argument('-q', '--query', type=str, required=True, help='The intext search query (e.g., "graphql", "XSS", etc.)')
    parser.add_argument('-n', '--num_pages', type=int, default=5, help='The number of Google search result pages to scrape. Default is 5.')
    parser.add_argument('-o', '--output', type=str, help='The file to save the output links. If not provided, outputs to console.')
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Create an instance of HackerOneScraper
    scraper = HackerOneScraper(f"site:hackerone.com intext:{args.query}", args.num_pages, args.output)
    
    # Run the scraper
    print(Fore.YELLOW + f"Searching for reports related to '{args.query}' on HackerOne...")
    scraper.scrape()
    scraper.output_results()

if __name__ == '__main__':
    main()
