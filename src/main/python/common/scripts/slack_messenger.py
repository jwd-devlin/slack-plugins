import asyncio

import nest_asyncio
import slack
#For jupyter
nest_asyncio.apply()
import logging

class SlackMessenger:

    def __init__(self, api_token):
        self._api_token = api_token
        self._client = slack.WebClient(token=self._api_token)

    def message_channel(self, message, channel):
        response = self._client.chat_postMessage(
            channel=channel,
            text=message)
        logging.info(f' Result of response successful: {response["ok"]}')