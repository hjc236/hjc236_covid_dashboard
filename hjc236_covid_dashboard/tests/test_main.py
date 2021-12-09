import sched
import time

from hjc236_covid_dashboard.covid_news_handling import news_API_request

from hjc236_covid_dashboard.main import run_scheduled_update, schedule_update, remove_update_from_update_list, \
    get_event_update_name, delete_news_article, delete_update

global webpage_news_articles
global webpage_covid_data

web_scheduler = sched.scheduler(time.time, time.sleep)
updates = []


def test_run_scheduled_update():
    run_scheduled_update("Test Update", repeat=False, covid=True, news=True)


def test_schedule_update():
    # Reset updates and scheduler before running tests
    for update in web_scheduler.queue:
        web_scheduler.cancel(update)

    schedule_update("00:00", "News and Covid Update", repeat=False, covid=True, news=True)


def test_remove_update_from_update_list():
    # Reset updates and scheduler before running tests
    for update in web_scheduler.queue:
        web_scheduler.cancel(update)

    schedule_update("00:00", "Update that gets deleted", repeat=False, covid=True, news=True)
    remove_update_from_update_list("Update that gets deleted")


def test_delete_update():
    # Reset updates and scheduler before running tests
    global updates
    updates = []
    for update in web_scheduler.queue:
        web_scheduler.cancel(update)

    schedule_update("00:00", "Test Update", repeat=False, covid=False, news=True)
    delete_update("Test Update")


def test_get_event_update_name():
    # Reset updates and scheduler before running tests
    global updates
    updates = []
    for update in web_scheduler.queue:
        web_scheduler.cancel(update)

    web_scheduler.enter(100, 1, run_scheduled_update, ("test update", False, True, True))


def test_delete_news_article():
    global webpage_news_articles
    webpage_news_articles = news_API_request()

    length_before_article_deleted = len(webpage_news_articles)

    article_for_deletion_title = webpage_news_articles[0]["title"]
    delete_news_article(article_for_deletion_title)
