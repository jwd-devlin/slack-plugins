# slack-plugins
(*) item in progress.

##Description:
The follow project uses airflow to routinely publish some helpful announcements on slack.


- Movies_Of_The_Week DAG(*)
  - Scrapes a list of local Cinemas and Posts to Slack the Movies for that week. #Random Channel.
  - Set to run once a week.
- Whos_Out_Today
  - Posts information about people are on leave from Personio. #General Channel.
  - Set to run Daily.


## How to run:

#### Setup:
- Slack Bot:

- Airflow Install

- Running