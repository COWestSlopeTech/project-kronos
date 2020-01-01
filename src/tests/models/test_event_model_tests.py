from unittest.mock import Mock

from src.models.event_model import Event
from src.models.eventbrite_event_model import Eventbrite_Event
from src.constants.constants import EVENT_SOURCE, EVENT_STATUS


def test_event_model_instantiates_tests():
    """

    """
    print("start")
    event_mock = Mock(spec=Event(EVENT_SOURCE["EVENT_BRITE"], 'testID', 'testName' ))

    # event_model = Event( EVENT_SOURCE["EVENT_BRITE"], ev["id"], ev["name"]["text"] )
    print("val --> ", event_mock.name)

    assert event_mock.name == 'testName'
