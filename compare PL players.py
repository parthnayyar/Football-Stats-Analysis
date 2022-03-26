import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import matplotlib.pyplot as plt


scrape_url= 'https://understat.com/league/EPL'

#establish connection b/w webpage and python notebook
page_connect = urlopen(scrape_url)

#using beautiful soup to get page source
page_html = BeautifulSoup(page_connect,'html.parser')

#finding the line we want
json_raw_string = page_html.findAll(name='script')[3].text[32:-4]

json_data = json_raw_string
json_data = json_data.encode('utf8').decode('unicode_escape')
json.loads(json_data)

epl_df = pd.json_normalize(json.loads(json_data))

players_list = epl_df['player_name'].to_list()
column_dict = {1:'games',
               2:'time',
               3:'goals',
               4:'xG',
               5:'assists',
               6:'xA',
               7:'shots',
               8:'key_passes',
               9:'yellow_cards',
               10:'red_cards',
               11:'npg',
               12:'npxG',
               13:'xGChain',
               14:'xGBuildup'}

while True:
    players_to_compare = []
    n = int(input("Enter number of players to compare (max 4): "))
    if n > 4 or n <= 0:
        continue
    for i in range(n):
        player = input("Enter player " + str(i + 1) + " name: ")
        while player not in players_list:
            print("No player with that name")
            player = input("Enter player " + str(i + 1) + " name: ")
        players_to_compare.append(player)
    print()
    for i in column_dict:
        print(i, column_dict[i])
    print()
    columns_to_compare = input("Enter column numbers to compare, seperated by commas (1,4,6,...): ")
    print()
    columns_to_compare = columns_to_compare.split(',')
    columns_to_compare = [int(i) for i in columns_to_compare]
    columns_to_compare = [column_dict[i] for i in columns_to_compare]
    columns_to_compare_dict = {}
    
    lp = len(players_to_compare)
    lc = len(columns_to_compare)
    
    for i in range(lp):
        columns_to_compare_dict[i] = epl_df.loc[epl_df.player_name == players_to_compare[i], columns_to_compare].values.flatten().tolist()
        columns_to_compare_dict[i] = [int(j) for j in columns_to_compare_dict[i]]
    
    bars = {}
    lp = len(players_to_compare)
    lc = len(columns_to_compare)
    
    if lp == 1:
        width = 0.8
    elif lp == 2:
        width = 0.4
    elif lp == 3:
        width = 0.3
    else:
        width = 0.2
        
    for i in range(lp):
        bars[i] = [j + (i*width) for j in range(lc)]

    for i in range(lp):
        plt.bar(bars[i], columns_to_compare_dict[i], width, label = players_to_compare[i])
    
    plt.ylabel("Players")
    plt.title("Comparison")
    plt.xticks([i+((lp-1)*width/2) for i in bars[0]] , columns_to_compare)
    plt.legend()
    plt.show()
