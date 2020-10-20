import requests
import json
from bs4 import BeautifulSoup
from gamayun.gamayun_utils import report_result_with_maps_only
from gamayun.gamayun_utils import report_error
from gamayun.gamayun_utils import run_gamayun_script_logic

def parse_single_entry(entry):
    result = dict()
    result["title"] = entry.text
    result["link"] = entry["href"]
    return result

def job_logic():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:81.0) Gecko/20100101 Firefox/81.0'}
    page = requests.get(url = "https://news.ycombinator.com/", headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = [parse_single_entry(x) for x in soup.find_all("a", class_ = "storylink")]
    report_result_with_maps_only(result)

run_gamayun_script_logic(job_logic)
