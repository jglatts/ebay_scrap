#!/usr/bin/env python
#
# Author: John Glatts
# This is a program for searching\scraping EBAY.
# Search for Products, and see when\how much they sold for.
#
#
import requests
from bs4 import BeautifulSoup


def bayscrap():
    """ Get some info from EBAY with requests and bs4. """

    check_words = ['yes', 'YES', 'Yes']
    file = open("test.txt", "w")

    while True:
        try:
            print('\nWhat Do You Want To View From Ebay?')
            search = input()
            url = 'https://www.ebay.com/sch/' + search

            # Add headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
            source_code = requests.get(url, headers=headers)  # pass the url to requests, HTTP for humans
            plain_text = source_code.text

            # Display findings
            soup = BeautifulSoup(plain_text, "html.parser")  
            for items in soup.find_all("div", {"class": "s-item__info clearfix"}):
                # Find the links
                for links in items.find_all("a", href=True):
                    pass    
                print('\n' + items.get_text())
                print(links['href'])
            print('\n\n View sold listings for %s?' % search.title())
            check = input()
            if check in check_words:
                soldlistings(search)
            else:
                print('\nOK!\n')
                return

        except KeyboardInterrupt:
            print('\n\n\n\tProgram Canceled\n\n\n')
            return


def soldlistings(search_item):
    """ Scrap EBAY for sold items of the search product.
    This changes the url to find the sold listings.
    New URL will be fed to requests\bs4.  """

    print('\nDisplaying Sold Items For:' + ' ' + search_item.title() + '\n')
    sold_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + search_item + '&_sacat=0&LH_Sold=1&_dmd=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    src_sold = requests.get(sold_url, headers=headers)  # pass the url to requests, HTTP for humans
    bs4_text = src_sold.text

    # Throw findings to bs4 then display
    sold_soup = BeautifulSoup(bs4_text, 'html.parser')
    for sold in sold_soup.find_all("li", {"class": "s-item"}):
        for links in sold.find_all("a", href=True):
            pass
        print('\n' + sold.get_text())
        print(links['href'])


bayscrap()
