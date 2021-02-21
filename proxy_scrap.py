import requests
from bs4 import BeautifulSoup
from random import randint

url='https://www.sslproxies.org/'

def get_agent():
	uas_len=578
	return open('useragents.txt', 'r').readlines()[randint(1,uas_len)].split('\n')[0]

def scrap():
	proxies=list()
	html=requests.get(url, headers={'user-agent': get_agent()}).text
	soup=BeautifulSoup(html, 'html.parser')
	proxies_table=soup.find(id='proxylisttable')
	for row in proxies_table.tbody.find_all('tr'):
		proxies.append({
			'ip':row.find_all('td')[0].string, 
			'port':row.find_all('td')[1].string}
		)
	return proxies

def random_proxy():
	res=list()
	proxies=scrap()
	for proxy in proxies:
		res.append(proxy['ip']+':'+proxy['port'])
	return res

def main():
	proxies=random_proxy()
	print('[+] Your random proxies:')
	for proxy in proxies: print('[+]', proxy)
	print('there are', len(proxies), 'proxies')

if __name__=='__main__':
	main()