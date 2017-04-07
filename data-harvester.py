import sys
import datetime
import urllib
from football_utils import get_json

def table_harvester():
    i = 1
    for i in range (3):
        table_all = open('/home/rob/Scripts/python/data-harvester/data/tables/comp-' + str(i) + '-' + str(datetime.date.today()) + '.json', 'w')
        page = get_json("http://www.footballwebpages.co.uk/league.json?comp=" + str(i) + "&showHa=yes" )
        page = str(page)
        table_all.write(page)
        table_all.close
#        table_home = open('/home/rob/Scripts/python/data-harvester/data/tables/comp-' + str(i) + '-' + str(datetime.date.today()) + '.json', 'w')
#        table_home.write(get_json("http://www.footballwebpages.co.uk/league.json?comp=" + str(i) + "&sort=home&showHa=no" ))
#        table_home.close
#        table_away = open('/home/rob/Scripts/python/data-harvester/data/tables/comp-' + str(i) + '-' + str(datetime.date.today()) + '.json', 'w')
#        table_away.write(get_json("http://www.footballwebpages.co.uk/league.json?comp=" + str(i) + "&sort=away&showHa=no" ))
#        table_away.close

table_harvester()
print "done"
