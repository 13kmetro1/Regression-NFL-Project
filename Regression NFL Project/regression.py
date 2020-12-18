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