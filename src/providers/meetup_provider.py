from typing import Dict, Any

from src.event_provider import EventProviderABC


class MeetupEventProvider(EventProviderABC):
    """
    
    """

    def find_events(self, url: str, headers, query_params) -> Dict[str, Any]:
        """
        Fetch the content from url

        Args:
            url: url of target calendar

        Returns:
            response body in python native form
        """
        return {}
