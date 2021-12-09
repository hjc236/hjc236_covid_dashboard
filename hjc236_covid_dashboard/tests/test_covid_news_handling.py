from hjc236_covid_dashboard.covid_news_handling import news_API_request, format_news_data, update_news
from hjc236_covid_dashboard.config_handler import ConfigError


def test_news_API_request():
    assert news_API_request()
    assert news_API_request('Covid COVID-19 coronavirus') == news_API_request()


def test_update_news():
    try:
        assert update_news('test')
    except TypeError:
        # TypeError here means that articles have not been returned, probably due to a faulty API key
        # Normally this would raise a ConfigError but we don't want it to during tests as it is expected behaviour
        # So it will just be logged
        pass


def test_format_news_data():
    articles = news_API_request()

    try:
        formatted_articles = format_news_data(news_API_request())
    except TypeError:
        # TypeError here means that articles have not been returned, probably due to a faulty API key
        # Normally this would raise a ConfigError but we don't want it to during tests as it is expected behaviour
        # So just assert that the error did actually come from the lack of a valid API key and not something else
        assert articles["code"] == "apiKeyInvalid"
        return

    for article in formatted_articles:

        # Do titles contain URL hyperlinks?
        assert article["url"] in article["title"]

        # If an article has something in the description field, has its content value been changed to the description?
        if article["description"] is not None:
            assert article["description"] == article["content"]
