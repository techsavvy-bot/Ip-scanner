import requests
from bs4 import BeautifulSoup
url ='https://myip.ms/files/blacklist/csf/latest_blacklist.txt'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')

get = soup.get_text()

get = get.split()
get = get[118:]
print(get)
with open('ip_output.csv','w') as f:
    for ips in get:
        f.write(ips + '\n')
# ipList = soup.select(".row_name")
# print(ipList)
# with open('ip_output.csv', 'w') as f:
#     for ips in ipList:
#         f.write(ips.find('a').text + '\n')