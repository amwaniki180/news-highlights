import urllib.request,json
from .models import Source,Articles

api_key = None
base_url = None
news_headlines_base_url = None
article_url= None

def configure_request(app):
    global api_key,base_url,article_url,news_headlines_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config["ARTICLES_BASE_URL"]
    news_headlines_base_url = app.config['TOP_HEADLINES_BASE_URL']
