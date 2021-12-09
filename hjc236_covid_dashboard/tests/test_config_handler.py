from hjc236_covid_dashboard.config_handler import get_config_data, validate_config_data, ConfigError

def test_get_config_data():
    data = get_config_data()
    assert data["news_api_key"] is not None
    assert data["news_covid_terms"] is not None
    assert data["local_location"] is not None
    assert data["local_location_type"] is not None
    assert data["nation_location"] is not None


def test_validate_config_data():
    invalid_configuration = {
        "news_api_key": "not an API key",
        "news_covid_terms": "Covid COVID-19 coronavirus",
        "news_language": "wy4h",
        "number_of_articles_to_display": "-438",

        "local_location": "mars",
        "local_location_type": "planet",
        "nation_location": "3574",

        "repeat_interval_seconds": "0"
    }

    try:
        validate_config_data(invalid_configuration)

    except ConfigError:
        pass
    else:
        raise AssertionError("config_handler did not catch invalid configuration details")


