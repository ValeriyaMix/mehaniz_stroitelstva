#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    features = "html.parser"
    soup = BeautifulSoup(html, features)
    table = soup.find('table', class_='issues')
    rows = table.find_all('td')
    # print(table.prettify())
    print(rows)

    
def main():
    parse(get_html('http://ms.enjournal.net/archive/2017/'))


if __name__ == '__main__':
    main()