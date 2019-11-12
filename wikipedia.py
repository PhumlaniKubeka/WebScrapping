from bs4 import BeautifulSoup
import requests
import csv

url = 'https://fbref.com/en/comps/9/Premier-League-Stats'


source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('epl_stats.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['team', 'apps','wins','draws','losses','goals_for','goals_against','goal_diff','attendance'])
# stats_table = soup.find('tbody')
# team,apps, wins,draws,losses,goals_for,goals_against, = [] ,[]
for i in range(19):
    for stats_table in soup.find_all('tbody'):
        team = stats_table.select('tr')[i].select('td')[0].get_text(strip=True)
        apps = stats_table.select('tr')[i].select('td')[1].get_text(strip=True)
        wins = stats_table.select('tr')[i].select('td')[2].get_text(strip=True)
        draws = stats_table.select('tr')[i].select('td')[3].get_text(strip=True)
        losses = stats_table.select('tr')[i].select('td')[4].get_text(strip=True)
        goals_for = stats_table.select('tr')[i].select('td')[5].get_text(strip=True)
        goals_against = stats_table.select('tr')[i].select('td')[6].get_text(strip=True)
        goal_diff = stats_table.select('tr')[i].select('td')[7].get_text(strip=True)
        attendance =stats_table.select('tr')[i].select('td')[12].get_text(strip=True)
       
    csv_writer.writerow([team, apps,wins,draws,losses,goals_for,goals_against,goal_diff,attendance])
csv_file.close()