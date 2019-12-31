import os
from unittest import TestCase

from src.providers.eventbrite_provider import EventbriteEventProvider


class EventbriteEventProviderTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_key = os.getenv("EVENTBRITE_KEY")
        if not cls.api_key:
            raise Exception("EVENTBRITE_KEY not found")

    def test_find_events(self):
        provider = EventbriteEventProvider(api_key=self.api_key)

        # TODO: decouple from the actual EventBrite API to follow best practice
        assert isinstance(provider.find_events(query_params=""), list)
