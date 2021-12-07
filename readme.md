# hjc236-covid-dashboard

hjc236_covid_dashboard is a python project which generates a web dashboard with COVID-19 data and relevant news articles.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install hjc236_covid_dashboard.

```bash
pip install hjc236_covid-dashboard
```

## Usage

* Run ```main.py```
* Navigate to ```127.0.0.1:5000/index``` in a web browser.

## Config
The ```config.json```  file can be edited to customise the dashboard. Configuration options are:

```news_api_key```: The API key to use for [News API](https://newsapi.org/). **You will need to generate your own API key and put it here for the program to function.**

```news_covid_terms```: The list of search terms to use when determining which news articles to show. This should be a single string of search terms separated by spaces. Default is ```"covid COVID-19 coronavirus"```

```news_language```: The 2-letter language code for the language you wish to receive news articles in. Valid options: ```ar``` ```de``` ```en``` ```es``` ```fr``` ```he``` ```it``` ```nl``` ```no``` ```pt``` ```ru``` ```se``` ```ud``` ```zh```, or blank to get articles in all languages. Default is ```en```.

```number_of_articles_to_display```: The amount of articles to display on the webpage. Default is ```5```, more than this means the news articles are likely to extend beyond the rest of the webpage's content.

```local_location```: The location to get local COVID-19 data from. Default is ```exeter```.

```local_location_type```: The area type of the local location. **This must correspond to local location - for example, ```exeter``` has an area type of ```ltla```**.

```nation_location```: The country to get national COVID-19 data from. Valid options: ```england``` ```northern ireland``` ```scotland``` ```wales```. Default is ```england```.

```log_file_path```: The path to the log file. Default is ```syslog.log```.

```repeat_interval_seconds```: The amount of time before a repeating update repeats itself, in seconds. Default is ```86400``` which is 24 hours.

## License
[MIT](https://choosealicense.com/licenses/mit/)
