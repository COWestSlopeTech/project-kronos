import os
from pprint import pprint
from unittest import TestCase

from src.providers.eventbrite_provider import EventbriteEventProvider


class EventbriteEventProviderTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_key = os.getenv("KRONOS_EVENTBRITE_API_KEY")
        if not cls.api_key:
            raise Exception("KRONOS_EVENTBRITE_API_KEY not found")

    def test_find_events(self):
        provider = EventbriteEventProvider(api_key=self.api_key)

        qp = {"location.address": "aspen", "location.within": "10km", "expand": "venue"}
        events = provider.find_events(qp)

        pprint(events)
