import os

from src.providers.eventbrite_provider import EventbriteEventProvider


class CalendarProvider:

    def __init__(self):
        pass

    def find_events(self, name: str, url: str):
        if name == "eventbrite":
            event_brite: EventbriteEventProvider = EventbriteEventProvider(api_key=os.getenv("EVENTBRITE_KEY"))
            resp = event_brite.find_events(
                query_params="location.latitude=39.4000702&location.longitude=-107.208836&location.within=50km&expand=venue")
            return resp