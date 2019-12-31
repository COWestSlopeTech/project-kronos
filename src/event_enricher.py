from typing import Any, Dict
from src.constants.constants import EVENT_SOURCE
# from src.models.event_model import Event
# from src.models.eventbrite_event_model import Eventbrite_Event



class EventEnricher:
    def enrich(self, data: Dict[str, Any], source: str) -> Dict[str, Any]:
        """
        I provide additional data for an event
        
        The data is enriched in-place, but also returned for convenience
        
        Args:
            data: calendar data in our datastore format

        Returns:
            enriched data
        """

        # TODO: Scrub the data on un-wanted properties.
        # TODO: Consider converting all objects into instance objects from the model definitions in src/models
        for ev in data:
            ev["source"] = source

        return data

