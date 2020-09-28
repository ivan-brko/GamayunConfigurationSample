import requests
import json
from bs4 import BeautifulSoup
from gamayun.gamayun_utils import report_result
from gamayun.gamayun_utils import report_error
from gamayun.gamayun_utils import run_gamayun_script_logic

def parse_single_entry(entry):
    # test if this entry contains comment (if it doesn't it is an ad so we skip it)
    if entry.find("a", class="comments") is not None:
        result = dict()
        result["title"] = entry.find("a", class_="title").text
        result["link"] = entry.find("a", class_="title")["href"]
        result["comments_link"] = entry.find("a", class_="comments")["href"]
        return json.dumps(result)
    else:
        return None

def job_logic():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:81.0) Gecko/20100101 Firefox/81.0'}
    page = requests.get(url = "https://old.reddit.com/r/programming/", headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = [x for x in [parse_single_entry(entry) for entry in soup.find_all("div", class_ = "top-matter")] if x is not None]
    report_result(result)

run_gamayun_script_logic(job_logic)
