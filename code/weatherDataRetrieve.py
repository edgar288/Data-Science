import matplotlib.pyplot as plt
import urllib2
import re


#A function that takes the kind of temperature ("Max", "Min", "Ave") and
#a URL and returns the temperature from that line.
def getTempFromWeb(kind,url):
     page = urllib2.urlopen(url)
     lines = page.readlines()
     for i in range(len(lines)):
          if lines[i].find(kind) >= 0:
               m = i
     searchObj = re.search('\d+', lines[m+2])
     if searchObj is None:
         return 0
     else:
         return int(searchObj.group(0))

def main():
     w = open('weather.txt','w')
     w.write("DATE   TEMP\n")
     #The url is made up of the prefix, year, and suffix:
     prefix = "http://www.wunderground.com/history/airport/KLGA/2015/"
     suffix = "/DailyHistory"
     months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}	
     for month in months.keys(): #For each month
          for day in range(1,months[month]+1):
               url = prefix+str(month)+'/'+str(day)+suffix  #Make the url
               M = getTempFromWeb("Max Temperature",url)   #Call the function to extract temp
               P = getTempFromWeb("Precipitation",url)   #Call the function to extract temp
               S = getTempFromWeb("Snow",url)   #Call the function to extract temp             
               w.write(str(month)+'/'+str(day)+','+str(M)+','+str(P)+','+str(S)+'\n') #Add the temp to the list
               
main()
