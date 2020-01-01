from typing import Dict, Any

from src.event_provider import EventProviderABC

from eventbrite import Eventbrite

from src.config.eventbrite_config import orgs


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
            url: url of /organizations/{organization_id}/events?{params}

        Returns:
            response body in python native form


        Example requests:
            * /organizations/350577373737/events?page_size=200&status=live
        """

        eventbrite = Eventbrite(self.api_key)

        all_events = []
        for key in orgs:

            # TODO: This doesn't work for any other organization than Roaring Fork Technologists because oauth2 needs to be setup.
            # 200 is the max page_size
            url = '/organizations/' + orgs[key] + '/events?page_size=200&status=live'
            resp = eventbrite.get(url)

            pagination_props = resp['pagination']
            events = resp['events']

            if(len(events) > 0):
                all_events.extend(events)

            if(pagination_props['has_more_items'] is True):
                print("There are more events which we can ignore for now...")

        return all_events


    def _get_headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}
