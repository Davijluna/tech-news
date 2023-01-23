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
        date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        date_list = search_news({"timestamp": {"$eq": date}})
        return [
            (date_list["title"], date_list["url"])
            for date_list in date_list
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    new = []
    reponse = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for index in reponse:
        new.append((index["title"], index["url"]))
    return new


# Requisito 9
def search_by_category(category):

    new = []
    response = search_news({"category": {"$regex": category, "$options": "i"}})
    for index in response:
        new.append((index["title"], index["url"]))
    return new
    """Seu código deve vir aqui"""
