import  requests as re
import datetime as dt
import json

api = "api"
URL_template = "https://newsapi.org/v2/everything?"

'''
url = https://newsapi.org/v2/everything?
      q=Dave+toilet+other&
      from=2023-10-09&
      apiKey=14d5c81c097e493cb4fe3dba59774c9f
'''
def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    global URL_template

    lookback_days = int(lookback_days)

    if news_keywords == []:
        raise ValueError
    
    for keyword in news_keywords:
        if not(keyword.isalnum()):
            raise ValueError

    if lookback_days < 0:
        lookback_days = 10
    
    q = "q=" + "+".join(news_keywords) + "&"
    end_date = dt.date.today() - dt.timedelta(days=lookback_days)
    end_date = 'from=' + end_date.strftime("%Y-%m-%d") + "&"
    api = "apiKey=" + api_key
    url = (URL_template + q + end_date + api)
    response = re.get(url)
    data = response.json()
    return [x for x in data['articles']]
    
if "__main__" == __name__:
    print(fetch_latest_news(api,["technology@"], lookback_days=7))