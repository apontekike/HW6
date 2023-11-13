import unittest
from datetime import datetime, timedelta, date
from newsapi import fetch_latest_news, api

class NewsApiTest(unittest.TestCase):

    def test_fetch_latest_news_no_keywords(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(api,[])

    def test_fetch_latest_news_lookback_days(self):
        # Set a custom lookback_days value
        lookback_days = 7
        end_date = date.today()
        start_date = end_date - timedelta(days=lookback_days)

        # Fetch news articles and check their publication dates
        articles = fetch_latest_news(api,["technology"], lookback_days=lookback_days)
        for article in articles:
            article_date = datetime.strptime(article["publishedAt"][:10],"%Y-%m-%d").date()  # Remove 'Z' from the end
            self.assertTrue(start_date <= article_date)
        return
    
    def test_fetch_latest_news_invalid_keyword(self):

        invalid_keywords = ["tech!", "science123", "business@news"]
        
        with self.assertRaises(ValueError):
            fetch_latest_news(api,invalid_keywords)

        return

if "__main__" == __name__:
    unittest.main()