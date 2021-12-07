# hjc236-covid-dashboard

hjc236_covid_dashboard is a python project which generates a web dashboard with COVID-19 data and relevant news articles.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install hjc236_covid_dashboard.

```bash
pip install hjc236_covid_dashboard
```

## Usage

### Starting the dashboard
* Run ```main.py``` from the terminal.
* Navigate to ```127.0.0.1:5000/index``` in a web browser.

###Scheduling updates
* Set the time you want your update to run
* Set a name for the update (it must not be the same as any existing updates)
* Choose whether you want the update to repeat or not. By default, updates repeat every 24 hours if selected. This can be changed in the ```config.json``` file.
* Choose whether you want to update COVID data, news articles, or both. At least one of these must be selected for the update to register.
* Submit, and you will see the update has been added to the sidebar on the left.

###Deleting updates
Updates can be deleted by pressing the [x] on them in the left sidebar.

###Deleting news articles
Updates can be deleted by pressing the [x] on them in the right sidebar. Deleted news articles will not come back when news is updated.

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

## FAQ
#####I am getting the error: *'news_api_key has not been set in config file'*
You need to register for an account at https://newsapi.org/ and insert your API key in the ```news_api_key``` field in the ```config.json``` file.

####I am getting the error: *'Invalid News API key in configuration file'*
The API key in the ```config.json``` file is not correct. Ensure you have entered your own API key exactly as it appears on https://newsapi.org/

####Some of the news articles are not relevant to coronavirus
This is a limitation of the News API. Some articles may not be about Covid-19 directly but if they mention it enough they may still be displayed due to the way the keywords work. You can simply delete the irrelevant articles from the webpage, or try altering the keywords in ```config.json``` yourself

####Some of the functions in this program are not used
This program was made to fit a specification which required the creation of some specific functions. In some cases, the role of these functions has been implemented in a different way and so they were not used. 

####The COVID-19 data is incorrect
The data processing functions find the most recent valid values from the API, but this is often a few days behind because collecting the data takes time. All Covid-19 data is taken from the UK government's statistics via the official [API](https://coronavirus.data.gov.uk/details/developers-guide).

## License
[MIT](https://choosealicense.com/licenses/mit/)
