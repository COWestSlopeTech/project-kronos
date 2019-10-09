from ..calendar_provider import CalendarProvider


def test_get_calendar_returns_a_dictionary():
    """
    NOTE: This is a pretty vacuous test, especially
    since we've got type hinting in place. However,
    we're putting in place to give pytest something
    to run until we get more substantive tests in place.
    """
    provider = CalendarProvider()
    assert isinstance(provider.get_calendar('dummy url'), dict)
