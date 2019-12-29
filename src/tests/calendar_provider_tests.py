from ..calendar_provider import CalendarProvider


def test_no_name_find_events_returns_none():
    """
    NOTE: This is a pretty vacuous test, especially
    since we've got type hinting in place. However,
    we're putting in place to give pytest something
    to run until we get more substantive tests in place.
    """
    provider = CalendarProvider()
    assert isinstance(provider.find_events('', 'dummy url'), None)
