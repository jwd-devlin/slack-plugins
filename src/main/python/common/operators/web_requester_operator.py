from airflow.models import BaseOperator
from airflow.utils import apply_defaults
from common.scripts.web_requester import WebRequester

class WebRequesterOperator(BaseOperator):

    @apply_defaults
    def __init__(self, theater_website_dic,
                 *args, **kwargs):
        super(WebRequesterOperator, self).__init__(*args, **kwargs)
        self._theater_website_dic = theater_website_dic

    def execute(self, context):
        # Request information from the websites
        response = WebRequester().request_response(self._theater_website_dic)

        return response