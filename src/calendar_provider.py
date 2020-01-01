import os

from src.providers.eventbrite_provider import EventbriteEventProvider
from src.event_enricher import EventEnricher
from src.constants.constants import EVENT_SOURCE


class CalendarProvider:

    def __init__(self):
        pass

    def find_events(self, name: str, url: str):
        if name == EVENT_SOURCE["EVENT_BRITE"]:
            event_brite: EventbriteEventProvider = EventbriteEventProvider(api_key=os.getenv("EVENTBRITE_KEY"))

            resp = event_brite.find_events(query_params="expand=venue")

<<<<<<< HEAD
            enricher = EventEnricher()
            events = enricher.enrich(resp, EVENT_SOURCE["EVENT_BRITE"])

            return events

=======
            return resp
>>>>>>> master
