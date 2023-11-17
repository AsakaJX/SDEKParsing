from bs4 import BeautifulSoup
import requests
import sys
import re

def parse(orderID, element):
    source = requests.get(f'https://maintransport.ru/transportnye-kompanii/sdek/tracking?track={orderID}').text
    soup = BeautifulSoup(source, 'lxml')

    # parsing
    search_result = soup.find_all("div", class_="tracking-main-param wide smallbm")
    if (element >= len(search_result)):
        print("There's no element with that element_id!")
        sys.exit(1)
    # applying regex search on our choosen element
    regex = "<\\/strong>(.*)<\\/div>"
    if ("<span class=\"col-xs-6 nopadding\">" in str(search_result[element])):
        regex = "<span class=\"col-xs-6 nopadding\">(.*)<\\/span>"

    search_result_normalized = re.search(regex, str(search_result[element])).group(1)

    if (search_result_normalized == ""):
        search_result_normalized = "result is empty or package id is invalid"

    return search_result_normalized

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        sys.exit("Not enough arguments!")

    PACKAGE_ID = str(sys.argv[1])
    ELEMENT_ID = int(sys.argv[2])

    result = parse(PACKAGE_ID, ELEMENT_ID)
    print(result)
