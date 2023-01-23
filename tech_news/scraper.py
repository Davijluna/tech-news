import requests
import re
import time
from parsel import Selector

# from bs4 import BeautifulSoup


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
    responce = Selector(text=html_content)
    return responce.css(".next::attr(href)").get()
    """Seu código deve vir aqui"""


def remover_html_tags(text):
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)
# https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css("comment-list li").getall()) or 0
    summary = remover_html_tags(selector.css(".entry-content p").get()).strip()
    tags = selector.css(".post-tags li a::text").getall()
    category = selector.css(".meta-category .label::text").get()

    return {
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "comments_count": comments_count,
            "summary": summary,
            "tags": tags,
            "category": category
     }

# Requisito 5


def get_tech_news(amount):
    """Seu código deve vir aqui"""
