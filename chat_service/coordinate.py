import urllib.request
import urllib.parse
import json

def get_address(address):
    address = str(address)
    addre = ['%','2','0']
    count = 0
    number = 0 

    for mark in address:
        if address[number] == ' ':
             count = count + 1
        if address[number] != ' ':    
            if(count > 1):
                addre += address[number]
        number = number + 1
        
    address = "".join(addre)
    return address

if __name__ == "__main__":
    rtnText = get_address(address)