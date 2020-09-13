import requests
from bs4 import BeautifulSoup
import shadow_useragent

ua = shadow_useragent.ShadowUserAgent()
my_user_agent = ua.percent(0.05)

protocols = ["HTTPS","HTTP","SOCKS5"]

headers = {
   'User-Agent': '{}'.format(my_user_agent),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

url = "https://spys.one"

r = requests.get(url,headers = headers)
soup = BeautifulSoup(r.text,'html.parser')

proxies = []

def listOfProxies(n=0):
	for line in soup.find_all('tr',{"class":"spy1xx"}):
		for k,td in enumerate(line.find_all('td')[:2]):
			if k==0:
				proxies.append({"addr":td.text})
			else:
				proxies[-1]["protocol"] = td.text
	if n==0 or n>len(proxies):
		return proxies
	return proxies[:n]

if __name__ == "__main__":
	for elem in listOfProxies():
		print(elem)