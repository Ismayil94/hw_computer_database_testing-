import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_table_data(url):
    """
    Function for parsing table data:
        input: Target url
        return: List of dictionaries where dictionary contains one row data of table
    
    """

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    data = []

    table_rows = soup.find('tbody').find_all('tr') # Finding all table rows inside of tbody tag
    for row in table_rows:
        item = {}
        columns = row.find_all('td')

        item['name'] = columns[0].text
        item['company'] = columns[3].text
        
        if '-' in columns[1].text:
            item['introduced'] = datetime(800,1,1,1,1,1,1,) # Alternative for sorting by datetime object
            item['introduced_real'] = None 
        else:
            item['introduced'] = datetime.strptime(columns[1].text, '%d %b %Y')
        
        if '-' in columns[2].text:
            item['discontinued'] = datetime(800,1,1,1,1,1,1,) # Alternative for sorting by datetime object
            item['discontinued_real'] = None
        else:
            item['discontinued'] = datetime.strptime(columns[2].text, '%d %b %Y')
        
        data.append(item)
    
    req.close()

    return data
