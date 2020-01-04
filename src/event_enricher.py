from typing import Any, Dict
from src.constants.constants import EVENT_SOURCE, EVENT_STATUS
from src.models.eventbrite_event_model import Eventbrite_Event


class EventEnricher:
    def enrich(self, data: Dict[str, Any], source: str) -> Dict[str, Any]:
        """
        I provide additional data for an event

        The data is enriched in-place, but also returned for convenience

        Args:
            data: calendar data in our datastore format

        Returns:
            enriched data as Event objects
        """

        encoded_data = []
        for ev in data:

            if (source == EVENT_SOURCE["EVENT_BRITE"]):

                event = Eventbrite_Event(EVENT_SOURCE["EVENT_BRITE"], ev["id"], ev["name"]["text"])

                # Optionals
                event.start_time = "{'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}"
                event.end_time = "{'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}"
                event.description = ev["description"]["text"]

                event.capacity = ev["capacity"]
                event.source_url = ev["resource_uri"]
                event.venue_id = ev["venue_id"]
                event.organization_id = ev["organization_id"]
                event.invite_only = ev["invite_only"]
                event.online_event = ev["online_event"]
                event.organizer_id = ev["organizer_id"]
                # event.image_url = ev["image_url"]
                # event.logo_url = ev["logo_id"]

                if (ev["is_free"]):
                    event.cost = 0
                else:
                    event.cost = ev["is_free"]

                if (ev["status"] == "live"):
                    event.status = EVENT_STATUS["ACTIVE"]
                else:
                    # TODO: determine all status types from EventBrite to set status more precisely
                    event.status = EVENT_STATUS["INACTIVE"]

                encoded_data.append(event)

            elif (EVENT_SOURCE["GOOGLE"]):
                print("TODO: Support Google enriching")

        return encoded_data
