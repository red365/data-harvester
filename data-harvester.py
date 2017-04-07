import sys
import datetime
import urllib
from football_utils import get_json

def store_data(comp_id, directory, table_name, table_type, show_ha):
    
    table = open('/home/rob/Scripts/python/data-harvester/data/' + directory + '/comp-' + str(comp_id) + '-' + str(datetime.date.today()) + '-' + table_name + '.json', 'w')
    if directory == "tables":
        table.write(str(get_json("http://www.footballwebpages.co.uk/league.json?comp=" + str(comp_id) + "&sort=" + table_type + "&showHa=" + show_ha + "" )))
    else:
        table.write(str(get_json("http://www.footballwebpages.co.uk/form.json?comp=" + str(comp_id) + "&type=" + table_name + "" )))
    table.close

def data_harvester():
    for i in range(21):
        if i == 0:
            i += 1
        store_data(i, "tables", "ALL", "normal", "yes")
        store_data(i, "tables", "HOME", "home", "no")
        store_data(i, "tables", "AWAY", "away", "no")
        store_data(i, "form", "all", "...", "...")
        store_data(i, "form", "home", "...", "...")
        store_data(i, "form", "away", "...", "...")
                
data_harvester()
print "done"
