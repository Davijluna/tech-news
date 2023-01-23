from tech_news.database import search_news
from datetime import datetime
# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    response = {"title": {"$regex": title, "$options": "i"}}
    response_new = search_news(response)
    return [(new["title"], new["url"]) for new in response_new]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date = datetime.fromisocalendar(date).strftime("%d/%m/%Y")
        date_list = search_news({"timestamp": {"$eq": date}})
        return [
            (new["title"], new["url"])
            for new in date_list
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
