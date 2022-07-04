import requests
from bs4 import BeautifulSoup
url ='https://myip.ms/browse/scam'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
ipList = soup.select(".row_name")
print(ipList)
with open('ip_output.csv', 'w') as f:
    for ips in ipList:
        f.write(ips.find('a').text + '\n')