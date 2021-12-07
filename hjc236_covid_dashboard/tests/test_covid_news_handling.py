from hjc236_covid_dashboard.covid_news_handling import news_API_request, format_news_data, update_news


def test_news_API_request():
    assert news_API_request()
    assert news_API_request('Covid COVID-19 coronavirus') == news_API_request()


def test_update_news():
    update_news('test')


def test_format_news_data():
    unformatted = news_API_request()
    formatted = format_news_data(news_API_request())

    for article in formatted:

        # Do titles contain URL links?
        assert article["url"] in article["title"]

        # If an article has a description, has its content value been changed to the description?
        if article["description"] is not None:
            assert article["content"] == article["description"]



