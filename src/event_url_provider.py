from src.constants import EVENT_SOURCE
from typing import Dict


class EventUrlProvider:
    """
    I am the source of known event calendar urls
    """

    def get_urls(self) -> Dict[str, str]:
        """
        Return a map of event name -> url
        """
        return {
            EVENT_SOURCE["EVENT_BRITE"]: "https://www.eventbriteapi.com/v3"
        }
