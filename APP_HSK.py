# -*- coding: utf-8 -*-

import csv
import json

with open('/Users/francois/Documents/MacBook Pro 3/Documents UTBM/Cours UTSEUS/A1 - Data Science/Cours 2/APP HSK/HSK_Level_1_V2.csv', 'r') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)

    hsk = []

    for line in reader:
        order = line[0]
        hsk_level_order = line [1]
        word = line[2]
        pinyin = line [3]
        english = line [4]
        #append means add an element in a list
        hsk.append({'word':word, 'pinyin':pinyin, 'english':english})
print json.dumps(hsk)
#json est utilisé pour transformer le dictionary .py en language directement copiable pour créer un site internet


        
	
 