import json

from unittest import TestCase

from src.models.event_model import Event

from src.tests.models.config import event_model_fields


class EventModelJsonEncodingTest(TestCase):

    def test_event_model_has_optional_props(self):
        """
            Test that we are encoding required props
        """

        event_mock = Event(event_model_fields["source"], event_model_fields["source_id"], event_model_fields["name"])

        event_mock.__setattr__("start_time", event_model_fields["start_time"])
        event_mock.__setattr__("end_time", event_model_fields["end_time"])
        event_mock.__setattr__("description", event_model_fields["description"])

        assert event_mock.__getattribute__("start_time") == event_model_fields["start_time"]
        assert event_mock.__getattribute__("start_time") == event_model_fields["end_time"]
        assert event_mock.__getattribute__("description") == event_model_fields["description"]

    def test_event_to_json_has_all_props(self):
        """
            Test that we are encoding required and optional props
        """

        event_mock = Event(event_model_fields["source"], event_model_fields["source_id"], event_model_fields["name"])

        event_mock.__setattr__("start_time", event_model_fields["start_time"])
        event_mock.__setattr__("end_time", event_model_fields["end_time"])
        event_mock.__setattr__("description", event_model_fields["description"])

        json_obj = event_mock.to_json()

        json_obj_as_dict = json.loads(json_obj)
        assert json_obj_as_dict["name"] == event_model_fields["name"]
        assert json_obj_as_dict["source"] == event_model_fields["source"]
        assert json_obj_as_dict["source_id"] == event_model_fields["source_id"]
        assert json_obj_as_dict["start_time"] == event_model_fields["start_time"]
        assert json_obj_as_dict["end_time"] == event_model_fields["end_time"]
        assert json_obj_as_dict["description"] == event_model_fields["description"]
