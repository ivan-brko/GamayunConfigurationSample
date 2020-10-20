import requests
import json
from bs4 import BeautifulSoup
from gamayun.gamayun_utils import report_result_with_maps_only
from gamayun.gamayun_utils import report_error
from gamayun.gamayun_utils import run_gamayun_script_logic

def parse_single_entry(entry):
    result = dict()
    
    model = entry.find("h2", class_="cldt-summary-makemodel sc-font-bold sc-ellipsis").text + " " + entry.find("h2", class_="cldt-summary-version sc-ellipsis").text
    result["model"] = model
    
    link_ending = entry.find(lambda tag: tag.has_attr("data-item-name") and tag["data-item-name"] == "detail-page-link")["href"]
    link = "https://www.autoscout24.hr" + link_ending
    result["link"] = link
    
    price = entry.find("span", class_="cldt-price sc-font-xl sc-font-bold").text.strip()
    result["price"] = price
    
    vehicle_details = entry.find(lambda tag: tag.has_attr("data-item-name") and tag["data-item-name"] == "vehicle-details")
    for detail in vehicle_details.find_all("li"):
        if detail.has_attr("data-type"):
            string_to_be_erased = "Više informacija o službenoj potrošnji goriva i CO2 emisiji novih putničkih vozila možete dobiti iz vodiča o potrošnji goriva i CO2 emisiji novih putničkih vozila. Vodič je besplatno dostupan na svim prodajnim mjestima i kod Deutsche Automobil Treuhand GMBH na www.dat.de."
            result[detail["data-type"]] = detail.text.strip().replace(string_to_be_erased, "")
    
    return result

def job_logic():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:81.0) Gecko/20100101 Firefox/81.0'}
    page = requests.get(url = "https://www.autoscout24.hr/lst?body=6&dtr=s&page=1&fregfrom=2006&ipc=HP-AltSearch&kmto=80000&results=20&ipl=bodytype-limousine&pricefrom=1000&pic=True&sort=threetier,price&ustate=N,U&atype=C", headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = [parse_single_entry(entry) for entry in soup.find_all("div", class_ = "cldt-summary-full-item-main")]
    report_result_with_maps_only(result)


run_gamayun_script_logic(job_logic)
