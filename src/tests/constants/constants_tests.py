from unittest import TestCase

from src.constants.constants import EVENT_SOURCE, EVENT_STATUS


class ConstantsTest(TestCase):

    def test_event_source(self):
        """
            Testing that constants are what we expect them to be
        """

        assert EVENT_SOURCE["EVENT_BRITE"] == "EventBrite"
        assert EVENT_SOURCE["GOOGLE"] == "Google"

    def test_event_status(self):
        """
            Testing that constants are what we expect them to be
        """

        assert EVENT_STATUS["ACTIVE"] == "ACTIVE"
        assert EVENT_STATUS["INACTIVE"] == "INACTIVE"
