import os
import urllib
import datetime
from shutil import copyfile
from bs4 import BeautifulSoup

with open('website_pull.html') as f:
    soup = BeautifulSoup(f, 'html.parser') 

tables = soup.find_all('table')

date = tables[0].caption.text.split(' ')[-1]
date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%d/%m/%Y')
date = date.replace('/', '-')

copyfile('website_pull.html', f'website-snapshots/{date}.html')

print(f'Copied snapshot from {date}')