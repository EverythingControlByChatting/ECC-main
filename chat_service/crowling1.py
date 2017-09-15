import requests
from bs4 import BeautifulSoup
from . import GPS

def crowlier(context):
    req = requests.get('http://www.diningcode.com/list.php?query='+ str(context))

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    list_name = soup.select(".dc-restaurant-name")
    list_address = soup.select("dc-restaurant-info")
    lists_name = []
    for list1 in list_name:
        lists_name.append(list1.text.strip('\n'))
    address = []
    for addr in list_address:
        address.append(addr.select('.dc-restaurant-info')[1])
    
    lists_address = []
    for add in address:
        data = add.select('.dc-restaurant-info-text')[0].text
        lists_address.append("http://map.daum.net/?q="+GPS.getGPS_coordinate(data))
   
    return lists_name, lists_address

if __name__ == "__main__":
    crowlier(context)