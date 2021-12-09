from hjc236_covid_dashboard.covid_news_handling import news_API_request, format_news_data, update_news
from hjc236_covid_dashboard.config_handler import ConfigError


def test_news_API_request():
    try:
        assert news_API_request()
        assert news_API_request('Covid COVID-19 coronavirus') == news_API_request()
    except ConfigError:
        # If the program fails here due to a ConfigError, this is because news_api_key has not been set correctly in
        # the config file. This will be excepted, since it is expected behaviour than an error is raised when there is
        # no valid API key in config.json.
        return


def test_update_news():
    try:
        update_news('test')
    except ConfigError:
        # If the program fails here due to a ConfigError, this is because news_api_key has not been set correctly in
        # the config file. This will be excepted, since it is expected behaviour than an error is raised when there is
        # no valid API key in config.json.
        return


def test_format_news_data():
    try:
        formatted_articles = format_news_data(news_API_request())
    except ConfigError:
        # If the program fails here due to a ConfigError, this is because news_api_key has not been set correctly in
        # the config file. This will be excepted, since it is expected behaviour than an error is raised when there is
        # no valid API key in config.json.
        return

    # Otherwise, check articles have been formatted correctly.
    for article in formatted_articles:

        # Do titles contain URL hyperlinks?
        assert article["url"] in article["title"]

        # If an article has something in the description field, has its content value been changed to the description?
        if article["description"] is not None:
            assert article["description"] == article["content"]
