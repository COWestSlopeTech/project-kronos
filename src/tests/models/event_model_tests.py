import json
from unittest.mock import Mock
from unittest import TestCase

from src.models.event_model import Event

from src.tests.models.config import event_model_fields


class EventModelTest(TestCase):

    event_mock = Event(event_model_fields["source"], event_model_fields["source_id"], event_model_fields["name"])

    def test_event_model_has_required_props(self):
        """
            Testing that properties are set in the object
        """

        assert self.event_mock.__getattribute__("name") == event_model_fields["name"]
        assert self.event_mock.__getattribute__("source") == event_model_fields["source"]
        assert self.event_mock.__getattribute__("source_id") == event_model_fields["source_id"]

    def test_event_model_has_optional_props(self):
        """
            Testing that properties are set in the object
        """

        self.event_mock.__setattr__("start_time", event_model_fields["start_time"])
        self.event_mock.__setattr__("end_time", event_model_fields["end_time"])
        self.event_mock.__setattr__("description", event_model_fields["description"])

        assert self.event_mock.__getattribute__("start_time") == event_model_fields["start_time"]
        assert self.event_mock.__getattribute__("start_time") == event_model_fields["end_time"]
        assert self.event_mock.__getattribute__("description") == event_model_fields["description"]

