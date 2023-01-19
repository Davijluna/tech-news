import requests
import time
from parsel import Selector


# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        responce = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        responce.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return responce.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css(".entry-title a::attr(href)").getall()
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
