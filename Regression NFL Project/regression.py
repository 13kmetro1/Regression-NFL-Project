# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
team1 = "Arizona Cardinals"
team2 = 'Philadelphia Eagles'
opp = "Philadelphia Eagles"
switcher = {
     'Buffalo Bills' : 'bills.csv',
     'Miami Dolphins' : 'miami.csv',
     'New England Patriots' : 'patriots.csv',
     'New York Jets' : 'jets.csv',
     'Pittsburgh Steelers': 'steelers.csv',
     'Cleveland Browns': 'browns.csv',
     'Baltimore Ravens': 'ravens.csv',
     'Cincinnati Bengals':'bengals.csv',
     'Indianapolis Colts': 'colts.csv',
     'Tennessee Titans': 'titans.csv',
     'Houston Texans': 'texans.csv',
     'Jacksonville Jaguars': 'jaguars.csv',
     'Kansas City Chiefs': 'chiefs.csv',
     'Las Vegas Raiders': 'raiders.csv',
     'Denver Broncos': 'denver.csv',
     'Los Angeles Chargers': 'chargers.csv',
     'Washington Football Team': 'washington.csv',
     'New York Giants':'giants.csv',
     'Philadelphia Eagles': 'eagles.csv',
     'Dallas Cowboys':'dallas.csv',
     'Green Bay Packers': 'greenbay.csv',
     'Minnesota Vikings': 'minnesota.csv',
     'Chicago Bears': 'chicago.csv',
     'Detroit Lions':'detroit.csv',
     'New Orleans Saints': 'saints.csv',
     'Tampa Bay Buccaneers':'tampa.csv',
     'Atlanta Falcons': 'atlanta.csv',
     'Carolina Panthers':'panthers.csv',
     'Los Angeles Rams' : 'rams.csv',
     'Seattle Seahawks' : 'seahawks.csv',
     'Arizona Cardinals' : 'arizona.csv',
     'San Francisco 49ers' : '49ers.csv' }
avg = {
     'Buffalo Bills' : [4880, 313],
     'Miami Dolphins' : [4204,274],
     'New England Patriots' : [4328, 280],
     'New York Jets' : [2507, 213],
     'Pittsburgh Steelers': [4362,266],
     'Cleveland Browns': [4864, 287],
     'Baltimore Ravens': [4444, 252],
     'Cincinnati Bengals':[3507, 213],
     'Indianapolis Colts': [4897, 300],
     'Tennessee Titans': [5128, 310],
     'Houston Texans': [4634,255],
     'Jacksonville Jaguars': [4389, 261],
     'Kansas City Chiefs': [5579, 322],
     'Las Vegas Raiders': [5250,314],
     'Denver Broncos': [4272, 242],
     'Los Angeles Chargers': [5381, 328],
     'Washington Football Team': [4089, 260],
     'New York Giants':[3901, 237],
     'Philadelphia Eagles': [4239, 270],
     'Dallas Cowboys':[4838, 308],
     'Green Bay Packers': [5169, 294],
     'Minnesota Vikings': [5013, 301],
     'Chicago Bears': [4158, 263],
     'Detroit Lions': [4570, 290],
     'New Orleans Saints': [4808, 296],
     'Tampa Bay Buccaneers':[4656, 279],
     'Atlanta Falcons': [4774, 295],
     'Carolina Panthers':[4628, 279],
     'Los Angeles Rams' : [5062, 295],
     'Seattle Seahawks' : [5038, 304],
     'Arizona Cardinals' : [5063, 320],
     'San Francisco 49ers' : [4738,283] }
from sklearn import linear_model
df = pandas.read_csv("/Users/kevinmetro/Regression-NFL-Project/Regression NFL Project/Schedules/"+switcher[team1])
x = df[['TotYd','1stD','oppd']]
y = df[['Tm']]
df1 = pandas.read_csv("/Users/kevinmetro/Regression-NFL-Project/Regression NFL Project/Schedules/"+switcher[team2])
x1 = df1[['TotYd','1stD','oppd']]
y1 = df1[['Tm']]
regr = linear_model.LinearRegression()
regr.fit(x,y)
predict = regr.predict([[(5063/13),(320/13),29]])
print(predict)
regr.fit(x1,y1)
predict = regr.predict([[(4239/13),(270/13),17]])
print(predict)   