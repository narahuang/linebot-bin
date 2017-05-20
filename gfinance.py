#!/usr/bin/python3
# Simple script to parse company description from Google Finance
#

import requests
from bs4 import BeautifulSoup
#import urllib.parse
import sys

def get_company_name(stock):
    baseurl= 'https://www.google.com/finance?q='
    url = baseurl+stock
    head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url, headers=head)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('div', class_="appbar-snippet-primary")
    return name.span.text

def get_company_summary(stock):
    baseurl= 'https://www.google.com/finance?q='
    url = baseurl+stock
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    summary = soup.find('div', 'companySummary')
    return summary.contents[0]

if __name__ == '__main__':
    stock = sys.argv[1]
    baseurl= 'https://www.google.com/finance?q='
    url = baseurl+stock
    print(get_company_summary(url))
    print(get_company_name(url))
