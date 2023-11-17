from bs4 import BeautifulSoup
import requests
import sys
import re
import json

dict = { "package_id": -1, "data": [] }
output = json.loads(json.dumps(dict))

def parse(orderID):
    source = requests.get(f'https://maintransport.ru/transportnye-kompanii/sdek/tracking?track={orderID}').text
    soup = BeautifulSoup(source, 'lxml')

    # parsing
    search_result = soup.find_all("div", class_="tracking-main-param wide smallbm")
    
    # updating json
    new_data = {}
    for i in range(len(search_result)):
        # applying regex search on our choosen element
        regex = "<\\/strong>(.*)<\\/div>"
        if ("<span class=\"col-xs-6 nopadding\">" in str(search_result[i])):
            regex = "<span class=\"col-xs-6 nopadding\">(.*)<\\/span>"

        element_name_normalized = str(re.search("<strong class=\"col-xs-6\">(.*)</strong>", str(search_result[i])).group(1)).strip()
        search_result_normalized = str(re.search(regex, str(search_result[i])).group(1)).strip().replace("<br/>", " ")

        if (search_result_normalized == ""):
            search_result_normalized = "empty or package id invalid"

        new_data[element_name_normalized] = str(search_result_normalized)
    
    output["data"].append(new_data)
    output_updated = json.loads(json.dumps(output))

    return output_updated

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        sys.exit("Not enough arguments!")

    PACKAGE_ID = str(sys.argv[1])
    output["package_id"] = PACKAGE_ID
    
    result = parse(PACKAGE_ID)
    print(json.dumps(result, indent=4, ensure_ascii=False))
