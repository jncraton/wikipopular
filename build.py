import urllib.request
from urllib.parse import quote_plus, unquote_plus
import json
from time import perf_counter
from bs4 import BeautifulSoup

def get_cur_pop():
  index = 'https://en.wikipedia.org/w/api.php?action=parse&page=User:Community_Tech_bot/Popular_pages&format=json&prop=links&redirects=1'
  
  f = urllib.request.urlopen(index)
  index = json.loads(f.read().decode())
  
  for link in index['parse']['links']:
    link = link['*']
    if '/Popular pages' in link:
      page = 'https://en.wikipedia.org/w/api.php?action=parse&page=%s&format=json&prop=text&redirects=1' % quote_plus(link)
      f = urllib.request.urlopen(page)
      res = json.loads(f.read())

      html = res['parse']['text']['*']

      soup = BeautifulSoup(html,features='html.parser')

      try:
        for row in soup.find('table',class_='wikitable').find('tbody').find_all('tr'):
          cells = row.find_all('td')
          if len(cells) < 2: continue

          try:
            href = cells[1].find('a')['href']
          except:
            # We end up here if the link doesn't exist. Some of the pages are buggy, and we just skip that entry
            continue
          try:
            views = cells[2].find('a').get_text()
          except AttributeError:
            views = cells[2].get_text()
  
          views = int(views.replace(',', ''))

          if not '&redlink=1' in href and views > 10000:
            page = unquote_plus(href[6:])
            print("%d\t%s" % (views, page))
      except (AttributeError, TypeError) as e:
        print(e)
        print(link)
        exit(1)

get_cur_pop()