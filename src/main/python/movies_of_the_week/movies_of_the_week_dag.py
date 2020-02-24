import datetime

from airflow import DAG
from common.operators.web_requester_operator import WebRequesterOperator
from movies_of_the_week.operators.movie_title_parser_operator import MovieTitleParserOperator
# Take today as start
date = datetime.datetime.now().strftime('%Y-%m-%d')

default_args = {
    "owner": "slack_movies",
    "start_date": date,
    'retries': 2,
    'retry_delay': datetime.timedelta(minutes=2),
    'catchup_by_default': False
}

# Input information
theater_webpage_dic = {"CINEMA Filmtheater":"https://www.cinema-muenchen.de/filme.html"}

dag = DAG("slack_movies_of_the_week", schedule_interval=None, default_args=default_args)


scrape_theater_websites = WebRequesterOperator(
    task_id='scrape_theater_websites',
    provide_context=True,
    dag=dag,
    theater_website_dic = theater_webpage_dic
)

parse_websites = MovieTitleParserOperator(
    task_id='parse_websites',
    provide_context=True,
    dag=dag,
    prior_task_id="scrape_theater_websites"
)

scrape_theater_websites >> parse_websites