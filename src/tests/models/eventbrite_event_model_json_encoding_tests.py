import json

from unittest import TestCase

from src.models.eventbrite_event_model import Eventbrite_Event

from src.tests.models.config import eventbrite_model_fields


class EventBriteModelJsonEncodingTest(TestCase):

    def test_eventbrite_to_json_has_required_props(self):
        """
            Test that all necessary props are encoded in JSON
        """

        event_mock = Eventbrite_Event(eventbrite_model_fields["source"], eventbrite_model_fields["source_id"],
                                      eventbrite_model_fields["name"])

        json_obj = event_mock.to_json()
        json_obj_as_dict = json.loads(json_obj)

        assert json_obj_as_dict["name"] == eventbrite_model_fields["name"]
        assert json_obj_as_dict["source"] == eventbrite_model_fields["source"]
        assert json_obj_as_dict["source_id"] == eventbrite_model_fields["source_id"]

    def test_eventbrite_to_json_has_all_props(self):
        """
            Test that all necessary props are encoded in JSON
        """

        event_mock = Eventbrite_Event(eventbrite_model_fields["source"], eventbrite_model_fields["source_id"],
                                      eventbrite_model_fields["name"])

        event_mock.start_time = eventbrite_model_fields["start_time"]
        event_mock.end_time = eventbrite_model_fields["end_time"]
        event_mock.description = eventbrite_model_fields["description"]

        event_mock.status = eventbrite_model_fields["status"]
        event_mock.capacity = eventbrite_model_fields["capacity"]
        event_mock.source_url = eventbrite_model_fields["source_url"]
        event_mock.venue_id = eventbrite_model_fields["venue_id"]
        event_mock.organization_id = eventbrite_model_fields["organization_id"]
        event_mock.invite_only = eventbrite_model_fields["invite_only"]
        event_mock.online_event = eventbrite_model_fields["online_event"]
        event_mock.organizer_id = eventbrite_model_fields["organizer_id"]
        event_mock.cost = eventbrite_model_fields["cost"]

        json_obj = event_mock.to_json()
        json_obj_as_dict = json.loads(json_obj)

        assert json_obj_as_dict["name"] == eventbrite_model_fields["name"]
        assert json_obj_as_dict["source"] == eventbrite_model_fields["source"]
        assert json_obj_as_dict["source_id"] == eventbrite_model_fields["source_id"]
        assert json_obj_as_dict["start_time"] == eventbrite_model_fields["start_time"]
        assert json_obj_as_dict["end_time"] == eventbrite_model_fields["end_time"]
        assert json_obj_as_dict["description"] == eventbrite_model_fields["description"]

        assert json_obj_as_dict["capacity"] == eventbrite_model_fields["capacity"]
        assert json_obj_as_dict["source_url"] == eventbrite_model_fields["source_url"]
        assert json_obj_as_dict["venue_id"] == eventbrite_model_fields["venue_id"]
        assert json_obj_as_dict["organization_id"] == eventbrite_model_fields["organization_id"]
        assert json_obj_as_dict["invite_only"] == eventbrite_model_fields["invite_only"]
        assert json_obj_as_dict["online_event"] == eventbrite_model_fields["online_event"]
        assert json_obj_as_dict["organizer_id"] == eventbrite_model_fields["organizer_id"]
