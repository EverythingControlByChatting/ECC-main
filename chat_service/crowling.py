import requests
from bs4 import BeautifulSoup
from . import coordinate

def crowlier_lunch(context):
    req = requests.get('http://www.diningcode.com/list.php?query='+ str(context))

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    list_name = soup.select(".localeft-cont > .lc-list > #div_list > li > a > .btxt")
    list_info = soup.select(".localeft-cont > .lc-list > #div_list > li > a > .stxt")
    list_address = soup.select(".localeft-cont > .lc-list > #div_list > li > a > span:nth-of-type(5)")
    lists_name = []
    for list1 in list_name:
        lists_name.append(list1.text.strip('\n'))
    print(list_address)
    
    address = []
    for addr in list_address:
        address.append(addr.text.strip())
    
    lists_address = []
    for addr in address:
        data = addr
        lists_address.append("http://map.daum.net/?q="+coordinate.get_address(data))
   
    lists_info = []
    for list1 in list_info:
        lists_info.append(list1.text)
    lists_name_info = []

    for i in range(0, len(lists_info)):        
        lists_name_info.append(lists_name[i]+"("+lists_info[i]+")")
    print(lists_name_info)    
    return lists_name_info, lists_address
    
def lunch_category():
    req = requests.get('http://www.diningcode.com/isearch.php?')

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    list_category = soup.select(".category-menu > .list > li > a")
    print(list_category)
    lists_category = []
    for i in range(0, len(list_category)):
        lists_category.append(list_category[i].text)
    
    return lists_category

if __name__ == "__main__":
    crowlier_lunch(context)
    crowlier_category()