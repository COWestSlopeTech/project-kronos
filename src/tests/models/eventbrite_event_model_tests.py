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

        assert event_mock.__getattribute__("name") == eventbrite_model_fields["name"]
        assert event_mock.__getattribute__("source") == eventbrite_model_fields["source"]
        assert event_mock.__getattribute__("source_id") == eventbrite_model_fields["source_id"]

    def test_eventbrite_event_model_has_optional_props(self):
        """
            Testing that properties are set in the object
        """

        event_mock = Eventbrite_Event(eventbrite_model_fields["source"], eventbrite_model_fields["source_id"],
                                      eventbrite_model_fields["name"])

        event_mock.__setattr__("start_time", eventbrite_model_fields["start_time"])
        event_mock.__setattr__("end_time", eventbrite_model_fields["end_time"])
        event_mock.__setattr__("description", eventbrite_model_fields["description"])

        assert event_mock.__getattribute__("start_time") == eventbrite_model_fields["start_time"]
        assert event_mock.__getattribute__("start_time") == eventbrite_model_fields["end_time"]
        assert event_mock.__getattribute__("description") == eventbrite_model_fields["description"]

        event_mock.__setattr__("status", eventbrite_model_fields["status"])
        event_mock.__setattr__("capacity", eventbrite_model_fields["capacity"])
        event_mock.__setattr__("source_url", eventbrite_model_fields["source_url"])
        event_mock.__setattr__("venue_id", eventbrite_model_fields["venue_id"])
        event_mock.__setattr__("organization_id", eventbrite_model_fields["organization_id"])
        event_mock.__setattr__("invite_only", eventbrite_model_fields["invite_only"])
        event_mock.__setattr__("online_event", eventbrite_model_fields["online_event"])
        event_mock.__setattr__("organizer_id", eventbrite_model_fields["organizer_id"])
        event_mock.__setattr__("cost", eventbrite_model_fields["cost"])

        assert event_mock.__getattribute__("capacity") == eventbrite_model_fields["capacity"]
        assert event_mock.__getattribute__("source_url") == eventbrite_model_fields["source_url"]
        assert event_mock.__getattribute__("venue_id") == eventbrite_model_fields["venue_id"]
        assert event_mock.__getattribute__("organization_id") == eventbrite_model_fields["organization_id"]
        assert event_mock.__getattribute__("invite_only") == eventbrite_model_fields["invite_only"]
        assert event_mock.__getattribute__("online_event") == eventbrite_model_fields["online_event"]
        assert event_mock.__getattribute__("organizer_id") == eventbrite_model_fields["organizer_id"]
