# hjc236_covid_dashboard
hjc236_covid_dashboard is a python project which generates a web dashboard with COVID-19 data and relevant news articles.

## Links
[GitHub](https://github.com/hjc236/hjc236_covid_dashboard)

[PyPi](https://pypi.org/manage/project/hjc236-covid-dashboard/releases/)


## Usage

**The program will not work successfully unless you have configured it with this API key. If you do not have an API key, you can get one at [this link](https://newsapi.org/docs/get-started).**

### Starting the dashboard
* Run ```main.py``` from the terminal.
* Navigate to ```127.0.0.1:5000/index``` in a web browser.

### Scheduling updates
At the bottom of the webpage, you can schedule and configure updates. Updates are able to replace the COVID-19 data and news articles with the most recent content from their respective APIs.
* Set the time you want your update to run
* Set a name for the update (it must not be the same as any existing updates)
* Choose whether you want the update to repeat or not. By default, updates repeat every 24 hours if selected. This can be changed in the ```config.json``` file.
* Choose whether you want to update COVID data, news articles, or both. At least one of these must be selected for the update to register.
* Submit, and you will see the update has been added to the sidebar on the left.

### Deleting updates
Updates can be deleted by pressing the [x] on them in the left sidebar.

### Deleting news articles
Updates can be deleted by pressing the [x] on them in the right sidebar. Deleted news articles will not come back when news is updated.

## COVID-19 Metrics
*All COVID-19 metrics are taken from the official [gov.uk API](https://coronavirus.data.gov.uk/details/developers-guide)*.

```Local 7-day infection rate in <local area>```: **the amount of COVID-19 cases in the local area over a recent 7-day period.**
* This will be a 7-day period starting from at least the previous day, because the current day's statistics are likely to be incomplete.
* The local area can be set in the configuration file.

```National 7-day infection rate in <national area>```: **the amount of COVID-19 cases in the national area over a recent 7-day period.**
* This will be a 7-day period starting from at least the previous day, because the current day's statistics are likely to be incomplete.
* The national area can be set in the configuration file.

```Current hospital cases (<national area>)```: **The amount of people currently hospitalised with COVID-19 in the national area**
* This is the most recent day the API has data for, which is likely to be a few days behind given the time it takes for the government to process the data.
* The national area can be set in the configuration file.

```Total deaths (<national area>)```: **The cumulative, total amount of COVID-19 related deaths in the national area**
* This is taken from the most recent total the API has data for, which may be a few days behind.

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


## Testing
The package can be tested by navigating to the file containing the package and running pytest in the terminal.
This means that pytest should be installed on your machine. If you do not have pytest, you can install it by running:

```bash
pip install pytest
```
Then navigate to the hjc236_covid_dashboard directory within the package's folder, and run pytest.
```bash
cd <path to project files>/hjc236_covid_dashboard
python -m pytest
```
**Note that you MUST run ```python -m pytest``` and not simply ```pytest``` from within this directory or the tests will not run successfully.**




## Troubleshooting
##### I am getting the error: *'news_api_key has not been set in config file'*
You need to register for an account at https://newsapi.org/ and insert your API key in the ```news_api_key``` field in the ```config.json``` file.

#### I am getting the error: *'Invalid News API key in configuration file'*
The API key in the ```config.json``` file is not correct. Ensure you have entered your own API key exactly as it appears on https://newsapi.org/.

#### Some of the news articles are not relevant to coronavirus
This is a limitation of the News API. Some articles may not be about Covid-19 directly but if they mention it enough they may still be displayed due to the way the keywords work. You can simply delete the irrelevant articles from the webpage, or try altering the keywords in ```config.json``` yourself

#### Some of the functions in this program are not used
This program was made to fit a specification which required the creation of some specific functions. In some cases, the role of these functions has been implemented in a different way and so they were not used. 

#### The COVID-19 data is incorrect
The data processing functions find the most recent valid values from the API, but this is often a few days behind because collecting it takes time to ensure the data is complete.

The 7-day infection rate metrics are always at least one day behind because the data for the most recent day is typically incomplete.
All Covid-19 data is taken from the UK government's statistics via the official [API](https://coronavirus.data.gov.uk/details/developers-guide).

#### I have another problem
Try looking at the log file which will have more information about what happened. It is called ```syslog.log```, in the same directory as the python files, unless you have changed this in the configuration file.

## License
[MIT](https://choosealicense.com/licenses/mit/)
