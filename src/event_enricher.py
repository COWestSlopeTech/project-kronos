from typing import Any, Dict


class EventEnricher:
    def enrich(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        I provide additional data for an event

        The data is enriched in-place, but also returned for convenience

        Args:
            data: calendar data in our datastore format

        Returns:
            enriched data
        """
        return data
