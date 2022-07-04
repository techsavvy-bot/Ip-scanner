def blackListed():
    textfile = open('full_blacklist_database.txt','r')
    data = textfile.read().splitlines()
    data = data[15:]
    n = data.__len__()
    for i in range(0,n):
        data[i] = data[i].split()[0]
    textfile.close()

    with open('ip_complete.csv', 'w') as f:
        for ips in data:
            f.write(ips + '\n')

blackListed()

def update():
    import requests
    from bs4 import BeautifulSoup
    url ='https://myip.ms/files/blacklist/csf/latest_blacklist.txt'
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')

    get = soup.get_text()

    get = get.split()
    get = get[118:]
    print(get)
    with open('ip_complete.csv','a') as f:
        for ips in get:
            f.write(ips + '\n')
    # ipList = soup.select(".row_name")
    # print(ipList)
    # with open('ip_output.csv', 'w') as f:
    #     for ips in ipList:
    #         f.write(ips.find('a').text + '\n')