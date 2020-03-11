#!/usr/bin/python3
from bs4 import BeautifulSoup as BSHTML
from urllib.request import urlopen
import sys

URL="https://www.worldometers.info/coronavirus/"

#va por parametro
tipo=int (sys.argv[1])
#Tipo 0 --- Infectados
#Tipo 1 --- Muertos
#Tipo 2 --- Curados

def scrap(URL):
     prod = urlopen(URL)
     soup = BSHTML(prod,"html.parser")
     getdata =  soup.find_all("div",class_="maincounter-number")
     return (getdata[tipo].text).replace(',','') 


prod = scrap(URL)
print (prod)
