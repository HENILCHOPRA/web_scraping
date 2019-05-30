#Source of information "www.howstat.com"
#Packages used:
#               BeautifulSoup4
#               lxml
#Code By: HENIL CHOPRA
#Date: 30-05-2019
#Task: Assignment-1

#######################################################################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import *

def get_details(link):                                               #get Detailed Score Card of Player
    html=urlopen(link)
    obj1=BeautifulSoup(html,"lxml")
    div = obj1.find("div", class_="panel-container")                 #get the div containing score table
    rows = div.find("table", class_="TableLined").findAll("tr")[1:]  #get the rows of score table
    cum=0
    print("\t\tYear\tRuns\tcumulative score")
    print("----------------------------------------------------------")
    for row in rows[0:-1]:
        td = row.findAll("td")
        cum+=int(td[8].text.strip())                                 #Find Cumulative Score
        print("\t\t"+td[0].text.strip(),"\t", td[8].text.strip(),"\t\t",cum)
        print("----------------------------------------------------------")
    print("\t\t(OverAll)\t\t",cum)

####################################################################################################

if (__name__=="__main__"):
    c=65
    j=0
    for i in range(0,26):                                            #Iterate through A-Z names of Cricketers
        link="http://www.howstat.com/cricket/Statistics/Players/PlayerList.asp?Country=ALL&Group="+chr(c+i)
        html=urlopen(link)
        Bsobj=BeautifulSoup(html,"lxml")
        table = Bsobj.find("table", class_="TableLined")
        rows = table.findAll("tr")[2:]
        for row in rows[:-1]:
            col4 = row.findAll("td")[4]                              #Find number of ODIs played by Player
            ODIs = 0
            try:
                ODIs = int(col4.text)
            except:
                ODIs = 0
            if (ODIs == 0):                                          #Continue if Player never Played ODI
                continue
            col1 = row.find("a")
            name = col1.text
            uid = col1["href"][-4:]                                  #Find UID of Player from href link
            print(name + ":\n")
            try:
                get_details("http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=" + uid)
                pass
            except URLError as e:
                print("No RECORD FOUND")



