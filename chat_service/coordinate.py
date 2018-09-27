import urllib.request
import urllib.parse
import json

def get_address(address):
    address = str(address)
    count = 0
    number = 0 
    print(address)
    list_str = []
    for mark in address:
        if address[number] == ' ':
             count = count + 1
        if count >= 1:
            if address[number] == ' ':
                list_str.append('+')
            else:    
                list_str.append(address[number])
            
        number = number + 1
    
        
    address = "".join(list_str)
    address = str(address)
    return address

if __name__ == "__main__":
    rtnText = get_address(address)