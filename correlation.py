from bokeh.plotting import figure, output_file, show, vplot
import statistics as st
import matplotlib.pyplot as plt
import numpy as np
import datetime, calendar
import csv

def main():
    c = getTemps()
    crimes = getFA()
    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    days = [datetime.date(2015,month,day) for month in range(1,13) for day in range(1,months[month]+1)]
##    for month in months.keys():
##        for day in range(1,months[month]+1):
##            days.append(month * 100 + day)

    print len(days)
    print len(crimes.values())
    print len(crimes.keys())
    createBokehPlots(days,crimes,c)
##    plt.plot(days, c, color='r', label="Max Temp")
##    plt.show()
    print "Correlation of Weather and Felony Assaults: ", st.correlation(c,crimes.values())

def createBokehPlots(days,crimes,c):
    output_file("nyc.html")
    s1 = figure(plot_width=800, plot_height=250,  x_axis_label = "Date", y_axis_label = "Number of Felony Assaults",x_axis_type="datetime")
    s1.line(days,crimes.values(), line_width=2, line_color="orange")
    s1.circle(days, crimes.values(), fill_color="white", size=8)
    s1.title = "Felony Assaults"

    s2 = figure(plot_width=800, plot_height=250, x_axis_label = "Date", y_axis_label = "Weather", x_axis_type="datetime")
    s2.line(days,c, line_width=2,  line_color="green")
    s2.circle(days, c, fill_color="white", size=8)
    s2.title = "Temperature"

    s3 = figure(plot_width=800, plot_height=250, x_axis_label = "Date", x_axis_type="datetime")
    s3.line(days, crimes.values(), line_width=2,  line_color="purple")
    s3.line(days,c, line_width=2,  line_color="green")
    s3.title = "Temperature and Felony Assaults in 2015 in NYC"
    
    p = vplot(s1, s2, s3)
    show(p)

def getFA():
    f = open("FelonyIncidentsNYC.csv", 'r')
    reader = csv.DictReader(f)
    counts = {}
    months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    for row in reader:
        if(len(row['Occurrence Month']) > 0 and row['Occurrence Month'] != 'NA'):
            date = str(months[row['Occurrence Month']])+'/'+str(row['Occurrence Day'])
            counts[date] = counts.get(date,0) + 1
    f.close()
    print counts
    return counts

def getTemps():
    f = open('weather.txt','r')
    temps = []
    f.next()
    for row in f:
        line = row.split(',')
        temps.append(int(line[1].strip('\n')))
    f.close()
    return temps
    
main()
