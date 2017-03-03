import sys
import datetime
import urllib

def table_harvester():
    i = 1
    while i < 21:
        f = open('/home/rob/Scripts/python/data-harvester/data/tables/comp-' + str(i) + '-' + str(datetime.date.today()) + '.json', 'w')
        url = "http://www.footballwebpages.co.uk/league.json?comp=" + str(i) + "&showHa=yes" 
        feed = urllib.urlopen(url)
        page = feed.read()
        f.write(page)
        f.close
        i += 1

table_harvester()
