from unittest import TestCase

from src.models.eventbrite_event_model import Eventbrite_Event

from src.tests.models.config import eventbrite_model_fields


class EventBriteModelTest(TestCase):

    def test_eventbrite_event_model_has_required_props(self):
        """
            Testing that properties are set in the object
        """
        event_mock = Eventbrite_Event(eventbrite_model_fields["source"], eventbrite_model_fields["source_id"],
                                      eventbrite_model_fields["name"])

        assert event_mock.name == eventbrite_model_fields["name"]
        assert event_mock.source == eventbrite_model_fields["source"]
        assert event_mock.source_id == eventbrite_model_fields["source_id"]

    def test_eventbrite_event_model_has_optional_props(self):
        """
            Testing that properties are set in the object
        """

        event_mock = Eventbrite_Event(eventbrite_model_fields["source"], eventbrite_model_fields["source_id"],
                                      eventbrite_model_fields["name"])

        event_mock.start_time = eventbrite_model_fields["start_time"]
        event_mock.end_time = eventbrite_model_fields["end_time"]
        event_mock.description = eventbrite_model_fields["description"]

        assert event_mock.start_time == eventbrite_model_fields["start_time"]
        assert event_mock.start_time == eventbrite_model_fields["end_time"]
        assert event_mock.description == eventbrite_model_fields["description"]

        event_mock.status = eventbrite_model_fields["status"]
        event_mock.capacity = eventbrite_model_fields["capacity"]
        event_mock.source_url = eventbrite_model_fields["source_url"]
        event_mock.venue_id = eventbrite_model_fields["venue_id"]
        event_mock.organization_id = eventbrite_model_fields["organization_id"]
        event_mock.invite_only = eventbrite_model_fields["invite_only"]
        event_mock.online_event = eventbrite_model_fields["online_event"]
        event_mock.organizer_id = eventbrite_model_fields["organizer_id"]
        event_mock.cost = eventbrite_model_fields["cost"]

        assert event_mock.capacity == eventbrite_model_fields["capacity"]
        assert event_mock.source_url == eventbrite_model_fields["source_url"]
        assert event_mock.venue_id == eventbrite_model_fields["venue_id"]
        assert event_mock.organization_id == eventbrite_model_fields["organization_id"]
        assert event_mock.invite_only == eventbrite_model_fields["invite_only"]
        assert event_mock.online_event == eventbrite_model_fields["online_event"]
        assert event_mock.organizer_id == eventbrite_model_fields["organizer_id"]
