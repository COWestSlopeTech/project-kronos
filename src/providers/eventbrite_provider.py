from pathlib import PurePath
from pprint import pprint
from typing import Dict, Any

import requests

from src.event_provider import EventProviderABC


class EventbriteEventProvider(EventProviderABC):
    """

    """

    def __init__(self, api_key: str):
        """
        Todo:
            * should our ABC have a common init sig, perhaps store all variants of creds
        """
        self.api_key = api_key
        self.url_prefix = "https://www.eventbriteapi.com/v3"

        if not self.api_key:
            raise Exception("Eventbrite API key not found")

    def find_events(self, query_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fetch the content from url

        Args:
            url: url of target calendar

        Returns:
            response body in python native form
        
        See Also:
            * https://pypi.org/project/requests/
        
        Example requests:
            * https://www.eventbriteapi.com/v3/events/search?location.address=vancovuer&location.within=10km&expand=venue   -H 'Authorization: Bearer PERSONAL_OAUTH_TOKEN'
        """
        url = f"{self.url_prefix}/events/search"
        headers = self._get_headers()
        resp = requests.get(url, headers=headers, params=query_params)

        if resp.status_code != 200:
            msg = f"Error searching Eventbrite: {resp.status_code}"
            print(msg)
            pprint(resp.json())
            raise Exception(msg)

        return resp.json()

    def _get_headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}
