import requests
from bs4 import BeautifulSoup
import replit
from datetime import datetime
import pytz

replit.clear()

baseURL = 'https://www.asx.com.au/asx/markets/equityPrices.do?by=asxCodes&asxCodes='

betashares = ["GEAR", "MNRS", "NDQ", "ETHI", "QLTY", "ASIA", "HACK", "RBTZ", "FAIR", "UMAX", "QUS", "A200", "EX20", "EINC", "WRLD", "QOZ", "QFN", "INCM", "QAU", "SMLL", "HVST", "HEUR", "QRE", "CRED", "DRUG", "USD", "POU", "BNDS", "HJPN", "EEU", "QPON", "BNKS", "FOOD", "AAA", "GBND", "IIND", "F100", "DHHF", "DGGF", "DZZF", "DBBF", "AGVT", "OOO", "QCB", "FUEL", "QAG", "BEAR", "BBUS", "BBOZ", "AUDS", "RINC", "GGUS", "GLIN", "RENT", "YANK", "AUST", "YMAX", "HBRD", "DMKT", "EMMG"]

lastDict = {}
last = []

now = datetime.now(pytz.timezone('Australia/Sydney'))

print("Last price from ASX on: " + now.strftime("%Y-%m-%d %H:%M:%S") + " (Sydney time)")

for i in betashares:
  tickerUrl = baseURL + i
  page = requests.get(tickerUrl)
  soup = BeautifulSoup(page.content, 'html.parser')
  table = soup.find("td",{"class":"last"})
  val = table.text.strip()
  last.append(val)
  lastDict[i] = val
  print(i + ": $" + val)

print(last)
print(lastDict)

# https://realpython.com/beautiful-soup-web-scraper-python/