import os
class Config:
        '''
        General configuration parent class
        '''
        NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
        SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
        ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'
        TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&pageSize={}&apiKey={}'

class ProdConfig(Config):
        '''
        Production  configuration child class

        Args:
        Config: The parent configuration class with General configuration settings
        '''
        pass

class DevConfig(Config):
        '''
        Development  configuration child class

        Args:
        Config: The parent configuration class with General configuration settings
        '''

        DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
